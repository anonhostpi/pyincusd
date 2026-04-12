# pyincusd

Auto-generated Python client for the [Incus](https://linuxcontainers.org/incus/) daemon REST API.

Published to [PyPI](https://pypi.org/project/pyincusd/) nightly whenever a new Incus release is detected.

## How it works

A [GitHub Actions workflow](.github/workflows/publish.yaml) runs every night:

1. **Check**: queries the latest [lxc/incus](https://github.com/lxc/incus/releases) release and compares against what's currently on PyPI
2. **Build** (only if new release): fetches the Swagger spec for that release, generates a typed Python client via [OpenAPI Generator](https://openapi-generator.tech/), builds a wheel
3. **Publish**: pushes to PyPI via [trusted publishing](https://docs.pypi.org/trusted-publishers/) (no API token)

## Install

```bash
pip install pyincusd
```

## PyPI setup required

For the first publish to work, configure [PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/):

1. Go to https://pypi.org/manage/account/publishing/
2. Add a new pending publisher:
   - **PyPI project name**: `pyincusd`
   - **Owner**: `anonhostpi`
   - **Repository**: `pyincusd`
   - **Workflow name**: `publish.yaml`
   - **Environment**: `pypi`
