# pyincusd.CertificatesApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificate_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesApi.md#certificate_delete) | **DELETE** /1.0/certificates/{fingerprint} | Delete the trusted certificate
[**certificate_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesApi.md#certificate_get) | **GET** /1.0/certificates/{fingerprint} | Get the trusted certificate
[**certificate_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesApi.md#certificate_patch) | **PATCH** /1.0/certificates/{fingerprint} | Partially update the trusted certificate
[**certificate_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesApi.md#certificate_put) | **PUT** /1.0/certificates/{fingerprint} | Update the trusted certificate
[**certificates_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesApi.md#certificates_get) | **GET** /1.0/certificates | Get the trusted certificates
[**certificates_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesApi.md#certificates_get_recursion1) | **GET** /1.0/certificates?recursion&#x3D;1 | Get the trusted certificates
[**certificates_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesApi.md#certificates_post) | **POST** /1.0/certificates | Add a trusted certificate
[**certificates_post_untrusted**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesApi.md#certificates_post_untrusted) | **POST** /1.0/certificates?public | Add a trusted certificate


# **certificate_delete**
> ServerPut200Response certificate_delete()

Delete the trusted certificate

Removes the certificate from the trust store.

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
    api_instance = pyincusd.CertificatesApi(api_client)

    try:
        # Delete the trusted certificate
        api_response = await api_instance.certificate_delete()
        print("The response of CertificatesApi->certificate_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificate_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/ServerPut200Response.md)

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

# **certificate_get**
> CertificateGet200Response certificate_get()

Get the trusted certificate

Gets a specific certificate entry from the trust store.

### Example


```python
import pyincusd
from pyincusd.models.certificate_get200_response import CertificateGet200Response
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
    api_instance = pyincusd.CertificatesApi(api_client)

    try:
        # Get the trusted certificate
        api_response = await api_instance.certificate_get()
        print("The response of CertificatesApi->certificate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificate_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CertificateGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificateGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificate_patch**
> ServerPut200Response certificate_patch(certificate)

Partially update the trusted certificate

Updates a subset of the certificate configuration.

### Example


```python
import pyincusd
from pyincusd.models.certificate_put import CertificatePut
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
    api_instance = pyincusd.CertificatesApi(api_client)
    certificate = pyincusd.CertificatePut() # CertificatePut | Certificate configuration

    try:
        # Partially update the trusted certificate
        api_response = await api_instance.certificate_patch(certificate)
        print("The response of CertificatesApi->certificate_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificate_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | [**CertificatePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatePut.md)| Certificate configuration | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/ServerPut200Response.md)

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

# **certificate_put**
> ServerPut200Response certificate_put(certificate)

Update the trusted certificate

Updates the entire certificate configuration.

### Example


```python
import pyincusd
from pyincusd.models.certificate_put import CertificatePut
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
    api_instance = pyincusd.CertificatesApi(api_client)
    certificate = pyincusd.CertificatePut() # CertificatePut | Certificate configuration

    try:
        # Update the trusted certificate
        api_response = await api_instance.certificate_put(certificate)
        print("The response of CertificatesApi->certificate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | [**CertificatePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatePut.md)| Certificate configuration | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/ServerPut200Response.md)

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

# **certificates_get**
> CertificatesGet200Response certificates_get(filter=filter)

Get the trusted certificates

Returns a list of trusted certificates (URLs).

### Example


```python
import pyincusd
from pyincusd.models.certificates_get200_response import CertificatesGet200Response
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
    api_instance = pyincusd.CertificatesApi(api_client)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the trusted certificates
        api_response = await api_instance.certificates_get(filter=filter)
        print("The response of CertificatesApi->certificates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**CertificatesGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesGet200Response.md)

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

# **certificates_get_recursion1**
> CertificatesGetRecursion1200Response certificates_get_recursion1(filter=filter)

Get the trusted certificates

Returns a list of trusted certificates (structs).

### Example


```python
import pyincusd
from pyincusd.models.certificates_get_recursion1200_response import CertificatesGetRecursion1200Response
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
    api_instance = pyincusd.CertificatesApi(api_client)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the trusted certificates
        api_response = await api_instance.certificates_get_recursion1(filter=filter)
        print("The response of CertificatesApi->certificates_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificates_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**CertificatesGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesGetRecursion1200Response.md)

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

# **certificates_post**
> ServerPut200Response certificates_post(certificate)

Add a trusted certificate

Adds a certificate to the trust store.
In this mode, the `token` property is always ignored.

### Example


```python
import pyincusd
from pyincusd.models.certificates_post import CertificatesPost
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
    api_instance = pyincusd.CertificatesApi(api_client)
    certificate = pyincusd.CertificatesPost() # CertificatesPost | Certificate

    try:
        # Add a trusted certificate
        api_response = await api_instance.certificates_post(certificate)
        print("The response of CertificatesApi->certificates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | [**CertificatesPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesPost.md)| Certificate | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/ServerPut200Response.md)

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

# **certificates_post_untrusted**
> ServerPut200Response certificates_post_untrusted(certificate)

Add a trusted certificate

Adds a certificate to the trust store as an untrusted user.
In this mode, the `token` property must be set to the correct value.

The `certificate` field can be omitted in which case the TLS client
certificate in use for the connection will be retrieved and added to the
trust store.

The `?public` part of the URL isn't required, it's simply used to
separate the two behaviors of this endpoint.

### Example


```python
import pyincusd
from pyincusd.models.certificates_post import CertificatesPost
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
    api_instance = pyincusd.CertificatesApi(api_client)
    certificate = pyincusd.CertificatesPost() # CertificatesPost | Certificate

    try:
        # Add a trusted certificate
        api_response = await api_instance.certificates_post_untrusted(certificate)
        print("The response of CertificatesApi->certificates_post_untrusted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificates_post_untrusted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | [**CertificatesPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/CertificatesPost.md)| Certificate | 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/ServerPut200Response.md)

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

