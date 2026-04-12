# ImagesGetRecursion1Untrusted200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[Image]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/Image.md) | List of images | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.images_get_recursion1_untrusted200_response import ImagesGetRecursion1Untrusted200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesGetRecursion1Untrusted200Response from a JSON string
images_get_recursion1_untrusted200_response_instance = ImagesGetRecursion1Untrusted200Response.from_json(json)
# print the JSON string representation of the object
print(ImagesGetRecursion1Untrusted200Response.to_json())

# convert the object into a dict
images_get_recursion1_untrusted200_response_dict = images_get_recursion1_untrusted200_response_instance.to_dict()
# create an instance of ImagesGetRecursion1Untrusted200Response from a dict
images_get_recursion1_untrusted200_response_from_dict = ImagesGetRecursion1Untrusted200Response.from_dict(images_get_recursion1_untrusted200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


