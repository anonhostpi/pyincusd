# ImageAliasesEntryPost

ImageAliasesEntryPost represents the required fields to rename an image alias

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Alias name | [optional] 

## Example

```python
from pyincusd.models.image_aliases_entry_post import ImageAliasesEntryPost

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAliasesEntryPost from a JSON string
image_aliases_entry_post_instance = ImageAliasesEntryPost.from_json(json)
# print the JSON string representation of the object
print(ImageAliasesEntryPost.to_json())

# convert the object into a dict
image_aliases_entry_post_dict = image_aliases_entry_post_instance.to_dict()
# create an instance of ImageAliasesEntryPost from a dict
image_aliases_entry_post_from_dict = ImageAliasesEntryPost.from_dict(image_aliases_entry_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


