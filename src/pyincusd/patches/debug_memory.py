"""Patch: fix instance_debug_memory_get to return bytes.

The generated method has void return type, but the endpoint returns
application/octet-stream (a raw memory dump). This patch overrides
the response handling to return raw bytes.
"""

from __future__ import annotations
from pyincusd.api import instances_api

_original = instances_api.InstancesApi.instance_debug_memory_get


async def _patched_debug_memory_get(self, name, **kwargs):
    """Get memory debug info as raw bytes (VMs only)."""
    # Use the without_preload_content variant to get raw response
    response = await instances_api.InstancesApi.instance_debug_memory_get_without_preload_content(
        self, name, **kwargs)
    return response.content


def apply():
    instances_api.InstancesApi.instance_debug_memory_get = _patched_debug_memory_get


def revert():
    instances_api.InstancesApi.instance_debug_memory_get = _original
