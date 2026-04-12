# StorageVolumePut

StorageVolumePut represents the modifiable fields of a storage volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Storage volume configuration map (refer to doc/storage.md) | [optional] 
**description** | **str** | Description of the storage volume | [optional] 
**restore** | **str** | Name of a snapshot to restore | [optional] 

## Example

```python
from pyincusd.models.storage_volume_put import StorageVolumePut

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolumePut from a JSON string
storage_volume_put_instance = StorageVolumePut.from_json(json)
# print the JSON string representation of the object
print(StorageVolumePut.to_json())

# convert the object into a dict
storage_volume_put_dict = storage_volume_put_instance.to_dict()
# create an instance of StorageVolumePut from a dict
storage_volume_put_from_dict = StorageVolumePut.from_dict(storage_volume_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


