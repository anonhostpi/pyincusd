# pyincusd.NetworkZonesApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_zone_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zone_delete) | **DELETE** /1.0/network-zones/{zone} | Delete the network zone
[**network_zone_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zone_get) | **GET** /1.0/network-zones/{zone} | Get the network zone
[**network_zone_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zone_patch) | **PATCH** /1.0/network-zones/{zone} | Partially update the network zone
[**network_zone_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zone_put) | **PUT** /1.0/network-zones/{zone} | Update the network zone
[**network_zone_record_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zone_record_delete) | **DELETE** /1.0/network-zones/{zone}/records/{name} | Delete the network zone record
[**network_zone_record_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zone_record_get) | **GET** /1.0/network-zones/{zone}/records/{name} | Get the network zone record
[**network_zone_record_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zone_record_patch) | **PATCH** /1.0/network-zones/{zone}/records/{name} | Partially update the network zone record
[**network_zone_record_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zone_record_put) | **PUT** /1.0/network-zones/{zone}/records/{name} | Update the network zone record
[**network_zone_records_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zone_records_get) | **GET** /1.0/network-zones/{zone}/records | Get the network zone records
[**network_zone_records_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zone_records_get_recursion1) | **GET** /1.0/network-zones/{zone}/records?recursion&#x3D;1 | Get the network zone records
[**network_zone_records_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zone_records_post) | **POST** /1.0/network-zones/{zone}/records | Add a network zone record
[**network_zones_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zones_get) | **GET** /1.0/network-zones | Get the network zones
[**network_zones_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zones_get_recursion1) | **GET** /1.0/network-zones?recursion&#x3D;1 | Get the network zones
[**network_zones_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesApi.md#network_zones_post) | **POST** /1.0/network-zones | Add a network zone


# **network_zone_delete**
> ServerPut200Response network_zone_delete(project=project)

Delete the network zone

Removes the network zone.

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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the network zone
        api_response = await api_instance.network_zone_delete(project=project)
        print("The response of NetworkZonesApi->network_zone_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zone_delete: %s\n" % e)
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

# **network_zone_get**
> NetworkZoneGet200Response network_zone_get(project=project)

Get the network zone

Gets a specific network zone.

### Example


```python
import pyincusd
from pyincusd.models.network_zone_get200_response import NetworkZoneGet200Response
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the network zone
        api_response = await api_instance.network_zone_get(project=project)
        print("The response of NetworkZonesApi->network_zone_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zone_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**NetworkZoneGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZoneGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | zone |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_zone_patch**
> ServerPut200Response network_zone_patch(zone, project=project)

Partially update the network zone

Updates a subset of the network zone configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_zone_put import NetworkZonePut
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    zone = pyincusd.NetworkZonePut() # NetworkZonePut | zone configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Partially update the network zone
        api_response = await api_instance.network_zone_patch(zone, project=project)
        print("The response of NetworkZonesApi->network_zone_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zone_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | [**NetworkZonePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonePut.md)| zone configuration | 
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

# **network_zone_put**
> ServerPut200Response network_zone_put(zone, project=project)

Update the network zone

Updates the entire network zone configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_zone_put import NetworkZonePut
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    zone = pyincusd.NetworkZonePut() # NetworkZonePut | zone configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Update the network zone
        api_response = await api_instance.network_zone_put(zone, project=project)
        print("The response of NetworkZonesApi->network_zone_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zone_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | [**NetworkZonePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonePut.md)| zone configuration | 
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

# **network_zone_record_delete**
> ServerPut200Response network_zone_record_delete(project=project)

Delete the network zone record

Removes the network zone record.

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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the network zone record
        api_response = await api_instance.network_zone_record_delete(project=project)
        print("The response of NetworkZonesApi->network_zone_record_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zone_record_delete: %s\n" % e)
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

# **network_zone_record_get**
> NetworkZoneRecordGet200Response network_zone_record_get(project=project)

Get the network zone record

Gets a specific network zone record.

### Example


```python
import pyincusd
from pyincusd.models.network_zone_record_get200_response import NetworkZoneRecordGet200Response
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the network zone record
        api_response = await api_instance.network_zone_record_get(project=project)
        print("The response of NetworkZonesApi->network_zone_record_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zone_record_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**NetworkZoneRecordGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZoneRecordGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | zone |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_zone_record_patch**
> ServerPut200Response network_zone_record_patch(zone, project=project)

Partially update the network zone record

Updates a subset of the network zone record configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_zone_record_put import NetworkZoneRecordPut
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    zone = pyincusd.NetworkZoneRecordPut() # NetworkZoneRecordPut | zone record configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Partially update the network zone record
        api_response = await api_instance.network_zone_record_patch(zone, project=project)
        print("The response of NetworkZonesApi->network_zone_record_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zone_record_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | [**NetworkZoneRecordPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZoneRecordPut.md)| zone record configuration | 
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

# **network_zone_record_put**
> ServerPut200Response network_zone_record_put(zone, project=project)

Update the network zone record

Updates the entire network zone record configuration.

### Example


```python
import pyincusd
from pyincusd.models.network_zone_record_put import NetworkZoneRecordPut
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    zone = pyincusd.NetworkZoneRecordPut() # NetworkZoneRecordPut | zone record configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Update the network zone record
        api_response = await api_instance.network_zone_record_put(zone, project=project)
        print("The response of NetworkZonesApi->network_zone_record_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zone_record_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | [**NetworkZoneRecordPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZoneRecordPut.md)| zone record configuration | 
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

# **network_zone_records_get**
> NetworkZoneRecordsGet200Response network_zone_records_get(project=project, filter=filter)

Get the network zone records

Returns a list of network zone records (URLs).

### Example


```python
import pyincusd
from pyincusd.models.network_zone_records_get200_response import NetworkZoneRecordsGet200Response
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network zone records
        api_response = await api_instance.network_zone_records_get(project=project, filter=filter)
        print("The response of NetworkZonesApi->network_zone_records_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zone_records_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkZoneRecordsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZoneRecordsGet200Response.md)

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

# **network_zone_records_get_recursion1**
> NetworkZoneRecordsGetRecursion1200Response network_zone_records_get_recursion1(project=project, filter=filter)

Get the network zone records

Returns a list of network zone records (structs).

### Example


```python
import pyincusd
from pyincusd.models.network_zone_records_get_recursion1200_response import NetworkZoneRecordsGetRecursion1200Response
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network zone records
        api_response = await api_instance.network_zone_records_get_recursion1(project=project, filter=filter)
        print("The response of NetworkZonesApi->network_zone_records_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zone_records_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkZoneRecordsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZoneRecordsGetRecursion1200Response.md)

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

# **network_zone_records_post**
> ServerPut200Response network_zone_records_post(zone, project=project)

Add a network zone record

Creates a new network zone record.

### Example


```python
import pyincusd
from pyincusd.models.network_zone_records_post import NetworkZoneRecordsPost
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    zone = pyincusd.NetworkZoneRecordsPost() # NetworkZoneRecordsPost | zone
    project = 'project_example' # str | Project name (optional)

    try:
        # Add a network zone record
        api_response = await api_instance.network_zone_records_post(zone, project=project)
        print("The response of NetworkZonesApi->network_zone_records_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zone_records_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | [**NetworkZoneRecordsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZoneRecordsPost.md)| zone | 
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

# **network_zones_get**
> NetworkZonesGet200Response network_zones_get(project=project, all_projects=all_projects, filter=filter)

Get the network zones

Returns a list of network zones (URLs).

### Example


```python
import pyincusd
from pyincusd.models.network_zones_get200_response import NetworkZonesGet200Response
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve network zones from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network zones
        api_response = await api_instance.network_zones_get(project=project, all_projects=all_projects, filter=filter)
        print("The response of NetworkZonesApi->network_zones_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zones_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve network zones from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkZonesGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesGet200Response.md)

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

# **network_zones_get_recursion1**
> NetworkZonesGetRecursion1200Response network_zones_get_recursion1(project=project, all_projects=all_projects, filter=filter)

Get the network zones

Returns a list of network zones (structs).

### Example


```python
import pyincusd
from pyincusd.models.network_zones_get_recursion1200_response import NetworkZonesGetRecursion1200Response
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve network zones from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the network zones
        api_response = await api_instance.network_zones_get_recursion1(project=project, all_projects=all_projects, filter=filter)
        print("The response of NetworkZonesApi->network_zones_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zones_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve network zones from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**NetworkZonesGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesGetRecursion1200Response.md)

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

# **network_zones_post**
> ServerPut200Response network_zones_post(zone, project=project)

Add a network zone

Creates a new network zone.

### Example


```python
import pyincusd
from pyincusd.models.network_zones_post import NetworkZonesPost
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
    api_instance = pyincusd.NetworkZonesApi(api_client)
    zone = pyincusd.NetworkZonesPost() # NetworkZonesPost | zone
    project = 'project_example' # str | Project name (optional)

    try:
        # Add a network zone
        api_response = await api_instance.network_zones_post(zone, project=project)
        print("The response of NetworkZonesApi->network_zones_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZonesApi->network_zones_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | [**NetworkZonesPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkZonesPost.md)| zone | 
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

