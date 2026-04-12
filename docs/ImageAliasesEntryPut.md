# ImageAliasesEntryPut

ImageAliasesEntryPut represents the modifiable fields of an image alias

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Alias description | [optional] 
**target** | **str** | Target fingerprint for the alias | [optional] 

## Example

```python
from pyincusd.models.image_aliases_entry_put import ImageAliasesEntryPut

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAliasesEntryPut from a JSON string
image_aliases_entry_put_instance = ImageAliasesEntryPut.from_json(json)
# print the JSON string representation of the object
print(ImageAliasesEntryPut.to_json())

# convert the object into a dict
image_aliases_entry_put_dict = image_aliases_entry_put_instance.to_dict()
# create an instance of ImageAliasesEntryPut from a dict
image_aliases_entry_put_from_dict = ImageAliasesEntryPut.from_dict(image_aliases_entry_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


