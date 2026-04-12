"""Patch: enable binary file upload for images_post().

The generated ImagesApi.images_post() only accepts header parameters
(X-Incus-aliases, X-Incus-fingerprint, etc.) but has no way to pass
the actual image body or multipart files. The Swagger spec defines
this endpoint with application/octet-stream, which OpenAPI Generator
maps to header-only params.

This patch replaces _images_post_serialize to accept body and files
parameters, enabling:

    api.images_post(
        x_incus_aliases='[{"name": "my-image"}]',
        files={
            "metadata": ("meta.tar.xz", open("meta.tar.xz", "rb"), "application/octet-stream"),
            "rootfs": ("rootfs.squashfs", open("rootfs.squashfs", "rb"), "application/octet-stream"),
        },
    )
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union
from pyincusd.api import images_api
from pyincusd.api_client import RequestSerialized

# Capture the unpatched method at import time — immune to double-apply pollution
_original = images_api.ImagesApi._images_post_serialize


def _patched_images_post_serialize(
    self,
    project=None,
    x_incus_secret=None,
    x_incus_fingerprint=None,
    x_incus_aliases=None,
    x_incus_properties=None,
    x_incus_public=None,
    x_incus_filename=None,
    x_incus_profiles=None,
    _request_auth=None,
    _content_type=None,
    _headers=None,
    _host_index=0,
    body: Optional[bytes] = None,
    files: Optional[Dict[str, Any]] = None,
) -> RequestSerialized:
    _path_params: Dict[str, str] = {}
    _query_params: List[Tuple[str, str]] = []
    _header_params: Dict[str, Optional[str]] = _headers or {}
    _form_params: List[Tuple[str, str]] = []
    _files: Dict[str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]] = files or {}
    _body_params: Optional[bytes] = body

    if project is not None:
        _query_params.append(('project', project))
    if x_incus_secret is not None:
        _header_params['X-Incus-secret'] = x_incus_secret
    if x_incus_fingerprint is not None:
        _header_params['X-Incus-fingerprint'] = x_incus_fingerprint
    if x_incus_aliases is not None:
        _header_params['X-Incus-aliases'] = x_incus_aliases
    if x_incus_properties is not None:
        _header_params['X-Incus-properties'] = x_incus_properties
    if x_incus_public is not None:
        _header_params['X-Incus-public'] = x_incus_public
    if x_incus_filename is not None:
        _header_params['X-Incus-filename'] = x_incus_filename
    if x_incus_profiles is not None:
        _header_params['X-Incus-profiles'] = x_incus_profiles

    if _content_type:
        _header_params['Content-Type'] = _content_type
    elif body is not None:
        _header_params['Content-Type'] = 'application/octet-stream'
    elif not files:
        _header_params['Content-Type'] = 'application/json'

    if 'Accept' not in _header_params:
        _header_params['Accept'] = 'application/json'

    return self.api_client.param_serialize(
        method='POST',
        resource_path='/1.0/images',
        path_params=_path_params,
        query_params=_query_params,
        header_params=_header_params,
        body=_body_params,
        post_params=_form_params,
        files=_files,
        auth_settings=[],
        collection_formats={},
        _host=None,
        _request_auth=_request_auth,
    )


def apply():
    """Patch ImagesApi._images_post_serialize to support file uploads."""
    images_api.ImagesApi._images_post_serialize = _patched_images_post_serialize


def revert():
    """Revert to the original unpatched method."""
    images_api.ImagesApi._images_post_serialize = _original
