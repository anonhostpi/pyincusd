# pyincusd.patches

Opt-in fixes for gaps in the auto-generated code.

## Usage

Apply a specific patch:

```python
from pyincusd.patches import metadata_config
metadata_config.apply()
```

Apply all available patches:

```python
from pyincusd.patches import apply_all
apply_all()
```

Revert a patch:

```python
from pyincusd.patches import metadata_config
metadata_config.revert()
```

## Spec preprocessing

`fix_spec.py` is a CI-stage tool (not a runtime patch). It rewrites the
Incus Swagger spec before code generation to fix generator-breaking
issues — missing path parameter declarations and the invalid dual-body
on `POST /1.0/images`. Invoked by the publish workflow, not by
`apply_all()`.

## Writing new patches

Add a new `.py` file in this directory with:

- `apply()` — applies the patch
- `revert()` — reverts to the original behavior
- `_original` — captured at module import time (not in `apply()`)

`apply_all()` auto-discovers all modules in this package and calls `apply()`
on each one. No manual registration needed.
