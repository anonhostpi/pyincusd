

## Local Unix Socket Client

Connect to incusd without manual configuration:

```python
from pyincusd.local import Client
from pyincusd.api import instances_api

c = Client()
result = c.run(instances_api.InstancesApi(c).instances_get())
print(result.metadata)
```

`Client` extends `ApiClient` with the Unix socket transport preconfigured.
`Client.run()` wraps async API calls for synchronous use. Supports `with` blocks.

Custom socket path: `Client(socket_path="/custom/path.socket")`

## Patches

Opt-in fixes for gaps in the auto-generated code. See [patches/README.md](patches/README.md) for details.

Apply all patches:

```python
from pyincusd.patches import apply_all
apply_all()
```

Apply individually:

```python
from pyincusd.patches import metadata_config
metadata_config.apply()
metadata_config.revert()  # undo
```

New patches are auto-discovered — drop a `.py` with `apply()`/`revert()` in `patches/` and `apply_all()` picks it up.

## High-Level Client

For an OOP abstraction layer built on pyincusd, see [incusd-client](https://github.com/anonhostpi/incusd-client) — provides classes like `Instance`, `StoragePool`, `Network`, `Cluster` with full coverage of the Incus REST API.
