"""Opt-in patches for pyincusd's generated code.

Each patch module has an apply() function. Import and call it to opt in:

    from pyincusd.patches import image_upload
    image_upload.apply()

Or apply all patches at once:

    from pyincusd.patches import apply_all
    apply_all()
"""


def apply_all():
    """Apply all available patches."""
    from pyincusd.patches import image_upload
    image_upload.apply()
