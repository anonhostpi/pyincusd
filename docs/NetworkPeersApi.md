# pyincusd.NetworkPeersApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_peer_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeersApi.md#network_peer_delete) | **DELETE** /1.0/networks/{networkName}/peers/{peerName} | Delete the network peer
[**network_peer_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeersApi.md#network_peer_get) | **GET** /1.0/networks/{networkName}/peers/{peerName} | Get the network peer
[**network_peer_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeersApi.md#network_peer_get_recursion1) | **GET** /1.0/networks/{networkName}/peers?recursion&#x3D;1 | Get the network peers
[**network_peer_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeersApi.md#network_peer_patch) | **PATCH** /1.0/networks/{networkName}/peers/{peerName} | Partially update the network peer
[**network_peer_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeersApi.md#network_peer_put) | **PUT** /1.0/networks/{networkName}/peers/{peerName} | Update the network peer
[**network_peers_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeersApi.md#network_peers_get) | **GET** /1.0/networks/{networkName}/peers | Get the network peers
[**network_peers_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeersApi.md#network_peers_post) | **POST** /1.0/networks/{networkName}/peers | Add a network peer


# **network_peer_delete**
> ServerPut200Response network_peer_delete(network_name, peer_name, project=project)

Delete the network peer

Removes the network peering.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.NetworkPeersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    peer_name = 'peer_name_example' # str | Path parameter: peerName
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the network peer
        api_response = await api_instance.network_peer_delete(network_name, peer_name, project=project)
        print("The response of NetworkPeersApi->network_peer_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkPeersApi->network_peer_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **peer_name** | **str**| Path parameter: peerName | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_peer_get**
> NetworkPeerGet200Response network_peer_get(network_name, peer_name, project=project)

Get the network peer

Gets a specific network peering.

### Example


```python
import pyincusd
from pyincusd.models.network_peer_get200_response import NetworkPeerGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.NetworkPeersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    peer_name = 'peer_name_example' # str | Path parameter: peerName
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the network peer
        api_response = await api_instance.network_peer_get(network_name, peer_name, project=project)
        print("The response of NetworkPeersApi->network_peer_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkPeersApi->network_peer_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **peer_name** | **str**| Path parameter: peerName | 
 **project** | **str**| Project name | [optional] 

### Return type

[**NetworkPeerGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeerGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Peer |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_peer_get_recursion1**
> NetworkPeerGetRecursion1200Response network_peer_get_recursion1(network_name, project=project, filter=filter)

Get the network peers

Returns a list of network peers (structs).

### Example


```python
import pyincusd
from pyincusd.models.network_peer_get_recursion1200_response import NetworkPeerGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.NetworkPeersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network peers
        api_response = await api_instance.network_peer_get_recursion1(network_name, project=project, filter=filter)
        print("The response of NetworkPeersApi->network_peer_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkPeersApi->network_peer_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkPeerGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeerGetRecursion1200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_peer_patch**
> ServerPut200Response network_peer_patch(network_name, peer_name, peer, project=project)

Partially update the network peer

Updates a subset of the network peering configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_peer_put import NetworkPeerPut
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.NetworkPeersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    peer_name = 'peer_name_example' # str | Path parameter: peerName
    peer = pyincusd.NetworkPeerPut() # NetworkPeerPut | Peer configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Partially update the network peer
        api_response = await api_instance.network_peer_patch(network_name, peer_name, peer, project=project)
        print("The response of NetworkPeersApi->network_peer_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkPeersApi->network_peer_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **peer_name** | **str**| Path parameter: peerName | 
 **peer** | [**NetworkPeerPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeerPut.md)| Peer configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_peer_put**
> ServerPut200Response network_peer_put(network_name, peer_name, peer, project=project)

Update the network peer

Updates the entire network peering configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_peer_put import NetworkPeerPut
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.NetworkPeersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    peer_name = 'peer_name_example' # str | Path parameter: peerName
    peer = pyincusd.NetworkPeerPut() # NetworkPeerPut | Peer configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Update the network peer
        api_response = await api_instance.network_peer_put(network_name, peer_name, peer, project=project)
        print("The response of NetworkPeersApi->network_peer_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkPeersApi->network_peer_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **peer_name** | **str**| Path parameter: peerName | 
 **peer** | [**NetworkPeerPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeerPut.md)| Peer configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_peers_get**
> NetworkPeersGet200Response network_peers_get(network_name, project=project, filter=filter)

Get the network peers

Returns a list of network peers (URLs).

### Example


```python
import pyincusd
from pyincusd.models.network_peers_get200_response import NetworkPeersGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.NetworkPeersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network peers
        api_response = await api_instance.network_peers_get(network_name, project=project, filter=filter)
        print("The response of NetworkPeersApi->network_peers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkPeersApi->network_peers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkPeersGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_peers_post**
> ServerPut200Response network_peers_post(network_name, peer, project=project)

Add a network peer

Initiates/creates a new network peering.

### Example


```python
import pyincusd
from pyincusd.models.network_peers_post import NetworkPeersPost
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.NetworkPeersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    peer = pyincusd.NetworkPeersPost() # NetworkPeersPost | Peer
    project = 'project_example' # str | Project name (optional)

    try:
        # Add a network peer
        api_response = await api_instance.network_peers_post(network_name, peer, project=project)
        print("The response of NetworkPeersApi->network_peers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkPeersApi->network_peers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **peer** | [**NetworkPeersPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkPeersPost.md)| Peer | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**202** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

