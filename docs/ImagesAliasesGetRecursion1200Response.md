# ImagesAliasesGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[ImageAliasesEntry]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ImageAliasesEntry.md) | List of image aliases | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.images_aliases_get_recursion1200_response import ImagesAliasesGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesAliasesGetRecursion1200Response from a JSON string
images_aliases_get_recursion1200_response_instance = ImagesAliasesGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(ImagesAliasesGetRecursion1200Response.to_json())

# convert the object into a dict
images_aliases_get_recursion1200_response_dict = images_aliases_get_recursion1200_response_instance.to_dict()
# create an instance of ImagesAliasesGetRecursion1200Response from a dict
images_aliases_get_recursion1200_response_from_dict = ImagesAliasesGetRecursion1200Response.from_dict(images_aliases_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


