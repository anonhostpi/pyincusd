"""Preprocess the Incus Swagger spec to fix generator-breaking issues.

Fix 1: Inject missing path parameter declarations.
    The Incus spec uses {placeholders} in URL paths but doesn't declare
    them as `in: path` parameters.

Fix 2: Rewrite POST /1.0/images to use multipart/form-data.
    The spec declares two `in: body` params (image + raw_image), which
    is invalid in Swagger 2.0 and causes openapi-generator to drop both,
    leaving the operation bodyless. Rewrite as multipart with metadata
    and rootfs file uploads — matches what incusd actually accepts.

Usage:
    python fix_spec.py rest-api.yaml rest-api-fixed.yaml
"""

import re
import sys
import yaml


def _fix_operation_metadata(spec):
    """Loosen Operation.metadata and Operation.resources to Dict[str, Any].

    metadata: The generator mis-translates empty-schema additionalProperties
    as Dict[str, Dict[str, Any]], which rejects flat string values like
    the image upload response `{"fingerprint": "abc...", "size": "123"}`.

    resources: The spec declares values as `array of string`, but the
    server can return null for entries (e.g. `{"cluster": null}`), which
    pydantic rejects because List[StrictStr] disallows None.

    Both are fixed by deleting additionalProperties, yielding Dict[str, Any]
    per JSON Schema's "allow anything" default.
    """
    fixed = 0
    props = spec.get("definitions", {}).get("Operation", {}).get("properties", {})
    for name in ("metadata", "resources"):
        p = props.get(name)
        if p is not None and "additionalProperties" in p:
            del p["additionalProperties"]
            fixed += 1
    return fixed


def _fix_images_post(spec):
    op = spec.get("paths", {}).get("/1.0/images", {}).get("post")
    if not op:
        return 0
    op["consumes"] = ["multipart/form-data"]
    params = [p for p in op.get("parameters", []) if p.get("in") != "body"]
    params.extend([
        {
            "name": "metadata",
            "in": "formData",
            "type": "file",
            "required": True,
            "description": "Image metadata tarball (incus.tar.xz)",
        },
        {
            "name": "rootfs",
            "in": "formData",
            "type": "file",
            "required": True,
            "description": "Image rootfs (squashfs or tarball)",
        },
    ])
    op["parameters"] = params
    return 1


def _fix_instances_post(spec):
    """Drop the secondary `raw_backup` body from POST /1.0/instances.

    Swagger 2.0 forbids multiple `in: body` params on one operation;
    the generator silently drops both, leaving the operation bodyless.
    We keep `instance` (the structured create body) and drop
    `raw_backup` (tarball restore — can be done via a separate client
    if needed).
    """
    op = spec.get("paths", {}).get("/1.0/instances", {}).get("post")
    if not op:
        return 0
    bodies = [p for p in op.get("parameters", []) if p.get("in") == "body"]
    if len(bodies) <= 1:
        return 0
    op["parameters"] = [
        p for p in op.get("parameters", [])
        if not (p.get("in") == "body" and p.get("name") == "raw_backup")
    ]
    return 1


def fix_spec(input_path: str, output_path: str):
    with open(input_path) as f:
        spec = yaml.safe_load(f)

    fixed_count = 0

    for path_url, path_obj in spec.get("paths", {}).items():
        placeholders = re.findall(r"\{(\w+)\}", path_url)
        if not placeholders:
            continue

        # Collect path-level declared path params
        path_level_params = {
            p["name"] for p in path_obj.get("parameters", [])
            if p.get("in") == "path"
        }

        for method in ("get", "put", "post", "patch", "delete", "head"):
            op = path_obj.get(method)
            if op is None:
                continue

            # Collect operation-level declared path params
            op_params = {
                p["name"] for p in op.get("parameters", [])
                if p.get("in") == "path"
            }
            declared = path_level_params | op_params

            # Find undeclared placeholders
            for placeholder in placeholders:
                if placeholder not in declared:
                    # Add the missing path parameter
                    if "parameters" not in op:
                        op["parameters"] = []
                    op["parameters"].append({
                        "name": placeholder,
                        "in": "path",
                        "type": "string",
                        "required": True,
                        "description": f"Path parameter: {placeholder}",
                    })
                    fixed_count += 1

    images_post_fixed = _fix_images_post(spec)
    instances_post_fixed = _fix_instances_post(spec)
    op_metadata_fixed = _fix_operation_metadata(spec)

    with open(output_path, "w") as f:
        yaml.dump(spec, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"Fixed {fixed_count} missing path parameter declarations.")
    if images_post_fixed:
        print("Fixed POST /1.0/images body params (multipart/form-data).")
    if instances_post_fixed:
        print("Fixed POST /1.0/instances body params (dropped raw_backup).")
    if op_metadata_fixed:
        print("Fixed Operation.metadata additionalProperties quirk.")
    print(f"Written to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.yaml> <output.yaml>")
        sys.exit(1)
    fix_spec(sys.argv[1], sys.argv[2])
