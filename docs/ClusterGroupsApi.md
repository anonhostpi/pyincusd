# pyincusd.ClusterGroupsApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_group_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupsApi.md#cluster_group_delete) | **DELETE** /1.0/cluster/groups/{name} | Delete the cluster group.
[**cluster_group_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupsApi.md#cluster_group_get) | **GET** /1.0/cluster/groups/{name} | Get the cluster group
[**cluster_group_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupsApi.md#cluster_group_patch) | **PATCH** /1.0/cluster/groups/{name} | Update the cluster group
[**cluster_group_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupsApi.md#cluster_group_post) | **POST** /1.0/cluster/groups/{name} | Rename the cluster group
[**cluster_group_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupsApi.md#cluster_group_put) | **PUT** /1.0/cluster/groups/{name} | Update the cluster group
[**cluster_groups_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupsApi.md#cluster_groups_get) | **GET** /1.0/cluster/groups | Get the cluster groups
[**cluster_groups_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupsApi.md#cluster_groups_get_recursion1) | **GET** /1.0/cluster/groups?recursion&#x3D;1 | Get the cluster groups


# **cluster_group_delete**
> ServerPut200Response cluster_group_delete(name)

Delete the cluster group.

Removes the cluster group.

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
    api_instance = pyincusd.ClusterGroupsApi(api_client)
    name = 'name_example' # str | Path parameter: name

    try:
        # Delete the cluster group.
        api_response = await api_instance.cluster_group_delete(name)
        print("The response of ClusterGroupsApi->cluster_group_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterGroupsApi->cluster_group_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ServerPut200Response.md)

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

# **cluster_group_get**
> ClusterGroupGet200Response cluster_group_get(name)

Get the cluster group

Gets a specific cluster group.

### Example


```python
import pyincusd
from pyincusd.models.cluster_group_get200_response import ClusterGroupGet200Response
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
    api_instance = pyincusd.ClusterGroupsApi(api_client)
    name = 'name_example' # str | Path parameter: name

    try:
        # Get the cluster group
        api_response = await api_instance.cluster_group_get(name)
        print("The response of ClusterGroupsApi->cluster_group_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterGroupsApi->cluster_group_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 

### Return type

[**ClusterGroupGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster group |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_group_patch**
> ServerPut200Response cluster_group_patch(name, cluster_group)

Update the cluster group

Updates the cluster group configuration.

### Example


```python
import pyincusd
from pyincusd.models.cluster_group_put import ClusterGroupPut
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
    api_instance = pyincusd.ClusterGroupsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    cluster_group = pyincusd.ClusterGroupPut() # ClusterGroupPut | cluster group configuration

    try:
        # Update the cluster group
        api_response = await api_instance.cluster_group_patch(name, cluster_group)
        print("The response of ClusterGroupsApi->cluster_group_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterGroupsApi->cluster_group_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **cluster_group** | [**ClusterGroupPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupPut.md)| cluster group configuration | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ServerPut200Response.md)

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

# **cluster_group_post**
> ServerPut200Response cluster_group_post(name, name2)

Rename the cluster group

Renames an existing cluster group.

### Example


```python
import pyincusd
from pyincusd.models.cluster_group_post import ClusterGroupPost
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
    api_instance = pyincusd.ClusterGroupsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    name2 = pyincusd.ClusterGroupPost() # ClusterGroupPost | Cluster group rename request

    try:
        # Rename the cluster group
        api_response = await api_instance.cluster_group_post(name, name2)
        print("The response of ClusterGroupsApi->cluster_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterGroupsApi->cluster_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **name2** | [**ClusterGroupPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupPost.md)| Cluster group rename request | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ServerPut200Response.md)

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

# **cluster_group_put**
> ServerPut200Response cluster_group_put(name, cluster_group)

Update the cluster group

Updates the entire cluster group configuration.

### Example


```python
import pyincusd
from pyincusd.models.cluster_group_put import ClusterGroupPut
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
    api_instance = pyincusd.ClusterGroupsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    cluster_group = pyincusd.ClusterGroupPut() # ClusterGroupPut | cluster group configuration

    try:
        # Update the cluster group
        api_response = await api_instance.cluster_group_put(name, cluster_group)
        print("The response of ClusterGroupsApi->cluster_group_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterGroupsApi->cluster_group_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **cluster_group** | [**ClusterGroupPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupPut.md)| cluster group configuration | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ServerPut200Response.md)

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

# **cluster_groups_get**
> ClusterGroupsGet200Response cluster_groups_get()

Get the cluster groups

Returns a list of cluster groups (URLs).

### Example


```python
import pyincusd
from pyincusd.models.cluster_groups_get200_response import ClusterGroupsGet200Response
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
    api_instance = pyincusd.ClusterGroupsApi(api_client)

    try:
        # Get the cluster groups
        api_response = await api_instance.cluster_groups_get()
        print("The response of ClusterGroupsApi->cluster_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterGroupsApi->cluster_groups_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterGroupsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupsGet200Response.md)

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

# **cluster_groups_get_recursion1**
> ClusterGroupsGetRecursion1200Response cluster_groups_get_recursion1()

Get the cluster groups

Returns a list of cluster groups (structs).

### Example


```python
import pyincusd
from pyincusd.models.cluster_groups_get_recursion1200_response import ClusterGroupsGetRecursion1200Response
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
    api_instance = pyincusd.ClusterGroupsApi(api_client)

    try:
        # Get the cluster groups
        api_response = await api_instance.cluster_groups_get_recursion1()
        print("The response of ClusterGroupsApi->cluster_groups_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterGroupsApi->cluster_groups_get_recursion1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterGroupsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ClusterGroupsGetRecursion1200Response.md)

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

