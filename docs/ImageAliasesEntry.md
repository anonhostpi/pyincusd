# ImageAliasesEntry

ImageAliasesEntry represents an image alias

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Alias description | [optional] 
**name** | **str** | Alias name | [optional] 
**target** | **str** | Target fingerprint for the alias | [optional] 
**type** | **str** | Alias type (container or virtual-machine) | [optional] 

## Example

```python
from pyincusd.models.image_aliases_entry import ImageAliasesEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAliasesEntry from a JSON string
image_aliases_entry_instance = ImageAliasesEntry.from_json(json)
# print the JSON string representation of the object
print(ImageAliasesEntry.to_json())

# convert the object into a dict
image_aliases_entry_dict = image_aliases_entry_instance.to_dict()
# create an instance of ImageAliasesEntry from a dict
image_aliases_entry_from_dict = ImageAliasesEntry.from_dict(image_aliases_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


