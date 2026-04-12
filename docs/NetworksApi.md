# pyincusd.NetworksApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksApi.md#network_delete) | **DELETE** /1.0/networks/{name} | Delete the network
[**network_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksApi.md#network_get) | **GET** /1.0/networks/{name} | Get the network
[**network_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksApi.md#network_patch) | **PATCH** /1.0/networks/{name} | Partially update the network
[**network_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksApi.md#network_post) | **POST** /1.0/networks/{name} | Rename the network
[**network_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksApi.md#network_put) | **PUT** /1.0/networks/{name} | Update the network
[**networks_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksApi.md#networks_get) | **GET** /1.0/networks | Get the networks
[**networks_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksApi.md#networks_get_recursion1) | **GET** /1.0/networks?recursion&#x3D;1 | Get the networks
[**networks_leases_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksApi.md#networks_leases_get) | **GET** /1.0/networks/{name}/leases | Get the DHCP leases
[**networks_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksApi.md#networks_post) | **POST** /1.0/networks | Add a network
[**networks_state_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksApi.md#networks_state_get) | **GET** /1.0/networks/{name}/state | Get the network state


# **network_delete**
> ServerPut200Response network_delete(project=project)

Delete the network

Removes the network.

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
    api_instance = pyincusd.NetworksApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the network
        api_response = await api_instance.network_delete(project=project)
        print("The response of NetworksApi->network_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->network_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/ServerPut200Response.md)

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

# **network_get**
> NetworkGet200Response network_get(project=project, target=target)

Get the network

Gets a specific network.

### Example


```python
import pyincusd
from pyincusd.models.network_get200_response import NetworkGet200Response
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
    api_instance = pyincusd.NetworksApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the network
        api_response = await api_instance.network_get(project=project, target=target)
        print("The response of NetworksApi->network_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->network_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**NetworkGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworkGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_patch**
> ServerPut200Response network_patch(network, project=project, target=target)

Partially update the network

Updates a subset of the network configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_put import NetworkPut
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
    api_instance = pyincusd.NetworksApi(api_client)
    network = pyincusd.NetworkPut() # NetworkPut | Network configuration
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Partially update the network
        api_response = await api_instance.network_patch(network, project=project, target=target)
        print("The response of NetworksApi->network_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->network_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | [**NetworkPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworkPut.md)| Network configuration | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/ServerPut200Response.md)

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

# **network_post**
> ServerPut200Response network_post(network, project=project)

Rename the network

Renames an existing network.

### Example


```python
import pyincusd
from pyincusd.models.network_post import NetworkPost
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
    api_instance = pyincusd.NetworksApi(api_client)
    network = pyincusd.NetworkPost() # NetworkPost | Network rename request
    project = 'project_example' # str | Project name (optional)

    try:
        # Rename the network
        api_response = await api_instance.network_post(network, project=project)
        print("The response of NetworksApi->network_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->network_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | [**NetworkPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworkPost.md)| Network rename request | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/ServerPut200Response.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_put**
> ServerPut200Response network_put(network, project=project, target=target)

Update the network

Updates the entire network configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_put import NetworkPut
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
    api_instance = pyincusd.NetworksApi(api_client)
    network = pyincusd.NetworkPut() # NetworkPut | Network configuration
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Update the network
        api_response = await api_instance.network_put(network, project=project, target=target)
        print("The response of NetworksApi->network_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->network_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | [**NetworkPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworkPut.md)| Network configuration | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/ServerPut200Response.md)

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

# **networks_get**
> NetworksGet200Response networks_get(project=project, all_projects=all_projects, filter=filter)

Get the networks

Returns a list of networks (URLs).

### Example


```python
import pyincusd
from pyincusd.models.networks_get200_response import NetworksGet200Response
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
    api_instance = pyincusd.NetworksApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve networks from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the networks
        api_response = await api_instance.networks_get(project=project, all_projects=all_projects, filter=filter)
        print("The response of NetworksApi->networks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->networks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve networks from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworksGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksGet200Response.md)

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

# **networks_get_recursion1**
> NetworksGetRecursion1200Response networks_get_recursion1(project=project, all_projects=all_projects, filter=filter)

Get the networks

Returns a list of networks (structs).

### Example


```python
import pyincusd
from pyincusd.models.networks_get_recursion1200_response import NetworksGetRecursion1200Response
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
    api_instance = pyincusd.NetworksApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve networks from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the networks
        api_response = await api_instance.networks_get_recursion1(project=project, all_projects=all_projects, filter=filter)
        print("The response of NetworksApi->networks_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->networks_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve networks from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworksGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksGetRecursion1200Response.md)

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

# **networks_leases_get**
> NetworksLeasesGet200Response networks_leases_get(project=project, target=target)

Get the DHCP leases

Returns a list of DHCP leases for the network.

### Example


```python
import pyincusd
from pyincusd.models.networks_leases_get200_response import NetworksLeasesGet200Response
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
    api_instance = pyincusd.NetworksApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the DHCP leases
        api_response = await api_instance.networks_leases_get(project=project, target=target)
        print("The response of NetworksApi->networks_leases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->networks_leases_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**NetworksLeasesGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksLeasesGet200Response.md)

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

# **networks_post**
> ServerPut200Response networks_post(network, project=project, target=target)

Add a network

Creates a new network.
When clustered, most network types require individual POST for each cluster member prior to a global POST.

### Example


```python
import pyincusd
from pyincusd.models.networks_post import NetworksPost
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
    api_instance = pyincusd.NetworksApi(api_client)
    network = pyincusd.NetworksPost() # NetworksPost | Network
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Add a network
        api_response = await api_instance.networks_post(network, project=project, target=target)
        print("The response of NetworksApi->networks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->networks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | [**NetworksPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksPost.md)| Network | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/ServerPut200Response.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **networks_state_get**
> NetworksStateGet200Response networks_state_get(project=project, target=target)

Get the network state

Returns the current network state information.

### Example


```python
import pyincusd
from pyincusd.models.networks_state_get200_response import NetworksStateGet200Response
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
    api_instance = pyincusd.NetworksApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the network state
        api_response = await api_instance.networks_state_get(project=project, target=target)
        print("The response of NetworksApi->networks_state_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksApi->networks_state_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**NetworksStateGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworksStateGet200Response.md)

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

