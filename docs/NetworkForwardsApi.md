# pyincusd.NetworkForwardsApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_forward_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardsApi.md#network_forward_delete) | **DELETE** /1.0/networks/{networkName}/forwards/{listenAddress} | Delete the network address forward
[**network_forward_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardsApi.md#network_forward_get) | **GET** /1.0/networks/{networkName}/forwards/{listenAddress} | Get the network address forward
[**network_forward_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardsApi.md#network_forward_get_recursion1) | **GET** /1.0/networks/{networkName}/forwards?recursion&#x3D;1 | Get the network address forwards
[**network_forward_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardsApi.md#network_forward_patch) | **PATCH** /1.0/networks/{networkName}/forwards/{listenAddress} | Partially update the network address forward
[**network_forward_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardsApi.md#network_forward_put) | **PUT** /1.0/networks/{networkName}/forwards/{listenAddress} | Update the network address forward
[**network_forwards_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardsApi.md#network_forwards_get) | **GET** /1.0/networks/{networkName}/forwards | Get the network address forwards
[**network_forwards_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardsApi.md#network_forwards_post) | **POST** /1.0/networks/{networkName}/forwards | Add a network address forward


# **network_forward_delete**
> ServerPut200Response network_forward_delete(project=project)

Delete the network address forward

Removes the network address forward.

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
    api_instance = pyincusd.NetworkForwardsApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the network address forward
        api_response = await api_instance.network_forward_delete(project=project)
        print("The response of NetworkForwardsApi->network_forward_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkForwardsApi->network_forward_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/ServerPut200Response.md)

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

# **network_forward_get**
> NetworkForwardGet200Response network_forward_get(project=project)

Get the network address forward

Gets a specific network address forward.

### Example


```python
import pyincusd
from pyincusd.models.network_forward_get200_response import NetworkForwardGet200Response
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
    api_instance = pyincusd.NetworkForwardsApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the network address forward
        api_response = await api_instance.network_forward_get(project=project)
        print("The response of NetworkForwardsApi->network_forward_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkForwardsApi->network_forward_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**NetworkForwardGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Address forward |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_forward_get_recursion1**
> NetworkForwardGetRecursion1200Response network_forward_get_recursion1(project=project, filter=filter)

Get the network address forwards

Returns a list of network address forwards (structs).

### Example


```python
import pyincusd
from pyincusd.models.network_forward_get_recursion1200_response import NetworkForwardGetRecursion1200Response
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
    api_instance = pyincusd.NetworkForwardsApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network address forwards
        api_response = await api_instance.network_forward_get_recursion1(project=project, filter=filter)
        print("The response of NetworkForwardsApi->network_forward_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkForwardsApi->network_forward_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkForwardGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardGetRecursion1200Response.md)

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

# **network_forward_patch**
> ServerPut200Response network_forward_patch(forward, project=project)

Partially update the network address forward

Updates a subset of the network address forward configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_forward_put import NetworkForwardPut
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
    api_instance = pyincusd.NetworkForwardsApi(api_client)
    forward = pyincusd.NetworkForwardPut() # NetworkForwardPut | Address forward configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Partially update the network address forward
        api_response = await api_instance.network_forward_patch(forward, project=project)
        print("The response of NetworkForwardsApi->network_forward_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkForwardsApi->network_forward_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward** | [**NetworkForwardPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardPut.md)| Address forward configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/ServerPut200Response.md)

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

# **network_forward_put**
> ServerPut200Response network_forward_put(forward, project=project)

Update the network address forward

Updates the entire network address forward configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_forward_put import NetworkForwardPut
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
    api_instance = pyincusd.NetworkForwardsApi(api_client)
    forward = pyincusd.NetworkForwardPut() # NetworkForwardPut | Address forward configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Update the network address forward
        api_response = await api_instance.network_forward_put(forward, project=project)
        print("The response of NetworkForwardsApi->network_forward_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkForwardsApi->network_forward_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward** | [**NetworkForwardPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardPut.md)| Address forward configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/ServerPut200Response.md)

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

# **network_forwards_get**
> NetworkForwardsGet200Response network_forwards_get(project=project, filter=filter)

Get the network address forwards

Returns a list of network address forwards (URLs).

### Example


```python
import pyincusd
from pyincusd.models.network_forwards_get200_response import NetworkForwardsGet200Response
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
    api_instance = pyincusd.NetworkForwardsApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network address forwards
        api_response = await api_instance.network_forwards_get(project=project, filter=filter)
        print("The response of NetworkForwardsApi->network_forwards_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkForwardsApi->network_forwards_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkForwardsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardsGet200Response.md)

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

# **network_forwards_post**
> ServerPut200Response network_forwards_post(forward, project=project)

Add a network address forward

Creates a new network address forward.

### Example


```python
import pyincusd
from pyincusd.models.network_forwards_post import NetworkForwardsPost
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
    api_instance = pyincusd.NetworkForwardsApi(api_client)
    forward = pyincusd.NetworkForwardsPost() # NetworkForwardsPost | Forward
    project = 'project_example' # str | Project name (optional)

    try:
        # Add a network address forward
        api_response = await api_instance.network_forwards_post(forward, project=project)
        print("The response of NetworkForwardsApi->network_forwards_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkForwardsApi->network_forwards_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward** | [**NetworkForwardsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/NetworkForwardsPost.md)| Forward | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/ServerPut200Response.md)

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

