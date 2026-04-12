# pyincusd.WarningsApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**warning_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/WarningsApi.md#warning_delete) | **DELETE** /1.0/warnings/{uuid} | Delete the warning
[**warning_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/WarningsApi.md#warning_get) | **GET** /1.0/warnings/{uuid} | Get the warning
[**warning_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/WarningsApi.md#warning_patch) | **PATCH** /1.0/warnings/{uuid} | Partially update the warning
[**warning_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/WarningsApi.md#warning_put) | **PUT** /1.0/warnings/{uuid} | Update the warning
[**warnings_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/WarningsApi.md#warnings_get) | **GET** /1.0/warnings | List the warnings
[**warnings_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/WarningsApi.md#warnings_get_recursion1) | **GET** /1.0/warnings?recursion&#x3D;1 | Get the warnings


# **warning_delete**
> ServerPut200Response warning_delete(uuid)

Delete the warning

Removes the warning.

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
    api_instance = pyincusd.WarningsApi(api_client)
    uuid = 'uuid_example' # str | Path parameter: uuid

    try:
        # Delete the warning
        api_response = await api_instance.warning_delete(uuid)
        print("The response of WarningsApi->warning_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarningsApi->warning_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Path parameter: uuid | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warning_get**
> WarningGet200Response warning_get(uuid)

Get the warning

Gets a specific warning.

### Example


```python
import pyincusd
from pyincusd.models.warning_get200_response import WarningGet200Response
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
    api_instance = pyincusd.WarningsApi(api_client)
    uuid = 'uuid_example' # str | Path parameter: uuid

    try:
        # Get the warning
        api_response = await api_instance.warning_get(uuid)
        print("The response of WarningsApi->warning_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarningsApi->warning_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Path parameter: uuid | 

### Return type

[**WarningGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/WarningGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Warning |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warning_patch**
> ServerPut200Response warning_patch(uuid, warning)

Partially update the warning

Updates a subset of the warning status.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.warning_put import WarningPut
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
    api_instance = pyincusd.WarningsApi(api_client)
    uuid = 'uuid_example' # str | Path parameter: uuid
    warning = pyincusd.WarningPut() # WarningPut | Warning status

    try:
        # Partially update the warning
        api_response = await api_instance.warning_patch(uuid, warning)
        print("The response of WarningsApi->warning_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarningsApi->warning_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Path parameter: uuid | 
 **warning** | [**WarningPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/WarningPut.md)| Warning status | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/ServerPut200Response.md)

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

# **warning_put**
> ServerPut200Response warning_put(uuid, warning)

Update the warning

Updates the warning status.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.warning_put import WarningPut
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
    api_instance = pyincusd.WarningsApi(api_client)
    uuid = 'uuid_example' # str | Path parameter: uuid
    warning = pyincusd.WarningPut() # WarningPut | Warning status

    try:
        # Update the warning
        api_response = await api_instance.warning_put(uuid, warning)
        print("The response of WarningsApi->warning_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarningsApi->warning_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Path parameter: uuid | 
 **warning** | [**WarningPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/WarningPut.md)| Warning status | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/ServerPut200Response.md)

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

# **warnings_get**
> WarningsGet200Response warnings_get(project=project)

List the warnings

Returns a list of warnings.

### Example


```python
import pyincusd
from pyincusd.models.warnings_get200_response import WarningsGet200Response
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
    api_instance = pyincusd.WarningsApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # List the warnings
        api_response = await api_instance.warnings_get(project=project)
        print("The response of WarningsApi->warnings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarningsApi->warnings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**WarningsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/WarningsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sync response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warnings_get_recursion1**
> WarningsGetRecursion1200Response warnings_get_recursion1(project=project)

Get the warnings

Returns a list of warnings (structs).

### Example


```python
import pyincusd
from pyincusd.models.warnings_get_recursion1200_response import WarningsGetRecursion1200Response
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
    api_instance = pyincusd.WarningsApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the warnings
        api_response = await api_instance.warnings_get_recursion1(project=project)
        print("The response of WarningsApi->warnings_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarningsApi->warnings_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**WarningsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/WarningsGetRecursion1200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

