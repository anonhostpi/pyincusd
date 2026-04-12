# pyincusd.patches

Opt-in fixes for gaps in the auto-generated code.

## Usage

Apply a specific patch:

```python
from pyincusd.patches import image_upload
image_upload.apply()
```

Apply all available patches:

```python
from pyincusd.patches import apply_all
apply_all()
```

Revert a patch:

```python
from pyincusd.patches import image_upload
image_upload.revert()
```

## Available patches

### `image_upload`

Enables binary file upload for `ImagesApi.images_post()`. The generated
method only accepts header parameters but has no way to pass image files.
This patch adds `body` and `files` parameters to `_images_post_serialize`.

```python
from pyincusd.patches import image_upload
image_upload.apply()

api.images_post(
    x_incus_aliases='[{"name": "my-image"}]',
    files={
        "metadata": ("meta.tar.xz", open("meta.tar.xz", "rb"), "application/octet-stream"),
        "rootfs": ("rootfs.squashfs", open("rootfs.squashfs", "rb"), "application/octet-stream"),
    },
)
```

## Writing new patches

Add a new `.py` file in this directory with:

- `apply()` — applies the patch
- `revert()` — reverts to the original behavior
- `_original` — captured at module import time (not in `apply()`)

`apply_all()` auto-discovers all modules in this package and calls `apply()`
on each one. No manual registration needed.
