# pyincusd.ImagesApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_alias_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#image_alias_delete) | **DELETE** /1.0/images/aliases/{name} | Delete the image alias
[**image_alias_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#image_alias_get) | **GET** /1.0/images/aliases/{name} | Get the image alias
[**image_alias_get_untrusted**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#image_alias_get_untrusted) | **GET** /1.0/images/aliases/{name}?public | Get the public image alias
[**image_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#image_delete) | **DELETE** /1.0/images/{fingerprint} | Delete the image
[**image_export_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#image_export_get) | **GET** /1.0/images/{fingerprint}/export | Get the raw image file(s)
[**image_export_get_untrusted**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#image_export_get_untrusted) | **GET** /1.0/images/{fingerprint}/export?public | Get the raw image file(s)
[**image_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#image_get) | **GET** /1.0/images/{fingerprint} | Get the image
[**image_get_untrusted**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#image_get_untrusted) | **GET** /1.0/images/{fingerprint}?public | Get the public image
[**image_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#image_patch) | **PATCH** /1.0/images/{fingerprint} | Partially update the image
[**image_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#image_put) | **PUT** /1.0/images/{fingerprint} | Update the image
[**images_alias_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_alias_patch) | **PATCH** /1.0/images/aliases/{name} | Partially update the image alias
[**images_alias_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_alias_post) | **POST** /1.0/images/aliases/{name} | Rename the image alias
[**images_aliases_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_aliases_get) | **GET** /1.0/images/aliases | Get the image aliases
[**images_aliases_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_aliases_get_recursion1) | **GET** /1.0/images/aliases?recursion&#x3D;1 | Get the image aliases
[**images_aliases_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_aliases_post) | **POST** /1.0/images/aliases | Add an image alias
[**images_aliases_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_aliases_put) | **PUT** /1.0/images/aliases/{name} | Update the image alias
[**images_export_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_export_post) | **POST** /1.0/images/{fingerprint}/export | Make the server push the image to a remote server
[**images_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_get) | **GET** /1.0/images | Get the images
[**images_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_get_recursion1) | **GET** /1.0/images?recursion&#x3D;1 | Get the images
[**images_get_recursion1_untrusted**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_get_recursion1_untrusted) | **GET** /1.0/images?public&amp;recursion&#x3D;1 | Get the public images
[**images_get_untrusted**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_get_untrusted) | **GET** /1.0/images?public | Get the public images
[**images_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_post) | **POST** /1.0/images | Add an image
[**images_post_untrusted**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_post_untrusted) | **POST** /1.0/images?public | Add an image
[**images_refresh_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_refresh_post) | **POST** /1.0/images/{fingerprint}/refresh | Refresh an image
[**images_secret_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesApi.md#images_secret_post) | **POST** /1.0/images/{fingerprint}/secret | Generate secret for retrieval of the image by an untrusted client


# **image_alias_delete**
> ServerPut200Response image_alias_delete(name, project=project)

Delete the image alias

Deletes a specific image alias.

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
    api_instance = pyincusd.ImagesApi(api_client)
    name = 'name_example' # str | Path parameter: name
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the image alias
        api_response = await api_instance.image_alias_delete(name, project=project)
        print("The response of ImagesApi->image_alias_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_alias_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

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

# **image_alias_get**
> ImageAliasGet200Response image_alias_get(name, project=project)

Get the image alias

Gets a specific image alias.

### Example


```python
import pyincusd
from pyincusd.models.image_alias_get200_response import ImageAliasGet200Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    name = 'name_example' # str | Path parameter: name
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the image alias
        api_response = await api_instance.image_alias_get(name, project=project)
        print("The response of ImagesApi->image_alias_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_alias_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ImageAliasGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImageAliasGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image alias |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_alias_get_untrusted**
> ImageAliasGet200Response image_alias_get_untrusted(name, project=project)

Get the public image alias

Gets a specific public image alias.
This untrusted endpoint only works for aliases pointing to public images.

### Example


```python
import pyincusd
from pyincusd.models.image_alias_get200_response import ImageAliasGet200Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    name = 'name_example' # str | Path parameter: name
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the public image alias
        api_response = await api_instance.image_alias_get_untrusted(name, project=project)
        print("The response of ImagesApi->image_alias_get_untrusted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_alias_get_untrusted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ImageAliasGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImageAliasGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image alias |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_delete**
> ClusterMembersPost202Response image_delete(fingerprint, project=project)

Delete the image

Removes the image from the image store.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    fingerprint = 'fingerprint_example' # str | Path parameter: fingerprint
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the image
        api_response = await api_instance.image_delete(fingerprint, project=project)
        print("The response of ImagesApi->image_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**| Path parameter: fingerprint | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_export_get**
> image_export_get(fingerprint, project=project)

Get the raw image file(s)

Download the raw image file(s) from the server.
If the image is in split format, a multipart http transfer occurs.

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
    api_instance = pyincusd.ImagesApi(api_client)
    fingerprint = 'fingerprint_example' # str | Path parameter: fingerprint
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the raw image file(s)
        await api_instance.image_export_get(fingerprint, project=project)
    except Exception as e:
        print("Exception when calling ImagesApi->image_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**| Path parameter: fingerprint | 
 **project** | **str**| Project name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw image data |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_export_get_untrusted**
> image_export_get_untrusted(fingerprint, project=project, secret=secret)

Get the raw image file(s)

Download the raw image file(s) of a public image from the server.
If the image is in split format, a multipart http transfer occurs.

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
    api_instance = pyincusd.ImagesApi(api_client)
    fingerprint = 'fingerprint_example' # str | Path parameter: fingerprint
    project = 'project_example' # str | Project name (optional)
    secret = 'secret_example' # str | Secret token to retrieve a private image (optional)

    try:
        # Get the raw image file(s)
        await api_instance.image_export_get_untrusted(fingerprint, project=project, secret=secret)
    except Exception as e:
        print("Exception when calling ImagesApi->image_export_get_untrusted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**| Path parameter: fingerprint | 
 **project** | **str**| Project name | [optional] 
 **secret** | **str**| Secret token to retrieve a private image | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, multipart/form-data

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw image data |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_get**
> ImageGet200Response image_get(fingerprint, project=project)

Get the image

Gets a specific image.

### Example


```python
import pyincusd
from pyincusd.models.image_get200_response import ImageGet200Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    fingerprint = 'fingerprint_example' # str | Path parameter: fingerprint
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the image
        api_response = await api_instance.image_get(fingerprint, project=project)
        print("The response of ImagesApi->image_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**| Path parameter: fingerprint | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ImageGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImageGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_get_untrusted**
> ImageGet200Response image_get_untrusted(fingerprint, project=project, secret=secret)

Get the public image

Gets a specific public image.

### Example


```python
import pyincusd
from pyincusd.models.image_get200_response import ImageGet200Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    fingerprint = 'fingerprint_example' # str | Path parameter: fingerprint
    project = 'project_example' # str | Project name (optional)
    secret = 'secret_example' # str | Secret token to retrieve a private image (optional)

    try:
        # Get the public image
        api_response = await api_instance.image_get_untrusted(fingerprint, project=project, secret=secret)
        print("The response of ImagesApi->image_get_untrusted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_get_untrusted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**| Path parameter: fingerprint | 
 **project** | **str**| Project name | [optional] 
 **secret** | **str**| Secret token to retrieve a private image | [optional] 

### Return type

[**ImageGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImageGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_patch**
> ServerPut200Response image_patch(fingerprint, image, project=project)

Partially update the image

Updates a subset of the image definition.

### Example


```python
import pyincusd
from pyincusd.models.image_put import ImagePut
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
    api_instance = pyincusd.ImagesApi(api_client)
    fingerprint = 'fingerprint_example' # str | Path parameter: fingerprint
    image = pyincusd.ImagePut() # ImagePut | Image configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Partially update the image
        api_response = await api_instance.image_patch(fingerprint, image, project=project)
        print("The response of ImagesApi->image_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**| Path parameter: fingerprint | 
 **image** | [**ImagePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagePut.md)| Image configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

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

# **image_put**
> ServerPut200Response image_put(fingerprint, image, project=project)

Update the image

Updates the entire image definition.

### Example


```python
import pyincusd
from pyincusd.models.image_put import ImagePut
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
    api_instance = pyincusd.ImagesApi(api_client)
    fingerprint = 'fingerprint_example' # str | Path parameter: fingerprint
    image = pyincusd.ImagePut() # ImagePut | Image configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Update the image
        api_response = await api_instance.image_put(fingerprint, image, project=project)
        print("The response of ImagesApi->image_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->image_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**| Path parameter: fingerprint | 
 **image** | [**ImagePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagePut.md)| Image configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

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

# **images_alias_patch**
> ServerPut200Response images_alias_patch(name, image_alias, project=project)

Partially update the image alias

Updates a subset of the image alias configuration.

### Example


```python
import pyincusd
from pyincusd.models.image_aliases_entry_put import ImageAliasesEntryPut
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
    api_instance = pyincusd.ImagesApi(api_client)
    name = 'name_example' # str | Path parameter: name
    image_alias = pyincusd.ImageAliasesEntryPut() # ImageAliasesEntryPut | Image alias configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Partially update the image alias
        api_response = await api_instance.images_alias_patch(name, image_alias, project=project)
        print("The response of ImagesApi->images_alias_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_alias_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **image_alias** | [**ImageAliasesEntryPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImageAliasesEntryPut.md)| Image alias configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

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

# **images_alias_post**
> ServerPut200Response images_alias_post(name, image_alias, project=project)

Rename the image alias

Renames an existing image alias.

### Example


```python
import pyincusd
from pyincusd.models.image_aliases_entry_post import ImageAliasesEntryPost
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
    api_instance = pyincusd.ImagesApi(api_client)
    name = 'name_example' # str | Path parameter: name
    image_alias = pyincusd.ImageAliasesEntryPost() # ImageAliasesEntryPost | Image alias rename request
    project = 'project_example' # str | Project name (optional)

    try:
        # Rename the image alias
        api_response = await api_instance.images_alias_post(name, image_alias, project=project)
        print("The response of ImagesApi->images_alias_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_alias_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **image_alias** | [**ImageAliasesEntryPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImageAliasesEntryPost.md)| Image alias rename request | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

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

# **images_aliases_get**
> ImagesAliasesGet200Response images_aliases_get(project=project)

Get the image aliases

Returns a list of image aliases (URLs).

### Example


```python
import pyincusd
from pyincusd.models.images_aliases_get200_response import ImagesAliasesGet200Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the image aliases
        api_response = await api_instance.images_aliases_get(project=project)
        print("The response of ImagesApi->images_aliases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_aliases_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ImagesAliasesGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesAliasesGet200Response.md)

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

# **images_aliases_get_recursion1**
> ImagesAliasesGetRecursion1200Response images_aliases_get_recursion1(project=project)

Get the image aliases

Returns a list of image aliases (structs).

### Example


```python
import pyincusd
from pyincusd.models.images_aliases_get_recursion1200_response import ImagesAliasesGetRecursion1200Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the image aliases
        api_response = await api_instance.images_aliases_get_recursion1(project=project)
        print("The response of ImagesApi->images_aliases_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_aliases_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ImagesAliasesGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesAliasesGetRecursion1200Response.md)

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

# **images_aliases_post**
> ServerPut200Response images_aliases_post(image_alias, project=project)

Add an image alias

Creates a new image alias.

### Example


```python
import pyincusd
from pyincusd.models.image_aliases_post import ImageAliasesPost
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
    api_instance = pyincusd.ImagesApi(api_client)
    image_alias = pyincusd.ImageAliasesPost() # ImageAliasesPost | Image alias
    project = 'project_example' # str | Project name (optional)

    try:
        # Add an image alias
        api_response = await api_instance.images_aliases_post(image_alias, project=project)
        print("The response of ImagesApi->images_aliases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_aliases_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_alias** | [**ImageAliasesPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImageAliasesPost.md)| Image alias | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

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

# **images_aliases_put**
> ServerPut200Response images_aliases_put(name, image_alias, project=project)

Update the image alias

Updates the entire image alias configuration.

### Example


```python
import pyincusd
from pyincusd.models.image_aliases_entry_put import ImageAliasesEntryPut
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
    api_instance = pyincusd.ImagesApi(api_client)
    name = 'name_example' # str | Path parameter: name
    image_alias = pyincusd.ImageAliasesEntryPut() # ImageAliasesEntryPut | Image alias configuration
    project = 'project_example' # str | Project name (optional)

    try:
        # Update the image alias
        api_response = await api_instance.images_aliases_put(name, image_alias, project=project)
        print("The response of ImagesApi->images_aliases_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_aliases_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Path parameter: name | 
 **image_alias** | [**ImageAliasesEntryPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImageAliasesEntryPut.md)| Image alias configuration | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

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

# **images_export_post**
> ClusterMembersPost202Response images_export_post(fingerprint, image, project=project)

Make the server push the image to a remote server

Gets the server to connect to a remote server and push the image to it.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.image_export_post import ImageExportPost
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
    api_instance = pyincusd.ImagesApi(api_client)
    fingerprint = 'fingerprint_example' # str | Path parameter: fingerprint
    image = pyincusd.ImageExportPost() # ImageExportPost | Image push request
    project = 'project_example' # str | Project name (optional)

    try:
        # Make the server push the image to a remote server
        api_response = await api_instance.images_export_post(fingerprint, image, project=project)
        print("The response of ImagesApi->images_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**| Path parameter: fingerprint | 
 **image** | [**ImageExportPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImageExportPost.md)| Image push request | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_get**
> ImagesGet200Response images_get(project=project, filter=filter, all_projects=all_projects)

Get the images

Returns a list of images (URLs).

### Example


```python
import pyincusd
from pyincusd.models.images_get200_response import ImagesGet200Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)
    all_projects = True # bool | Retrieve images from all projects (optional)

    try:
        # Get the images
        api_response = await api_instance.images_get(project=project, filter=filter, all_projects=all_projects)
        print("The response of ImagesApi->images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 
 **all_projects** | **bool**| Retrieve images from all projects | [optional] 

### Return type

[**ImagesGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesGet200Response.md)

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

# **images_get_recursion1**
> ImagesGetRecursion1Untrusted200Response images_get_recursion1(project=project, filter=filter, all_projects=all_projects)

Get the images

Returns a list of images (structs).

### Example


```python
import pyincusd
from pyincusd.models.images_get_recursion1_untrusted200_response import ImagesGetRecursion1Untrusted200Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)
    all_projects = True # bool | Retrieve images from all projects (optional)

    try:
        # Get the images
        api_response = await api_instance.images_get_recursion1(project=project, filter=filter, all_projects=all_projects)
        print("The response of ImagesApi->images_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 
 **all_projects** | **bool**| Retrieve images from all projects | [optional] 

### Return type

[**ImagesGetRecursion1Untrusted200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesGetRecursion1Untrusted200Response.md)

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

# **images_get_recursion1_untrusted**
> ImagesGetRecursion1Untrusted200Response images_get_recursion1_untrusted(project=project, filter=filter, all_projects=all_projects)

Get the public images

Returns a list of publicly available images (structs).

### Example


```python
import pyincusd
from pyincusd.models.images_get_recursion1_untrusted200_response import ImagesGetRecursion1Untrusted200Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)
    all_projects = True # bool | Retrieve images from all projects (optional)

    try:
        # Get the public images
        api_response = await api_instance.images_get_recursion1_untrusted(project=project, filter=filter, all_projects=all_projects)
        print("The response of ImagesApi->images_get_recursion1_untrusted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_get_recursion1_untrusted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 
 **all_projects** | **bool**| Retrieve images from all projects | [optional] 

### Return type

[**ImagesGetRecursion1Untrusted200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesGetRecursion1Untrusted200Response.md)

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

# **images_get_untrusted**
> ImagesGet200Response images_get_untrusted(project=project, filter=filter, all_projects=all_projects)

Get the public images

Returns a list of publicly available images (URLs).

### Example


```python
import pyincusd
from pyincusd.models.images_get200_response import ImagesGet200Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)
    all_projects = True # bool | Retrieve images from all projects (optional)

    try:
        # Get the public images
        api_response = await api_instance.images_get_untrusted(project=project, filter=filter, all_projects=all_projects)
        print("The response of ImagesApi->images_get_untrusted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_get_untrusted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 
 **all_projects** | **bool**| Retrieve images from all projects | [optional] 

### Return type

[**ImagesGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesGet200Response.md)

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

# **images_post**
> ClusterMembersPost202Response images_post(project=project, x_incus_secret=x_incus_secret, x_incus_fingerprint=x_incus_fingerprint, x_incus_aliases=x_incus_aliases, x_incus_properties=x_incus_properties, x_incus_public=x_incus_public, x_incus_filename=x_incus_filename, x_incus_profiles=x_incus_profiles)

Add an image

Adds a new image to the image store.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    x_incus_secret = None # object | Push secret for server to server communication (optional)
    x_incus_fingerprint = None # object | Expected fingerprint when pushing a raw image (optional)
    x_incus_aliases = None # object | List of aliases to assign (optional)
    x_incus_properties = None # object | Descriptive properties (optional)
    x_incus_public = None # object | Whether the image is available to unauthenticated users (optional)
    x_incus_filename = None # object | Original filename of the image (optional)
    x_incus_profiles = None # object | List of profiles to use (optional)

    try:
        # Add an image
        api_response = await api_instance.images_post(project=project, x_incus_secret=x_incus_secret, x_incus_fingerprint=x_incus_fingerprint, x_incus_aliases=x_incus_aliases, x_incus_properties=x_incus_properties, x_incus_public=x_incus_public, x_incus_filename=x_incus_filename, x_incus_profiles=x_incus_profiles)
        print("The response of ImagesApi->images_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **x_incus_secret** | [**object**](.md)| Push secret for server to server communication | [optional] 
 **x_incus_fingerprint** | [**object**](.md)| Expected fingerprint when pushing a raw image | [optional] 
 **x_incus_aliases** | [**object**](.md)| List of aliases to assign | [optional] 
 **x_incus_properties** | [**object**](.md)| Descriptive properties | [optional] 
 **x_incus_public** | [**object**](.md)| Whether the image is available to unauthenticated users | [optional] 
 **x_incus_filename** | [**object**](.md)| Original filename of the image | [optional] 
 **x_incus_profiles** | [**object**](.md)| List of profiles to use | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_post_untrusted**
> ServerPut200Response images_post_untrusted(image, project=project)

Add an image

Pushes the data to the target image server.
This is meant for server to server communication where a new image entry is
prepared on the target server and the source server is provided that URL
and a secret token to push the image content over.

### Example


```python
import pyincusd
from pyincusd.models.images_post import ImagesPost
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
    api_instance = pyincusd.ImagesApi(api_client)
    image = pyincusd.ImagesPost() # ImagesPost | Image
    project = 'project_example' # str | Project name (optional)

    try:
        # Add an image
        api_response = await api_instance.images_post_untrusted(image, project=project)
        print("The response of ImagesApi->images_post_untrusted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_post_untrusted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | [**ImagesPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ImagesPost.md)| Image | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ServerPut200Response.md)

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

# **images_refresh_post**
> ClusterMembersPost202Response images_refresh_post(fingerprint, project=project)

Refresh an image

This causes the server to check the image source server for an updated
version of the image and if available to refresh the local copy with the
new version.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    fingerprint = 'fingerprint_example' # str | Path parameter: fingerprint
    project = 'project_example' # str | Project name (optional)

    try:
        # Refresh an image
        api_response = await api_instance.images_refresh_post(fingerprint, project=project)
        print("The response of ImagesApi->images_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**| Path parameter: fingerprint | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_secret_post**
> ClusterMembersPost202Response images_secret_post(fingerprint, project=project)

Generate secret for retrieval of the image by an untrusted client

This generates a background operation including a secret one time key
in its metadata which can be used to fetch this image from an untrusted
client.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
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
    api_instance = pyincusd.ImagesApi(api_client)
    fingerprint = 'fingerprint_example' # str | Path parameter: fingerprint
    project = 'project_example' # str | Project name (optional)

    try:
        # Generate secret for retrieval of the image by an untrusted client
        api_response = await api_instance.images_secret_post(fingerprint, project=project)
        print("The response of ImagesApi->images_secret_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_secret_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fingerprint** | **str**| Path parameter: fingerprint | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

