"""Connect to incusd via Unix socket.

Usage:
    from pyincusd.local import Client
    from pyincusd.api import instances_api

    c = Client()
    api = instances_api.InstancesApi(c)
    result = c.run(api.instances_get())
    print(result.metadata)
"""

from __future__ import annotations
import asyncio
import httpx
import pyincusd

DEFAULT_SOCKET = "/run/incus/unix.socket"


class Client(pyincusd.ApiClient):
    """ApiClient preconfigured for the local incusd Unix socket."""

    def __init__(self, socket_path: str = DEFAULT_SOCKET, **kwargs):
        config = pyincusd.Configuration()
        config.host = "http://localhost"
        config.verify_ssl = False
        super().__init__(config, **kwargs)
        self._socket_path = socket_path
        self.rest_client._create_pool_manager = self._uds_pool

    def _uds_pool(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(
            transport=httpx.AsyncHTTPTransport(uds=self._socket_path),
            verify=False,
            trust_env=True,
        )

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    @staticmethod
    def run(coro):
        """Run an async API call synchronously."""
        return asyncio.run(coro)
