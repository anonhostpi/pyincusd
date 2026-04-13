# pyincusd.NetworkIntegrationsApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_integration_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationsApi.md#network_integration_delete) | **DELETE** /1.0/network-integrations/{integration} | Delete the network integration
[**network_integration_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationsApi.md#network_integration_get) | **GET** /1.0/network-integrations/{integration} | Get the network integration
[**network_integration_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationsApi.md#network_integration_patch) | **PATCH** /1.0/network-integrations/{integration} | Partially update the network integration
[**network_integration_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationsApi.md#network_integration_post) | **POST** /1.0/network-integrations/{integration} | Rename the network integration
[**network_integration_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationsApi.md#network_integration_put) | **PUT** /1.0/network-integrations/{integration} | Update the network integration
[**network_integrations_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationsApi.md#network_integrations_get) | **GET** /1.0/network-integrations | Get the network integrations
[**network_integrations_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationsApi.md#network_integrations_get_recursion1) | **GET** /1.0/network-integrations?recursion&#x3D;1 | Get the network integrations
[**network_integrations_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationsApi.md#network_integrations_post) | **POST** /1.0/network-integrations | Add a network integration


# **network_integration_delete**
> ServerPut200Response network_integration_delete(integration)

Delete the network integration

Removes the network integration.

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
    api_instance = pyincusd.NetworkIntegrationsApi(api_client)
    integration = 'integration_example' # str | Path parameter: integration

    try:
        # Delete the network integration
        api_response = await api_instance.network_integration_delete(integration)
        print("The response of NetworkIntegrationsApi->network_integration_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkIntegrationsApi->network_integration_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| Path parameter: integration | 

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

# **network_integration_get**
> NetworkIntegrationGet200Response network_integration_get(integration)

Get the network integration

Gets a specific network integration.

### Example


```python
import pyincusd
from pyincusd.models.network_integration_get200_response import NetworkIntegrationGet200Response
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
    api_instance = pyincusd.NetworkIntegrationsApi(api_client)
    integration = 'integration_example' # str | Path parameter: integration

    try:
        # Get the network integration
        api_response = await api_instance.network_integration_get(integration)
        print("The response of NetworkIntegrationsApi->network_integration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkIntegrationsApi->network_integration_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| Path parameter: integration | 

### Return type

[**NetworkIntegrationGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_integration_patch**
> ServerPut200Response network_integration_patch(integration, integration2)

Partially update the network integration

Updates a subset of the network integration configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_integration_put import NetworkIntegrationPut
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
    api_instance = pyincusd.NetworkIntegrationsApi(api_client)
    integration = 'integration_example' # str | Path parameter: integration
    integration2 = pyincusd.NetworkIntegrationPut() # NetworkIntegrationPut | integration configuration

    try:
        # Partially update the network integration
        api_response = await api_instance.network_integration_patch(integration, integration2)
        print("The response of NetworkIntegrationsApi->network_integration_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkIntegrationsApi->network_integration_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| Path parameter: integration | 
 **integration2** | [**NetworkIntegrationPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationPut.md)| integration configuration | 

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

# **network_integration_post**
> ServerPut200Response network_integration_post(integration, integration2)

Rename the network integration

Renames the network integration.

### Example


```python
import pyincusd
from pyincusd.models.network_integration_post import NetworkIntegrationPost
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
    api_instance = pyincusd.NetworkIntegrationsApi(api_client)
    integration = 'integration_example' # str | Path parameter: integration
    integration2 = pyincusd.NetworkIntegrationPost() # NetworkIntegrationPost | integration configuration

    try:
        # Rename the network integration
        api_response = await api_instance.network_integration_post(integration, integration2)
        print("The response of NetworkIntegrationsApi->network_integration_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkIntegrationsApi->network_integration_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| Path parameter: integration | 
 **integration2** | [**NetworkIntegrationPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationPost.md)| integration configuration | 

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

# **network_integration_put**
> ServerPut200Response network_integration_put(integration, integration2)

Update the network integration

Updates the entire network integration configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_integration_put import NetworkIntegrationPut
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
    api_instance = pyincusd.NetworkIntegrationsApi(api_client)
    integration = 'integration_example' # str | Path parameter: integration
    integration2 = pyincusd.NetworkIntegrationPut() # NetworkIntegrationPut | integration configuration

    try:
        # Update the network integration
        api_response = await api_instance.network_integration_put(integration, integration2)
        print("The response of NetworkIntegrationsApi->network_integration_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkIntegrationsApi->network_integration_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| Path parameter: integration | 
 **integration2** | [**NetworkIntegrationPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationPut.md)| integration configuration | 

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

# **network_integrations_get**
> NetworkIntegrationsGet200Response network_integrations_get(filter=filter)

Get the network integrations

Returns a list of network integrations (URLs).

### Example


```python
import pyincusd
from pyincusd.models.network_integrations_get200_response import NetworkIntegrationsGet200Response
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
    api_instance = pyincusd.NetworkIntegrationsApi(api_client)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network integrations
        api_response = await api_instance.network_integrations_get(filter=filter)
        print("The response of NetworkIntegrationsApi->network_integrations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkIntegrationsApi->network_integrations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkIntegrationsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationsGet200Response.md)

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

# **network_integrations_get_recursion1**
> NetworkIntegrationsGetRecursion1200Response network_integrations_get_recursion1(filter=filter)

Get the network integrations

Returns a list of network integrations (structs).

### Example


```python
import pyincusd
from pyincusd.models.network_integrations_get_recursion1200_response import NetworkIntegrationsGetRecursion1200Response
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
    api_instance = pyincusd.NetworkIntegrationsApi(api_client)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network integrations
        api_response = await api_instance.network_integrations_get_recursion1(filter=filter)
        print("The response of NetworkIntegrationsApi->network_integrations_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkIntegrationsApi->network_integrations_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkIntegrationsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationsGetRecursion1200Response.md)

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

# **network_integrations_post**
> ServerPut200Response network_integrations_post(integration)

Add a network integration

Creates a new network integration.

### Example


```python
import pyincusd
from pyincusd.models.network_integrations_post import NetworkIntegrationsPost
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
    api_instance = pyincusd.NetworkIntegrationsApi(api_client)
    integration = pyincusd.NetworkIntegrationsPost() # NetworkIntegrationsPost | integration

    try:
        # Add a network integration
        api_response = await api_instance.network_integrations_post(integration)
        print("The response of NetworkIntegrationsApi->network_integrations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkIntegrationsApi->network_integrations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | [**NetworkIntegrationsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkIntegrationsPost.md)| integration | 

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

