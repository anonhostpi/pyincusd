# pyincusd.NetworkAllocationsApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_allocations_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post19/docs/NetworkAllocationsApi.md#network_allocations_get) | **GET** /1.0/network-allocations | Get the network allocations in use (&#x60;network&#x60;, &#x60;network-forward&#x60; and &#x60;load-balancer&#x60; and &#x60;instance&#x60;)


# **network_allocations_get**
> NetworkAllocationsGet200Response network_allocations_get(project=project, all_projects=all_projects)

Get the network allocations in use (`network`, `network-forward` and `load-balancer` and `instance`)

Returns a list of network allocations.

### Example


```python
import pyincusd
from pyincusd.models.network_allocations_get200_response import NetworkAllocationsGet200Response
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
    api_instance = pyincusd.NetworkAllocationsApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve entities from all projects (optional)

    try:
        # Get the network allocations in use (`network`, `network-forward` and `load-balancer` and `instance`)
        api_response = await api_instance.network_allocations_get(project=project, all_projects=all_projects)
        print("The response of NetworkAllocationsApi->network_allocations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkAllocationsApi->network_allocations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve entities from all projects | [optional] 

### Return type

[**NetworkAllocationsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post19/docs/NetworkAllocationsGet200Response.md)

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

