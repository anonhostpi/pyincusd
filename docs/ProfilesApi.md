# pyincusd.ProfilesApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilesApi.md#profile_delete) | **DELETE** /1.0/profiles/{name} | Delete the profile
[**profile_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilesApi.md#profile_get) | **GET** /1.0/profiles/{name} | Get the profile
[**profile_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilesApi.md#profile_patch) | **PATCH** /1.0/profiles/{name} | Partially update the profile
[**profile_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilesApi.md#profile_post) | **POST** /1.0/profiles/{name} | Rename the profile
[**profile_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilesApi.md#profile_put) | **PUT** /1.0/profiles/{name} | Update the profile
[**profiles_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilesApi.md#profiles_get) | **GET** /1.0/profiles | Get the profiles
[**profiles_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilesApi.md#profiles_get_recursion1) | **GET** /1.0/profiles?recursion&#x3D;1 | Get the profiles
[**profiles_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilesApi.md#profiles_post) | **POST** /1.0/profiles | Add a profile


# **profile_delete**
> ServerPut200Response profile_delete(project=project)

Delete the profile

Removes the profile.

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
    api_instance = pyincusd.ProfilesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the profile
        api_response = await api_instance.profile_delete(project=project)
        print("The response of ProfilesApi->profile_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->profile_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ServerPut200Response.md)

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

# **profile_get**
> ProfileGet200Response profile_get(project=project)

Get the profile

Gets a specific profile.

### Example


```python
import pyincusd
from pyincusd.models.profile_get200_response import ProfileGet200Response
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
    api_instance = pyincusd.ProfilesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the profile
        api_response = await api_instance.profile_get(project=project)
        print("The response of ProfilesApi->profile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->profile_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ProfileGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfileGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profile |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_patch**
> ServerPut200Response profile_patch(profile, project=project)

Partially update the profile

Updates a subset of the profile configuration.

### Example


```python
import pyincusd
from pyincusd.models.profile_put import ProfilePut
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
    api_instance = pyincusd.ProfilesApi(api_client)
    profile = pyincusd.ProfilePut() # ProfilePut | Profile configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Partially update the profile
        api_response = await api_instance.profile_patch(profile, project=project)
        print("The response of ProfilesApi->profile_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->profile_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**ProfilePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilePut.md)| Profile configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ServerPut200Response.md)

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

# **profile_post**
> ServerPut200Response profile_post(profile, project=project)

Rename the profile

Renames an existing profile.

### Example


```python
import pyincusd
from pyincusd.models.profile_post import ProfilePost
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
    api_instance = pyincusd.ProfilesApi(api_client)
    profile = pyincusd.ProfilePost() # ProfilePost | Profile rename request
    project = 'project_example' # str | Project name (optional)

    try:
        # Rename the profile
        api_response = await api_instance.profile_post(profile, project=project)
        print("The response of ProfilesApi->profile_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->profile_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**ProfilePost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilePost.md)| Profile rename request | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ServerPut200Response.md)

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

# **profile_put**
> ServerPut200Response profile_put(profile, project=project)

Update the profile

Updates the entire profile configuration.

### Example


```python
import pyincusd
from pyincusd.models.profile_put import ProfilePut
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
    api_instance = pyincusd.ProfilesApi(api_client)
    profile = pyincusd.ProfilePut() # ProfilePut | Profile configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Update the profile
        api_response = await api_instance.profile_put(profile, project=project)
        print("The response of ProfilesApi->profile_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->profile_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**ProfilePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilePut.md)| Profile configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ServerPut200Response.md)

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

# **profiles_get**
> ProfilesGet200Response profiles_get(project=project, all_projects=all_projects, filter=filter)

Get the profiles

Returns a list of profiles (URLs).

### Example


```python
import pyincusd
from pyincusd.models.profiles_get200_response import ProfilesGet200Response
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
    api_instance = pyincusd.ProfilesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve profiles from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the profiles
        api_response = await api_instance.profiles_get(project=project, all_projects=all_projects, filter=filter)
        print("The response of ProfilesApi->profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->profiles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve profiles from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**ProfilesGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilesGet200Response.md)

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

# **profiles_get_recursion1**
> ProfilesGetRecursion1200Response profiles_get_recursion1(project=project, all_projects=all_projects, filter=filter)

Get the profiles

Returns a list of profiles (structs).

### Example


```python
import pyincusd
from pyincusd.models.profiles_get_recursion1200_response import ProfilesGetRecursion1200Response
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
    api_instance = pyincusd.ProfilesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve profiles from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the profiles
        api_response = await api_instance.profiles_get_recursion1(project=project, all_projects=all_projects, filter=filter)
        print("The response of ProfilesApi->profiles_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->profiles_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve profiles from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**ProfilesGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilesGetRecursion1200Response.md)

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

# **profiles_post**
> ServerPut200Response profiles_post(profile, project=project)

Add a profile

Creates a new profile.

### Example


```python
import pyincusd
from pyincusd.models.profiles_post import ProfilesPost
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
    api_instance = pyincusd.ProfilesApi(api_client)
    profile = pyincusd.ProfilesPost() # ProfilesPost | Profile
    project = 'project_example' # str | Project name (optional)

    try:
        # Add a profile
        api_response = await api_instance.profiles_post(profile, project=project)
        print("The response of ProfilesApi->profiles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->profiles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**ProfilesPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ProfilesPost.md)| Profile | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/ServerPut200Response.md)

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

