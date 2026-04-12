# pyincusd.OperationsApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**operation_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationsApi.md#operation_delete) | **DELETE** /1.0/operations/{id} | Cancel the operation
[**operation_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationsApi.md#operation_get) | **GET** /1.0/operations/{id} | Get the operation state
[**operation_wait_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationsApi.md#operation_wait_get) | **GET** /1.0/operations/{id}/wait | Wait for the operation
[**operation_wait_get_untrusted**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationsApi.md#operation_wait_get_untrusted) | **GET** /1.0/operations/{id}/wait?public | Wait for the operation
[**operation_websocket_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationsApi.md#operation_websocket_get) | **GET** /1.0/operations/{id}/websocket | Get the websocket stream
[**operation_websocket_get_untrusted**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationsApi.md#operation_websocket_get_untrusted) | **GET** /1.0/operations/{id}/websocket?public | Get the websocket stream
[**operations_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationsApi.md#operations_get) | **GET** /1.0/operations | Get the operations
[**operations_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationsApi.md#operations_get_recursion1) | **GET** /1.0/operations?recursion&#x3D;1 | Get the operations


# **operation_delete**
> ServerPut200Response operation_delete()

Cancel the operation

Cancels the operation if supported.

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
    api_instance = pyincusd.OperationsApi(api_client)

    try:
        # Cancel the operation
        api_response = await api_instance.operation_delete()
        print("The response of OperationsApi->operation_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->operation_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **operation_get**
> OperationGet200Response operation_get()

Get the operation state

Gets the operation state.

### Example


```python
import pyincusd
from pyincusd.models.operation_get200_response import OperationGet200Response
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
    api_instance = pyincusd.OperationsApi(api_client)

    try:
        # Get the operation state
        api_response = await api_instance.operation_get()
        print("The response of OperationsApi->operation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->operation_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OperationGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operation_wait_get**
> OperationGet200Response operation_wait_get(timeout=timeout)

Wait for the operation

Waits for the operation to reach a final state (or timeout) and retrieve its final state.

### Example


```python
import pyincusd
from pyincusd.models.operation_get200_response import OperationGet200Response
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
    api_instance = pyincusd.OperationsApi(api_client)
    timeout = 56 # int | Timeout in seconds (-1 means never) (optional)

    try:
        # Wait for the operation
        api_response = await api_instance.operation_wait_get(timeout=timeout)
        print("The response of OperationsApi->operation_wait_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->operation_wait_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds (-1 means never) | [optional] 

### Return type

[**OperationGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operation_wait_get_untrusted**
> OperationGet200Response operation_wait_get_untrusted(secret=secret, timeout=timeout)

Wait for the operation

Waits for the operation to reach a final state (or timeout) and retrieve its final state.

When accessed by an untrusted user, the secret token must be provided.

### Example


```python
import pyincusd
from pyincusd.models.operation_get200_response import OperationGet200Response
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
    api_instance = pyincusd.OperationsApi(api_client)
    secret = 'secret_example' # str | Authentication token (optional)
    timeout = 56 # int | Timeout in seconds (-1 means never) (optional)

    try:
        # Wait for the operation
        api_response = await api_instance.operation_wait_get_untrusted(secret=secret, timeout=timeout)
        print("The response of OperationsApi->operation_wait_get_untrusted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->operation_wait_get_untrusted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret** | **str**| Authentication token | [optional] 
 **timeout** | **int**| Timeout in seconds (-1 means never) | [optional] 

### Return type

[**OperationGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operation_websocket_get**
> operation_websocket_get(secret=secret)

Get the websocket stream

Connects to an associated websocket stream for the operation.
This should almost never be done directly by a client, instead it's
meant for server to server communication with the client only relaying the
connection information to the servers.

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
    api_instance = pyincusd.OperationsApi(api_client)
    secret = 'secret_example' # str | Authentication token (optional)

    try:
        # Get the websocket stream
        await api_instance.operation_websocket_get(secret=secret)
    except Exception as e:
        print("Exception when calling OperationsApi->operation_websocket_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret** | **str**| Authentication token | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Websocket operation messages (dependent on operation) |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operation_websocket_get_untrusted**
> operation_websocket_get_untrusted(secret=secret)

Get the websocket stream

Connects to an associated websocket stream for the operation.
This should almost never be done directly by a client, instead it's
meant for server to server communication with the client only relaying the
connection information to the servers.

The untrusted endpoint is used by the target server to connect to the source server.
Authentication is performed through the secret token.

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
    api_instance = pyincusd.OperationsApi(api_client)
    secret = 'secret_example' # str | Authentication token (optional)

    try:
        # Get the websocket stream
        await api_instance.operation_websocket_get_untrusted(secret=secret)
    except Exception as e:
        print("Exception when calling OperationsApi->operation_websocket_get_untrusted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret** | **str**| Authentication token | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Websocket operation messages (dependent on operation) |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get**
> OperationsGet200Response operations_get(project=project, all_projects=all_projects)

Get the operations

Returns a JSON object of operation type to operation list (URLs).

### Example


```python
import pyincusd
from pyincusd.models.operations_get200_response import OperationsGet200Response
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
    api_instance = pyincusd.OperationsApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve operations from all projects (optional)

    try:
        # Get the operations
        api_response = await api_instance.operations_get(project=project, all_projects=all_projects)
        print("The response of OperationsApi->operations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->operations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve operations from all projects | [optional] 

### Return type

[**OperationsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationsGet200Response.md)

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

# **operations_get_recursion1**
> OperationsGetRecursion1200Response operations_get_recursion1(project=project, all_projects=all_projects)

Get the operations

Returns a list of operations (structs).

### Example


```python
import pyincusd
from pyincusd.models.operations_get_recursion1200_response import OperationsGetRecursion1200Response
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
    api_instance = pyincusd.OperationsApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve operations from all projects (optional)

    try:
        # Get the operations
        api_response = await api_instance.operations_get_recursion1(project=project, all_projects=all_projects)
        print("The response of OperationsApi->operations_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->operations_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve operations from all projects | [optional] 

### Return type

[**OperationsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/OperationsGetRecursion1200Response.md)

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

