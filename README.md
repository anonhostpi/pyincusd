# pyincusd

[![PyPI version](https://img.shields.io/pypi/v/pyincusd)](https://pypi.org/project/pyincusd/)
[![Incus version](https://img.shields.io/badge/incus-6.23.0-blue)](https://github.com/lxc/incus/releases/tag/v6.23.0)

Auto-generated Python client for the [Incus](https://linuxcontainers.org/incus/) daemon REST API.

**Latest: 6.23.0** — generated from [`lxc/incus@v6.23.0`](https://github.com/lxc/incus/tree/v6.23.0)

## Install

```bash
pip install pyincusd
```

## Usage

```python
import pyincusd
from pyincusd.api import instances_api

config = pyincusd.Configuration()
config.host = "http+unix://%2Frun%2Fincus%2Funix.socket"

with pyincusd.ApiClient(config) as client:
    api = instances_api.InstancesApi(client)
    instances = api.instances_get()
```

## How it works

A [GitHub Actions workflow](.github/workflows/publish.yaml) runs every night:
1. Checks the latest [lxc/incus](https://github.com/lxc/incus/releases) release
2. Compares against what's on PyPI
3. If new: generates a typed Python client via [OpenAPI Generator](https://openapi-generator.tech/), publishes to PyPI

## PyPI trusted publishing setup

First publish requires configuring [trusted publishing](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/):
1. Go to https://pypi.org/manage/account/publishing/
2. Add pending publisher: owner=`anonhostpi`, repo=`pyincusd`, workflow=`publish.yaml`, environment=`pypi`
