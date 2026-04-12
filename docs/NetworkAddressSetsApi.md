# pyincusd.NetworkAddressSetsApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_address_set_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetsApi.md#network_address_set_delete) | **DELETE** /1.0/network-address-sets/{name} | Delete the network address set
[**network_address_set_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetsApi.md#network_address_set_get) | **GET** /1.0/network-address-sets/{name} | Get the network address set
[**network_address_set_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetsApi.md#network_address_set_patch) | **PATCH** /1.0/network-address-sets/{name} | Partially update the network address set
[**network_address_set_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetsApi.md#network_address_set_post) | **POST** /1.0/network-address-sets/{name} | Rename the network address set
[**network_address_set_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetsApi.md#network_address_set_put) | **PUT** /1.0/network-address-sets/{name} | Update the network address set
[**network_address_sets_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetsApi.md#network_address_sets_get) | **GET** /1.0/network-address-sets | Get the network address sets
[**network_address_sets_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetsApi.md#network_address_sets_get_recursion1) | **GET** /1.0/network-address-sets?recursion&#x3D;1 | Get the network address sets
[**network_address_sets_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetsApi.md#network_address_sets_post) | **POST** /1.0/network-address-sets | Add a network address set


# **network_address_set_delete**
> ServerPut200Response network_address_set_delete(project=project)

Delete the network address set

Removes the network address set.

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
    api_instance = pyincusd.NetworkAddressSetsApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the network address set
        api_response = await api_instance.network_address_set_delete(project=project)
        print("The response of NetworkAddressSetsApi->network_address_set_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAddressSetsApi->network_address_set_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ServerPut200Response.md)

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

# **network_address_set_get**
> NetworkAddressSetGet200Response network_address_set_get(project=project)

Get the network address set

Gets a specific network address set.

### Example


```python
import pyincusd
from pyincusd.models.network_address_set_get200_response import NetworkAddressSetGet200Response
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
    api_instance = pyincusd.NetworkAddressSetsApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the network address set
        api_response = await api_instance.network_address_set_get(project=project)
        print("The response of NetworkAddressSetsApi->network_address_set_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAddressSetsApi->network_address_set_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**NetworkAddressSetGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | address set |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_address_set_patch**
> ServerPut200Response network_address_set_patch(address_set, project=project)

Partially update the network address set

Updates a subset of the network address set configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_address_set_put import NetworkAddressSetPut
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
    api_instance = pyincusd.NetworkAddressSetsApi(api_client)
    address_set = pyincusd.NetworkAddressSetPut() # NetworkAddressSetPut | Address set configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Partially update the network address set
        api_response = await api_instance.network_address_set_patch(address_set, project=project)
        print("The response of NetworkAddressSetsApi->network_address_set_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAddressSetsApi->network_address_set_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_set** | [**NetworkAddressSetPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetPut.md)| Address set configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ServerPut200Response.md)

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

# **network_address_set_post**
> ServerPut200Response network_address_set_post(address_set, project=project)

Rename the network address set

Renames an existing network address set.

### Example


```python
import pyincusd
from pyincusd.models.network_address_set_post import NetworkAddressSetPost
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
    api_instance = pyincusd.NetworkAddressSetsApi(api_client)
    address_set = pyincusd.NetworkAddressSetPost() # NetworkAddressSetPost | Address set rename request
    project = 'project_example' # str | Project name (optional)

    try:
        # Rename the network address set
        api_response = await api_instance.network_address_set_post(address_set, project=project)
        print("The response of NetworkAddressSetsApi->network_address_set_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAddressSetsApi->network_address_set_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_set** | [**NetworkAddressSetPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetPost.md)| Address set rename request | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ServerPut200Response.md)

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

# **network_address_set_put**
> ServerPut200Response network_address_set_put(address_set, project=project)

Update the network address set

Updates the entire network address set configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_address_set_put import NetworkAddressSetPut
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
    api_instance = pyincusd.NetworkAddressSetsApi(api_client)
    address_set = pyincusd.NetworkAddressSetPut() # NetworkAddressSetPut | Address set configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Update the network address set
        api_response = await api_instance.network_address_set_put(address_set, project=project)
        print("The response of NetworkAddressSetsApi->network_address_set_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAddressSetsApi->network_address_set_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_set** | [**NetworkAddressSetPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetPut.md)| Address set configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ServerPut200Response.md)

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

# **network_address_sets_get**
> NetworkAddressSetsGet200Response network_address_sets_get(project=project, all_projects=all_projects, filter=filter)

Get the network address sets

Returns a list of network address sets (URLs).

### Example


```python
import pyincusd
from pyincusd.models.network_address_sets_get200_response import NetworkAddressSetsGet200Response
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
    api_instance = pyincusd.NetworkAddressSetsApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve network address sets from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network address sets
        api_response = await api_instance.network_address_sets_get(project=project, all_projects=all_projects, filter=filter)
        print("The response of NetworkAddressSetsApi->network_address_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAddressSetsApi->network_address_sets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve network address sets from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkAddressSetsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetsGet200Response.md)

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

# **network_address_sets_get_recursion1**
> NetworkAddressSetsGetRecursion1200Response network_address_sets_get_recursion1(project=project, all_projects=all_projects, filter=filter)

Get the network address sets

Returns a list of network address sets (structs).

### Example


```python
import pyincusd
from pyincusd.models.network_address_sets_get_recursion1200_response import NetworkAddressSetsGetRecursion1200Response
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
    api_instance = pyincusd.NetworkAddressSetsApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve network address sets from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network address sets
        api_response = await api_instance.network_address_sets_get_recursion1(project=project, all_projects=all_projects, filter=filter)
        print("The response of NetworkAddressSetsApi->network_address_sets_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAddressSetsApi->network_address_sets_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve network address sets from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkAddressSetsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetsGetRecursion1200Response.md)

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

# **network_address_sets_post**
> ServerPut200Response network_address_sets_post(address_set, project=project)

Add a network address set

Creates a new network address set.

### Example


```python
import pyincusd
from pyincusd.models.network_address_sets_post import NetworkAddressSetsPost
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
    api_instance = pyincusd.NetworkAddressSetsApi(api_client)
    address_set = pyincusd.NetworkAddressSetsPost() # NetworkAddressSetsPost | address set
    project = 'project_example' # str | Project name (optional)

    try:
        # Add a network address set
        api_response = await api_instance.network_address_sets_post(address_set, project=project)
        print("The response of NetworkAddressSetsApi->network_address_sets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAddressSetsApi->network_address_sets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_set** | [**NetworkAddressSetsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkAddressSetsPost.md)| address set | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ServerPut200Response.md)

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

