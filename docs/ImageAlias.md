# ImageAlias

ImageAlias represents an alias from the alias list of an image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the alias | [optional] 
**name** | **str** | Name of the alias | [optional] 

## Example

```python
from pyincusd.models.image_alias import ImageAlias

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAlias from a JSON string
image_alias_instance = ImageAlias.from_json(json)
# print the JSON string representation of the object
print(ImageAlias.to_json())

# convert the object into a dict
image_alias_dict = image_alias_instance.to_dict()
# create an instance of ImageAlias from a dict
image_alias_from_dict = ImageAlias.from_dict(image_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


