# pyincusd.MetricsApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/MetricsApi.md#metrics_get) | **GET** /1.0/metrics | Get metrics


# **metrics_get**
> str metrics_get(project=project, target=target)

Get metrics

Gets metrics of instances.

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
    api_instance = pyincusd.MetricsApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get metrics
        api_response = await api_instance.metrics_get(project=project, target=target)
        print("The response of MetricsApi->metrics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->metrics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metrics |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

