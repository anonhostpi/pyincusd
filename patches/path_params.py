r"""Patch: fix missing path parameters in all API methods.

OpenAPI Generator drops path parameters ({name}, {fingerprint},
{networkName}, etc.) from generated method signatures. The URL
templates have placeholders but _path_params is never populated.

This patch wraps every _*_serialize method on every API class to
auto-populate _path_params from a thread-local store that callers
set before invoking the API method.

Usage after applying:
    from pyincusd.patches.path_params import set_path_params
    set_path_params(name="foo")
    result = await api.instance_get()  # URL becomes /1.0/instances/foo
"""

from __future__ import annotations
import re
import threading
import functools
import pkgutil
import importlib
from pyincusd import api as api_pkg, api_client

_thread_local = threading.local()
_original_param_serialize = api_client.ApiClient.param_serialize
_patched = False


def set_path_params(**params):
    """Set path parameters for the next API call (thread-safe)."""
    _thread_local.path_params = params


def _patched_param_serialize(self, method, resource_path, path_params=None, **kwargs):
    """Injects thread-local path params into the URL."""
    if path_params is None:
        path_params = {}

    # Merge thread-local path params
    extra = getattr(_thread_local, 'path_params', {})
    if extra:
        path_params.update(extra)
        _thread_local.path_params = {}  # consume

    return _original_param_serialize(
        self, method, resource_path, path_params=path_params, **kwargs)


def apply():
    global _patched
    if _patched:
        return
    api_client.ApiClient.param_serialize = _patched_param_serialize
    _patched = True


def revert():
    global _patched
    api_client.ApiClient.param_serialize = _original_param_serialize
    _patched = False
