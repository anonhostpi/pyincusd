# pyincusd.ClusterApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_get) | **GET** /1.0/cluster | Get the cluster configuration
[**cluster_groups_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_groups_post) | **POST** /1.0/cluster/groups | Create a cluster group.
[**cluster_member_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_member_delete) | **DELETE** /1.0/cluster/members/{name} | Delete the cluster member
[**cluster_member_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_member_get) | **GET** /1.0/cluster/members/{name} | Get the cluster member
[**cluster_member_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_member_patch) | **PATCH** /1.0/cluster/members/{name} | Partially update the cluster member
[**cluster_member_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_member_post) | **POST** /1.0/cluster/members/{name} | Rename the cluster member
[**cluster_member_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_member_put) | **PUT** /1.0/cluster/members/{name} | Update the cluster member
[**cluster_member_state_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_member_state_get) | **GET** /1.0/cluster/members/{name}/state | Get state of the cluster member
[**cluster_member_state_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_member_state_post) | **POST** /1.0/cluster/members/{name}/state | Evacuate or restore a cluster member
[**cluster_members_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_members_get) | **GET** /1.0/cluster/members | Get the cluster members
[**cluster_members_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_members_get_recursion1) | **GET** /1.0/cluster/members?recursion&#x3D;1 | Get the cluster members
[**cluster_members_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_members_post) | **POST** /1.0/cluster/members | Request a join token
[**cluster_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#cluster_put) | **PUT** /1.0/cluster | Update the cluster configuration
[**clustering_update_cert**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterApi.md#clustering_update_cert) | **PUT** /1.0/cluster/certificate | Update the certificate for the cluster


# **cluster_get**
> ClusterGet200Response cluster_get()

Get the cluster configuration

Gets the current cluster configuration.

### Example


```python
import pyincusd
from pyincusd.models.cluster_get200_response import ClusterGet200Response
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
    api_instance = pyincusd.ClusterApi(api_client)

    try:
        # Get the cluster configuration
        api_response = await api_instance.cluster_get()
        print("The response of ClusterApi->cluster_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster configuration |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_groups_post**
> ServerPut200Response cluster_groups_post(cluster)

Create a cluster group.

Creates a new cluster group.

### Example


```python
import pyincusd
from pyincusd.models.cluster_groups_post import ClusterGroupsPost
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
    api_instance = pyincusd.ClusterApi(api_client)
    cluster = pyincusd.ClusterGroupsPost() # ClusterGroupsPost | Cluster group to create

    try:
        # Create a cluster group.
        api_response = await api_instance.cluster_groups_post(cluster)
        print("The response of ClusterApi->cluster_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | [**ClusterGroupsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterGroupsPost.md)| Cluster group to create | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ServerPut200Response.md)

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

# **cluster_member_delete**
> ServerPut200Response cluster_member_delete(name)

Delete the cluster member

Removes the member from the cluster.

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
    api_instance = pyincusd.ClusterApi(api_client)
    name = 'name_example' # str | Path parameter: name

    try:
        # Delete the cluster member
        api_response = await api_instance.cluster_member_delete(name)
        print("The response of ClusterApi->cluster_member_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_member_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ServerPut200Response.md)

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

# **cluster_member_get**
> ClusterMemberGet200Response cluster_member_get(name)

Get the cluster member

Gets a specific cluster member.

### Example


```python
import pyincusd
from pyincusd.models.cluster_member_get200_response import ClusterMemberGet200Response
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
    api_instance = pyincusd.ClusterApi(api_client)
    name = 'name_example' # str | Path parameter: name

    try:
        # Get the cluster member
        api_response = await api_instance.cluster_member_get(name)
        print("The response of ClusterApi->cluster_member_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_member_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 

### Return type

[**ClusterMemberGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterMemberGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster member |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_member_patch**
> ServerPut200Response cluster_member_patch(name, cluster)

Partially update the cluster member

Updates a subset of the cluster member configuration.

### Example


```python
import pyincusd
from pyincusd.models.cluster_member_put import ClusterMemberPut
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
    api_instance = pyincusd.ClusterApi(api_client)
    name = 'name_example' # str | Path parameter: name
    cluster = pyincusd.ClusterMemberPut() # ClusterMemberPut | Cluster member configuration

    try:
        # Partially update the cluster member
        api_response = await api_instance.cluster_member_patch(name, cluster)
        print("The response of ClusterApi->cluster_member_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_member_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **cluster** | [**ClusterMemberPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterMemberPut.md)| Cluster member configuration | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ServerPut200Response.md)

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

# **cluster_member_post**
> ServerPut200Response cluster_member_post(name, cluster)

Rename the cluster member

Renames an existing cluster member.

### Example


```python
import pyincusd
from pyincusd.models.cluster_member_post import ClusterMemberPost
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
    api_instance = pyincusd.ClusterApi(api_client)
    name = 'name_example' # str | Path parameter: name
    cluster = pyincusd.ClusterMemberPost() # ClusterMemberPost | Cluster member rename request

    try:
        # Rename the cluster member
        api_response = await api_instance.cluster_member_post(name, cluster)
        print("The response of ClusterApi->cluster_member_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_member_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **cluster** | [**ClusterMemberPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterMemberPost.md)| Cluster member rename request | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ServerPut200Response.md)

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

# **cluster_member_put**
> ServerPut200Response cluster_member_put(name, cluster)

Update the cluster member

Updates the entire cluster member configuration.

### Example


```python
import pyincusd
from pyincusd.models.cluster_member_put import ClusterMemberPut
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
    api_instance = pyincusd.ClusterApi(api_client)
    name = 'name_example' # str | Path parameter: name
    cluster = pyincusd.ClusterMemberPut() # ClusterMemberPut | Cluster member configuration

    try:
        # Update the cluster member
        api_response = await api_instance.cluster_member_put(name, cluster)
        print("The response of ClusterApi->cluster_member_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_member_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **cluster** | [**ClusterMemberPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterMemberPut.md)| Cluster member configuration | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ServerPut200Response.md)

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

# **cluster_member_state_get**
> ClusterMemberStateGet200Response cluster_member_state_get(name)

Get state of the cluster member

Gets state of a specific cluster member.

### Example


```python
import pyincusd
from pyincusd.models.cluster_member_state_get200_response import ClusterMemberStateGet200Response
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
    api_instance = pyincusd.ClusterApi(api_client)
    name = 'name_example' # str | Path parameter: name

    try:
        # Get state of the cluster member
        api_response = await api_instance.cluster_member_state_get(name)
        print("The response of ClusterApi->cluster_member_state_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_member_state_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 

### Return type

[**ClusterMemberStateGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterMemberStateGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster member state |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_member_state_post**
> ClusterMembersPost202Response cluster_member_state_post(name, cluster)

Evacuate or restore a cluster member

Evacuates or restores a cluster member.

### Example


```python
import pyincusd
from pyincusd.models.cluster_member_state_post import ClusterMemberStatePost
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
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
    api_instance = pyincusd.ClusterApi(api_client)
    name = 'name_example' # str | Path parameter: name
    cluster = pyincusd.ClusterMemberStatePost() # ClusterMemberStatePost | Cluster member state

    try:
        # Evacuate or restore a cluster member
        api_response = await api_instance.cluster_member_state_post(name, cluster)
        print("The response of ClusterApi->cluster_member_state_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_member_state_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **cluster** | [**ClusterMemberStatePost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterMemberStatePost.md)| Cluster member state | 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_members_get**
> ClusterMembersGet200Response cluster_members_get(filter=filter)

Get the cluster members

Returns a list of cluster members (URLs).

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_get200_response import ClusterMembersGet200Response
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
    api_instance = pyincusd.ClusterApi(api_client)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the cluster members
        api_response = await api_instance.cluster_members_get(filter=filter)
        print("The response of ClusterApi->cluster_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_members_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**ClusterMembersGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterMembersGet200Response.md)

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

# **cluster_members_get_recursion1**
> ClusterMembersGetRecursion1200Response cluster_members_get_recursion1(filter=filter)

Get the cluster members

Returns a list of cluster members (structs).

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_get_recursion1200_response import ClusterMembersGetRecursion1200Response
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
    api_instance = pyincusd.ClusterApi(api_client)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the cluster members
        api_response = await api_instance.cluster_members_get_recursion1(filter=filter)
        print("The response of ClusterApi->cluster_members_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_members_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**ClusterMembersGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterMembersGetRecursion1200Response.md)

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

# **cluster_members_post**
> ClusterMembersPost202Response cluster_members_post(cluster)

Request a join token

Requests a join token to add a cluster member.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post import ClusterMembersPost
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
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
    api_instance = pyincusd.ClusterApi(api_client)
    cluster = pyincusd.ClusterMembersPost() # ClusterMembersPost | Cluster member add request

    try:
        # Request a join token
        api_response = await api_instance.cluster_members_post(cluster)
        print("The response of ClusterApi->cluster_members_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_members_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | [**ClusterMembersPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterMembersPost.md)| Cluster member add request | 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_put**
> ServerPut200Response cluster_put(cluster)

Update the cluster configuration

Updates the entire cluster configuration.

### Example


```python
import pyincusd
from pyincusd.models.cluster_put import ClusterPut
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
    api_instance = pyincusd.ClusterApi(api_client)
    cluster = pyincusd.ClusterPut() # ClusterPut | Cluster configuration

    try:
        # Update the cluster configuration
        api_response = await api_instance.cluster_put(cluster)
        print("The response of ClusterApi->cluster_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | [**ClusterPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterPut.md)| Cluster configuration | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ServerPut200Response.md)

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

# **clustering_update_cert**
> ServerPut200Response clustering_update_cert(cluster)

Update the certificate for the cluster

Replaces existing cluster certificate and reloads each cluster member.

### Example


```python
import pyincusd
from pyincusd.models.cluster_certificate_put import ClusterCertificatePut
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
    api_instance = pyincusd.ClusterApi(api_client)
    cluster = pyincusd.ClusterCertificatePut() # ClusterCertificatePut | Cluster certificate replace request

    try:
        # Update the certificate for the cluster
        api_response = await api_instance.clustering_update_cert(cluster)
        print("The response of ClusterApi->clustering_update_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->clustering_update_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | [**ClusterCertificatePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ClusterCertificatePut.md)| Cluster certificate replace request | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/ServerPut200Response.md)

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

