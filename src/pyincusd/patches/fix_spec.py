"""Preprocess the Incus Swagger spec to inject missing path parameter declarations.

The Incus spec uses {placeholders} in URL paths but doesn't declare them
as `in: path` parameters. This script scans every path, finds undeclared
placeholders, and adds them as required string path parameters.

Usage:
    python fix_spec.py rest-api.yaml rest-api-fixed.yaml
"""

import re
import sys
import yaml


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

    with open(output_path, "w") as f:
        yaml.dump(spec, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"Fixed {fixed_count} missing path parameter declarations.")
    print(f"Written to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.yaml> <output.yaml>")
        sys.exit(1)
    fix_spec(sys.argv[1], sys.argv[2])
