# StorageVolumeState

StorageVolumeState represents the live state of the volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | [**StorageVolumeStateUsage**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post4/docs/StorageVolumeStateUsage.md) |  | [optional] 

## Example

```python
from pyincusd.models.storage_volume_state import StorageVolumeState

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolumeState from a JSON string
storage_volume_state_instance = StorageVolumeState.from_json(json)
# print the JSON string representation of the object
print(StorageVolumeState.to_json())

# convert the object into a dict
storage_volume_state_dict = storage_volume_state_instance.to_dict()
# create an instance of StorageVolumeState from a dict
storage_volume_state_from_dict = StorageVolumeState.from_dict(storage_volume_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


