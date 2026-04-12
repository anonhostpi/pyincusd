# pyincusd.DefaultApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_configuration_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/DefaultApi.md#metadata_configuration_get) | **GET** /1.0/metadata/configuration | Get the metadata configuration


# **metadata_configuration_get**
> MetadataConfigurationGet200Response metadata_configuration_get()

Get the metadata configuration

Returns the generated metadata configuration in YAML format.

### Example


```python
import pyincusd
from pyincusd.models.metadata_configuration_get200_response import MetadataConfigurationGet200Response
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
    api_instance = pyincusd.DefaultApi(api_client)

    try:
        # Get the metadata configuration
        api_response = await api_instance.metadata_configuration_get()
        print("The response of DefaultApi->metadata_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->metadata_configuration_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MetadataConfigurationGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/MetadataConfigurationGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

