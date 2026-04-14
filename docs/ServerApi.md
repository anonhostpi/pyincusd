# pyincusd.ServerApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerApi.md#api_get) | **GET** / | Get the supported API endpoints
[**events_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerApi.md#events_get) | **GET** /1.0/events | Get the event stream
[**resources_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerApi.md#resources_get) | **GET** /1.0/resources | Get system resources information
[**server_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerApi.md#server_get) | **GET** /1.0 | Get the server environment and configuration
[**server_get_untrusted**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerApi.md#server_get_untrusted) | **GET** /1.0?public | Get the server environment
[**server_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerApi.md#server_patch) | **PATCH** /1.0 | Partially update the server configuration
[**server_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerApi.md#server_put) | **PUT** /1.0 | Update the server configuration


# **api_get**
> ApiGet200Response api_get()

Get the supported API endpoints

Returns a list of supported API versions (URLs).

Internal API endpoints are not reported as those aren't versioned
and should only be used by the daemon itself.

### Example


```python
import pyincusd
from pyincusd.models.api_get200_response import ApiGet200Response
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
    api_instance = pyincusd.ServerApi(api_client)

    try:
        # Get the supported API endpoints
        api_response = await api_instance.api_get()
        print("The response of ServerApi->api_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->api_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ApiGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_get**
> Event events_get(project=project, type=type, all_projects=all_projects)

Get the event stream

Connects to the event API using websocket.

### Example


```python
import pyincusd
from pyincusd.models.event import Event
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
    api_instance = pyincusd.ServerApi(api_client)
    project = 'project_example' # str | Project name (optional)
    type = 'type_example' # str | Event type(s), comma separated (valid types are logging, operation or lifecycle) (optional)
    all_projects = True # bool | Retrieve instances from all projects (optional)

    try:
        # Get the event stream
        api_response = await api_instance.events_get(project=project, type=type, all_projects=all_projects)
        print("The response of ServerApi->events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **type** | **str**| Event type(s), comma separated (valid types are logging, operation or lifecycle) | [optional] 
 **all_projects** | **bool**| Retrieve instances from all projects | [optional] 

### Return type

[**Event**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Websocket message (JSON) |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_get**
> ResourcesGet200Response resources_get(target=target)

Get system resources information

Gets the hardware information profile of the server.

### Example


```python
import pyincusd
from pyincusd.models.resources_get200_response import ResourcesGet200Response
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
    api_instance = pyincusd.ServerApi(api_client)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get system resources information
        api_response = await api_instance.resources_get(target=target)
        print("The response of ServerApi->resources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->resources_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ResourcesGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ResourcesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hardware resources |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_get**
> ServerGet200Response server_get(target=target, project=project)

Get the server environment and configuration

Shows the full server environment and configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_get200_response import ServerGet200Response
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
    api_instance = pyincusd.ServerApi(api_client)
    target = 'target_example' # str | Cluster member name (optional)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the server environment and configuration
        api_response = await api_instance.server_get(target=target, project=project)
        print("The response of ServerApi->server_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->server_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Cluster member name | [optional] 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server environment and configuration |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_get_untrusted**
> ServerGetUntrusted200Response server_get_untrusted()

Get the server environment

Shows a small subset of the server environment and configuration
which is required by untrusted clients to reach a server.

The `?public` part of the URL isn't required, it's simply used to
separate the two behaviors of this endpoint.

### Example


```python
import pyincusd
from pyincusd.models.server_get_untrusted200_response import ServerGetUntrusted200Response
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
    api_instance = pyincusd.ServerApi(api_client)

    try:
        # Get the server environment
        api_response = await api_instance.server_get_untrusted()
        print("The response of ServerApi->server_get_untrusted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->server_get_untrusted: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServerGetUntrusted200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerGetUntrusted200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server environment and configuration |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_patch**
> ServerPut200Response server_patch(server, target=target)

Partially update the server configuration

Updates a subset of the server configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_put import ServerPut
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
    api_instance = pyincusd.ServerApi(api_client)
    server = pyincusd.ServerPut() # ServerPut | Server configuration
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Partially update the server configuration
        api_response = await api_instance.server_patch(server, target=target)
        print("The response of ServerApi->server_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->server_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | [**ServerPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerPut.md)| Server configuration | 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerPut200Response.md)

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

# **server_put**
> ServerPut200Response server_put(server, target=target)

Update the server configuration

Updates the entire server configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_put import ServerPut
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
    api_instance = pyincusd.ServerApi(api_client)
    server = pyincusd.ServerPut() # ServerPut | Server configuration
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Update the server configuration
        api_response = await api_instance.server_put(server, target=target)
        print("The response of ServerApi->server_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->server_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | [**ServerPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerPut.md)| Server configuration | 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ServerPut200Response.md)

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

