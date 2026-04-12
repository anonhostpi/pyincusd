# MetadataConfigGroup

MetadataConfigGroup represents a group of config keys

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[Dict[str, MetadataConfigKey]]** |  | [optional] 

## Example

```python
from pyincusd.models.metadata_config_group import MetadataConfigGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataConfigGroup from a JSON string
metadata_config_group_instance = MetadataConfigGroup.from_json(json)
# print the JSON string representation of the object
print(MetadataConfigGroup.to_json())

# convert the object into a dict
metadata_config_group_dict = metadata_config_group_instance.to_dict()
# create an instance of MetadataConfigGroup from a dict
metadata_config_group_from_dict = MetadataConfigGroup.from_dict(metadata_config_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


