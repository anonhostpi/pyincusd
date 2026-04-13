# pyincusd.ProjectsApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_access**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsApi.md#project_access) | **GET** /1.0/projects/{name}/access | Get who has access to a project
[**project_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsApi.md#project_delete) | **DELETE** /1.0/projects/{name} | Delete the project
[**project_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsApi.md#project_get) | **GET** /1.0/projects/{name} | Get the project
[**project_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsApi.md#project_patch) | **PATCH** /1.0/projects/{name} | Partially update the project
[**project_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsApi.md#project_post) | **POST** /1.0/projects/{name} | Rename the project
[**project_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsApi.md#project_put) | **PUT** /1.0/projects/{name} | Update the project
[**project_state_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsApi.md#project_state_get) | **GET** /1.0/projects/{name}/state | Get the project state
[**projects_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsApi.md#projects_get) | **GET** /1.0/projects | Get the projects
[**projects_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsApi.md#projects_get_recursion1) | **GET** /1.0/projects?recursion&#x3D;1 | Get the projects
[**projects_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsApi.md#projects_post) | **POST** /1.0/projects | Add a project


# **project_access**
> InstanceAccess200Response project_access(name)

Get who has access to a project

Gets the access information for the project.

### Example


```python
import pyincusd
from pyincusd.models.instance_access200_response import InstanceAccess200Response
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
    api_instance = pyincusd.ProjectsApi(api_client)
    name = 'name_example' # str | Path parameter: name

    try:
        # Get who has access to a project
        api_response = await api_instance.project_access(name)
        print("The response of ProjectsApi->project_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 

### Return type

[**InstanceAccess200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/InstanceAccess200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_delete**
> ServerPut200Response project_delete(name, force=force)

Delete the project

Removes the project.

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
    api_instance = pyincusd.ProjectsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    force = True # bool | Delete project and related artifacts (optional)

    try:
        # Delete the project
        api_response = await api_instance.project_delete(name, force=force)
        print("The response of ProjectsApi->project_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **force** | **bool**| Delete project and related artifacts | [optional] 

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

# **project_get**
> ProjectGet200Response project_get(name)

Get the project

Gets a specific project.

### Example


```python
import pyincusd
from pyincusd.models.project_get200_response import ProjectGet200Response
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
    api_instance = pyincusd.ProjectsApi(api_client)
    name = 'name_example' # str | Path parameter: name

    try:
        # Get the project
        api_response = await api_instance.project_get(name)
        print("The response of ProjectsApi->project_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 

### Return type

[**ProjectGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_patch**
> ServerPut200Response project_patch(name, project)

Partially update the project

Updates a subset of the project configuration.

### Example


```python
import pyincusd
from pyincusd.models.project_put import ProjectPut
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
    api_instance = pyincusd.ProjectsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    project = pyincusd.ProjectPut() # ProjectPut | Project configuration

    try:
        # Partially update the project
        api_response = await api_instance.project_patch(name, project)
        print("The response of ProjectsApi->project_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **project** | [**ProjectPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectPut.md)| Project configuration | 

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

# **project_post**
> ClusterMembersPost202Response project_post(name, project)

Rename the project

Renames an existing project.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.project_post import ProjectPost
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
    api_instance = pyincusd.ProjectsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    project = pyincusd.ProjectPost() # ProjectPost | Project rename request

    try:
        # Rename the project
        api_response = await api_instance.project_post(name, project)
        print("The response of ProjectsApi->project_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **project** | [**ProjectPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectPost.md)| Project rename request | 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ClusterMembersPost202Response.md)

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

# **project_put**
> ServerPut200Response project_put(name, project)

Update the project

Updates the entire project configuration.

### Example


```python
import pyincusd
from pyincusd.models.project_put import ProjectPut
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
    api_instance = pyincusd.ProjectsApi(api_client)
    name = 'name_example' # str | Path parameter: name
    project = pyincusd.ProjectPut() # ProjectPut | Project configuration

    try:
        # Update the project
        api_response = await api_instance.project_put(name, project)
        print("The response of ProjectsApi->project_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **project** | [**ProjectPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectPut.md)| Project configuration | 

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

# **project_state_get**
> ProjectStateGet200Response project_state_get(name)

Get the project state

Gets a specific project resource consumption information.

### Example


```python
import pyincusd
from pyincusd.models.project_state_get200_response import ProjectStateGet200Response
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
    api_instance = pyincusd.ProjectsApi(api_client)
    name = 'name_example' # str | Path parameter: name

    try:
        # Get the project state
        api_response = await api_instance.project_state_get(name)
        print("The response of ProjectsApi->project_state_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_state_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 

### Return type

[**ProjectStateGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectStateGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project state |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get**
> ProjectsGet200Response projects_get(filter=filter)

Get the projects

Returns a list of projects (URLs).

### Example


```python
import pyincusd
from pyincusd.models.projects_get200_response import ProjectsGet200Response
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
    api_instance = pyincusd.ProjectsApi(api_client)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the projects
        api_response = await api_instance.projects_get(filter=filter)
        print("The response of ProjectsApi->projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**ProjectsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsGet200Response.md)

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

# **projects_get_recursion1**
> ProjectsGetRecursion1200Response projects_get_recursion1(filter=filter)

Get the projects

Returns a list of projects (structs).

### Example


```python
import pyincusd
from pyincusd.models.projects_get_recursion1200_response import ProjectsGetRecursion1200Response
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
    api_instance = pyincusd.ProjectsApi(api_client)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the projects
        api_response = await api_instance.projects_get_recursion1(filter=filter)
        print("The response of ProjectsApi->projects_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**ProjectsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsGetRecursion1200Response.md)

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

# **projects_post**
> ServerPut200Response projects_post(project)

Add a project

Creates a new project.

### Example


```python
import pyincusd
from pyincusd.models.projects_post import ProjectsPost
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
    api_instance = pyincusd.ProjectsApi(api_client)
    project = pyincusd.ProjectsPost() # ProjectsPost | Project

    try:
        # Add a project
        api_response = await api_instance.projects_post(project)
        print("The response of ProjectsApi->projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**ProjectsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsPost.md)| Project | 

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

