"""Patch: fix metadata_configuration_get response deserialization.

The generated MetadataConfigurationGet200Response types the metadata
field as str, but the API actually returns a nested dict describing
all available configuration keys. This patch replaces from_dict to
accept the dict as-is.
"""

from __future__ import annotations
from pyincusd.models.metadata_configuration_get200_response import MetadataConfigurationGet200Response

_original_from_dict = MetadataConfigurationGet200Response.from_dict


@classmethod
def _patched_from_dict(cls, obj: dict):
    if obj is None:
        return None
    return cls.model_construct(
        metadata=obj.get("metadata"),
        status=obj.get("status"),
        status_code=obj.get("status_code"),
        type=obj.get("type"),
    )


def apply():
    """Patch MetadataConfigurationGet200Response to accept dict metadata."""
    MetadataConfigurationGet200Response.from_dict = _patched_from_dict


def revert():
    """Revert the patch."""
    MetadataConfigurationGet200Response.from_dict = _original_from_dict
