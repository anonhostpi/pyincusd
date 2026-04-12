# StorageVolumeStateUsage

StorageVolumeStateUsage represents the disk usage of a volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Storage volume size in bytes | [optional] 
**used** | **int** | Used space in bytes | [optional] 

## Example

```python
from pyincusd.models.storage_volume_state_usage import StorageVolumeStateUsage

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolumeStateUsage from a JSON string
storage_volume_state_usage_instance = StorageVolumeStateUsage.from_json(json)
# print the JSON string representation of the object
print(StorageVolumeStateUsage.to_json())

# convert the object into a dict
storage_volume_state_usage_dict = storage_volume_state_usage_instance.to_dict()
# create an instance of StorageVolumeStateUsage from a dict
storage_volume_state_usage_from_dict = StorageVolumeStateUsage.from_dict(storage_volume_state_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


