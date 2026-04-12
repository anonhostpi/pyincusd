# ImageAliasesPost

ImageAliasesPost represents a new image alias

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Alias description | [optional] 
**name** | **str** | Alias name | [optional] 
**target** | **str** | Target fingerprint for the alias | [optional] 
**type** | **str** | Alias type (container or virtual-machine) | [optional] 

## Example

```python
from pyincusd.models.image_aliases_post import ImageAliasesPost

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAliasesPost from a JSON string
image_aliases_post_instance = ImageAliasesPost.from_json(json)
# print the JSON string representation of the object
print(ImageAliasesPost.to_json())

# convert the object into a dict
image_aliases_post_dict = image_aliases_post_instance.to_dict()
# create an instance of ImageAliasesPost from a dict
image_aliases_post_from_dict = ImageAliasesPost.from_dict(image_aliases_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


