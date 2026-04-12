"""Opt-in patches for pyincusd's generated code.

Each patch module has an apply() function. Import and call it to opt in:

    from pyincusd.patches import image_upload
    image_upload.apply()

Or apply all patches at once:

    from pyincusd.patches import apply_all
    apply_all()
"""

import importlib
import pkgutil


def apply_all():
    """Discover and apply all patches in this package."""
    for info in pkgutil.iter_modules(__path__):
        if info.name.startswith("_"):
            continue
        mod = importlib.import_module(f"{__name__}.{info.name}")
        if hasattr(mod, "apply"):
            mod.apply()
