# pyincusd.NetworkAclsApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_acl_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclsApi.md#network_acl_delete) | **DELETE** /1.0/network-acls/{name} | Delete the network ACL
[**network_acl_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclsApi.md#network_acl_get) | **GET** /1.0/network-acls/{name} | Get the network ACL
[**network_acl_log_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclsApi.md#network_acl_log_get) | **GET** /1.0/network-acls/{name}/log | Get the network ACL log
[**network_acl_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclsApi.md#network_acl_patch) | **PATCH** /1.0/network-acls/{name} | Partially update the network ACL
[**network_acl_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclsApi.md#network_acl_post) | **POST** /1.0/network-acls/{name} | Rename the network ACL
[**network_acl_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclsApi.md#network_acl_put) | **PUT** /1.0/network-acls/{name} | Update the network ACL
[**network_acls_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclsApi.md#network_acls_get) | **GET** /1.0/network-acls | Get the network ACLs
[**network_acls_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclsApi.md#network_acls_get_recursion1) | **GET** /1.0/network-acls?recursion&#x3D;1 | Get the network ACLs
[**network_acls_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclsApi.md#network_acls_post) | **POST** /1.0/network-acls | Add a network ACL


# **network_acl_delete**
> ServerPut200Response network_acl_delete(name, project=project)

Delete the network ACL

Removes the network ACL.

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
    api_instance = pyincusd.NetworkAclsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the network ACL
        api_response = await api_instance.network_acl_delete(name, project=project)
        print("The response of NetworkAclsApi->network_acl_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAclsApi->network_acl_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/ServerPut200Response.md)

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

# **network_acl_get**
> NetworkAclGet200Response network_acl_get(name, project=project)

Get the network ACL

Gets a specific network ACL.

### Example


```python
import pyincusd
from pyincusd.models.network_acl_get200_response import NetworkAclGet200Response
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
    api_instance = pyincusd.NetworkAclsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the network ACL
        api_response = await api_instance.network_acl_get(name, project=project)
        print("The response of NetworkAclsApi->network_acl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAclsApi->network_acl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **project** | **str**| Project name | [optional] 

### Return type

[**NetworkAclGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ACL |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_acl_log_get**
> network_acl_log_get(name, project=project)

Get the network ACL log

Gets a specific network ACL log entries.

### Example


```python
import pyincusd
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
    api_instance = pyincusd.NetworkAclsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the network ACL log
        await api_instance.network_acl_log_get(name, project=project)
    except Exception as e:
        print("Exception when calling NetworkAclsApi->network_acl_log_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **project** | **str**| Project name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw log file |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_acl_patch**
> ServerPut200Response network_acl_patch(name, acl, project=project)

Partially update the network ACL

Updates a subset of the network ACL configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_acl_put import NetworkACLPut
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
    api_instance = pyincusd.NetworkAclsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    acl = pyincusd.NetworkACLPut() # NetworkACLPut | ACL configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Partially update the network ACL
        api_response = await api_instance.network_acl_patch(name, acl, project=project)
        print("The response of NetworkAclsApi->network_acl_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAclsApi->network_acl_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **acl** | [**NetworkACLPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkACLPut.md)| ACL configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/ServerPut200Response.md)

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

# **network_acl_post**
> ServerPut200Response network_acl_post(name, acl, project=project)

Rename the network ACL

Renames an existing network ACL.

### Example


```python
import pyincusd
from pyincusd.models.network_acl_post import NetworkACLPost
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
    api_instance = pyincusd.NetworkAclsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    acl = pyincusd.NetworkACLPost() # NetworkACLPost | ACL rename request
    project = 'project_example' # str | Project name (optional)

    try:
        # Rename the network ACL
        api_response = await api_instance.network_acl_post(name, acl, project=project)
        print("The response of NetworkAclsApi->network_acl_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAclsApi->network_acl_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **acl** | [**NetworkACLPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkACLPost.md)| ACL rename request | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/ServerPut200Response.md)

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

# **network_acl_put**
> ServerPut200Response network_acl_put(name, acl, project=project)

Update the network ACL

Updates the entire network ACL configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_acl_put import NetworkACLPut
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
    api_instance = pyincusd.NetworkAclsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    acl = pyincusd.NetworkACLPut() # NetworkACLPut | ACL configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Update the network ACL
        api_response = await api_instance.network_acl_put(name, acl, project=project)
        print("The response of NetworkAclsApi->network_acl_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAclsApi->network_acl_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **acl** | [**NetworkACLPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkACLPut.md)| ACL configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/ServerPut200Response.md)

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

# **network_acls_get**
> NetworkAclsGet200Response network_acls_get(project=project, all_projects=all_projects, filter=filter)

Get the network ACLs

Returns a list of network ACLs (URLs).

### Example


```python
import pyincusd
from pyincusd.models.network_acls_get200_response import NetworkAclsGet200Response
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
    api_instance = pyincusd.NetworkAclsApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve network ACLs from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network ACLs
        api_response = await api_instance.network_acls_get(project=project, all_projects=all_projects, filter=filter)
        print("The response of NetworkAclsApi->network_acls_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAclsApi->network_acls_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve network ACLs from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkAclsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclsGet200Response.md)

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

# **network_acls_get_recursion1**
> NetworkAclsGetRecursion1200Response network_acls_get_recursion1(project=project, all_projects=all_projects, filter=filter)

Get the network ACLs

Returns a list of network ACLs (structs).

### Example


```python
import pyincusd
from pyincusd.models.network_acls_get_recursion1200_response import NetworkAclsGetRecursion1200Response
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
    api_instance = pyincusd.NetworkAclsApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve network ACLs from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network ACLs
        api_response = await api_instance.network_acls_get_recursion1(project=project, all_projects=all_projects, filter=filter)
        print("The response of NetworkAclsApi->network_acls_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAclsApi->network_acls_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve network ACLs from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkAclsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkAclsGetRecursion1200Response.md)

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

# **network_acls_post**
> ServerPut200Response network_acls_post(acl, project=project)

Add a network ACL

Creates a new network ACL.

### Example


```python
import pyincusd
from pyincusd.models.network_acls_post import NetworkACLsPost
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
    api_instance = pyincusd.NetworkAclsApi(api_client)
    acl = pyincusd.NetworkACLsPost() # NetworkACLsPost | ACL
    project = 'project_example' # str | Project name (optional)

    try:
        # Add a network ACL
        api_response = await api_instance.network_acls_post(acl, project=project)
        print("The response of NetworkAclsApi->network_acls_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAclsApi->network_acls_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl** | [**NetworkACLsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/NetworkACLsPost.md)| ACL | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/ServerPut200Response.md)

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

