# pyincusd.NetworkLoadBalancersApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_load_balancer_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancersApi.md#network_load_balancer_delete) | **DELETE** /1.0/networks/{networkName}/load-balancers/{listenAddress} | Delete the network address load balancer
[**network_load_balancer_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancersApi.md#network_load_balancer_get) | **GET** /1.0/networks/{networkName}/load-balancers/{listenAddress} | Get the network address load balancer
[**network_load_balancer_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancersApi.md#network_load_balancer_get_recursion1) | **GET** /1.0/networks/{networkName}/load-balancers?recursion&#x3D;1 | Get the network address load balancers
[**network_load_balancer_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancersApi.md#network_load_balancer_patch) | **PATCH** /1.0/networks/{networkName}/load-balancers/{listenAddress} | Partially update the network address load balancer
[**network_load_balancer_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancersApi.md#network_load_balancer_put) | **PUT** /1.0/networks/{networkName}/load-balancers/{listenAddress} | Update the network address load balancer
[**network_load_balancer_state_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancersApi.md#network_load_balancer_state_get) | **GET** /1.0/networks/{networkName}/load-balancers/{listenAddress}/state | Get the network address load balancer state
[**network_load_balancers_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancersApi.md#network_load_balancers_get) | **GET** /1.0/networks/{networkName}/load-balancers | Get the network address of load balancers
[**network_load_balancers_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancersApi.md#network_load_balancers_post) | **POST** /1.0/networks/{networkName}/load-balancers | Add a network load balancer


# **network_load_balancer_delete**
> ServerPut200Response network_load_balancer_delete(network_name, listen_address, project=project)

Delete the network address load balancer

Removes the network address load balancer.

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
    api_instance = pyincusd.NetworkLoadBalancersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    listen_address = 'listen_address_example' # str | Path parameter: listenAddress
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the network address load balancer
        api_response = await api_instance.network_load_balancer_delete(network_name, listen_address, project=project)
        print("The response of NetworkLoadBalancersApi->network_load_balancer_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLoadBalancersApi->network_load_balancer_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **listen_address** | **str**| Path parameter: listenAddress | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ServerPut200Response.md)

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

# **network_load_balancer_get**
> NetworkLoadBalancerGet200Response network_load_balancer_get(network_name, listen_address, project=project)

Get the network address load balancer

Gets a specific network address load balancer.

### Example


```python
import pyincusd
from pyincusd.models.network_load_balancer_get200_response import NetworkLoadBalancerGet200Response
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
    api_instance = pyincusd.NetworkLoadBalancersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    listen_address = 'listen_address_example' # str | Path parameter: listenAddress
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the network address load balancer
        api_response = await api_instance.network_load_balancer_get(network_name, listen_address, project=project)
        print("The response of NetworkLoadBalancersApi->network_load_balancer_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLoadBalancersApi->network_load_balancer_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **listen_address** | **str**| Path parameter: listenAddress | 
 **project** | **str**| Project name | [optional] 

### Return type

[**NetworkLoadBalancerGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancerGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Load Balancer |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_load_balancer_get_recursion1**
> NetworkLoadBalancerGetRecursion1200Response network_load_balancer_get_recursion1(network_name, project=project, filter=filter)

Get the network address load balancers

Returns a list of network address load balancers (structs).

### Example


```python
import pyincusd
from pyincusd.models.network_load_balancer_get_recursion1200_response import NetworkLoadBalancerGetRecursion1200Response
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
    api_instance = pyincusd.NetworkLoadBalancersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network address load balancers
        api_response = await api_instance.network_load_balancer_get_recursion1(network_name, project=project, filter=filter)
        print("The response of NetworkLoadBalancersApi->network_load_balancer_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLoadBalancersApi->network_load_balancer_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkLoadBalancerGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancerGetRecursion1200Response.md)

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

# **network_load_balancer_patch**
> ServerPut200Response network_load_balancer_patch(network_name, listen_address, load_balancer, project=project)

Partially update the network address load balancer

Updates a subset of the network address load balancer configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_load_balancer_put import NetworkLoadBalancerPut
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
    api_instance = pyincusd.NetworkLoadBalancersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    listen_address = 'listen_address_example' # str | Path parameter: listenAddress
    load_balancer = pyincusd.NetworkLoadBalancerPut() # NetworkLoadBalancerPut | Address load balancer configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Partially update the network address load balancer
        api_response = await api_instance.network_load_balancer_patch(network_name, listen_address, load_balancer, project=project)
        print("The response of NetworkLoadBalancersApi->network_load_balancer_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLoadBalancersApi->network_load_balancer_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **listen_address** | **str**| Path parameter: listenAddress | 
 **load_balancer** | [**NetworkLoadBalancerPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancerPut.md)| Address load balancer configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ServerPut200Response.md)

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

# **network_load_balancer_put**
> ServerPut200Response network_load_balancer_put(network_name, listen_address, load_balancer, project=project)

Update the network address load balancer

Updates the entire network address load balancer configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_load_balancer_put import NetworkLoadBalancerPut
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
    api_instance = pyincusd.NetworkLoadBalancersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    listen_address = 'listen_address_example' # str | Path parameter: listenAddress
    load_balancer = pyincusd.NetworkLoadBalancerPut() # NetworkLoadBalancerPut | Address load balancer configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Update the network address load balancer
        api_response = await api_instance.network_load_balancer_put(network_name, listen_address, load_balancer, project=project)
        print("The response of NetworkLoadBalancersApi->network_load_balancer_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLoadBalancersApi->network_load_balancer_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **listen_address** | **str**| Path parameter: listenAddress | 
 **load_balancer** | [**NetworkLoadBalancerPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancerPut.md)| Address load balancer configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ServerPut200Response.md)

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

# **network_load_balancer_state_get**
> NetworkLoadBalancerStateGet200Response network_load_balancer_state_get(network_name, listen_address, project=project)

Get the network address load balancer state

Get the current state of a specific network address load balancer.

### Example


```python
import pyincusd
from pyincusd.models.network_load_balancer_state_get200_response import NetworkLoadBalancerStateGet200Response
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
    api_instance = pyincusd.NetworkLoadBalancersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    listen_address = 'listen_address_example' # str | Path parameter: listenAddress
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the network address load balancer state
        api_response = await api_instance.network_load_balancer_state_get(network_name, listen_address, project=project)
        print("The response of NetworkLoadBalancersApi->network_load_balancer_state_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLoadBalancersApi->network_load_balancer_state_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **listen_address** | **str**| Path parameter: listenAddress | 
 **project** | **str**| Project name | [optional] 

### Return type

[**NetworkLoadBalancerStateGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancerStateGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Load Balancer state |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_load_balancers_get**
> NetworkLoadBalancersGet200Response network_load_balancers_get(network_name, project=project, filter=filter)

Get the network address of load balancers

Returns a list of network address load balancers (URLs).

### Example


```python
import pyincusd
from pyincusd.models.network_load_balancers_get200_response import NetworkLoadBalancersGet200Response
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
    api_instance = pyincusd.NetworkLoadBalancersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network address of load balancers
        api_response = await api_instance.network_load_balancers_get(network_name, project=project, filter=filter)
        print("The response of NetworkLoadBalancersApi->network_load_balancers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLoadBalancersApi->network_load_balancers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkLoadBalancersGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancersGet200Response.md)

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

# **network_load_balancers_post**
> ServerPut200Response network_load_balancers_post(network_name, load_balancer, project=project)

Add a network load balancer

Creates a new network load balancer.

### Example


```python
import pyincusd
from pyincusd.models.network_load_balancers_post import NetworkLoadBalancersPost
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
    api_instance = pyincusd.NetworkLoadBalancersApi(api_client)
    network_name = 'network_name_example' # str | Path parameter: networkName
    load_balancer = pyincusd.NetworkLoadBalancersPost() # NetworkLoadBalancersPost | Load Balancer
    project = 'project_example' # str | Project name (optional)

    try:
        # Add a network load balancer
        api_response = await api_instance.network_load_balancers_post(network_name, load_balancer, project=project)
        print("The response of NetworkLoadBalancersApi->network_load_balancers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLoadBalancersApi->network_load_balancers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Path parameter: networkName | 
 **load_balancer** | [**NetworkLoadBalancersPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancersPost.md)| Load Balancer | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ServerPut200Response.md)

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

