# ImageAliasGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ImageAliasesEntry**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/ImageAliasesEntry.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.image_alias_get200_response import ImageAliasGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAliasGet200Response from a JSON string
image_alias_get200_response_instance = ImageAliasGet200Response.from_json(json)
# print the JSON string representation of the object
print(ImageAliasGet200Response.to_json())

# convert the object into a dict
image_alias_get200_response_dict = image_alias_get200_response_instance.to_dict()
# create an instance of ImageAliasGet200Response from a dict
image_alias_get200_response_from_dict = ImageAliasGet200Response.from_dict(image_alias_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


