# MetadataConfigKey

MetadataConfigKey describe a configuration key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | Condition specifies the condition that must be met for the option to be taken into account | [optional] 
**defaultdesc** | **str** | DefaultDesc specify default value for configuration | [optional] 
**liveupdate** | **str** | LiveUpdate specifies whether the server must be restarted for the option to be updated | [optional] 
**longdesc** | **str** | LongDesc provides long description for the option | [optional] 
**scope** | **str** | Scope defines if option apply to cluster or to the local server | [optional] 
**shortdesc** | **str** | ShortDesc provides short description for the configuration | [optional] 
**type** | **str** | Type specifies the type of the option | [optional] 

## Example

```python
from pyincusd.models.metadata_config_key import MetadataConfigKey

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataConfigKey from a JSON string
metadata_config_key_instance = MetadataConfigKey.from_json(json)
# print the JSON string representation of the object
print(MetadataConfigKey.to_json())

# convert the object into a dict
metadata_config_key_dict = metadata_config_key_instance.to_dict()
# create an instance of MetadataConfigKey from a dict
metadata_config_key_from_dict = MetadataConfigKey.from_dict(metadata_config_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


