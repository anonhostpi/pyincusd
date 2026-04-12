# StorageVolumeSnapshotPut

StorageVolumeSnapshotPut represents the modifiable fields of a storage volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the storage volume | [optional] 
**expires_at** | **datetime** | When the snapshot expires (gets auto-deleted) | [optional] 

## Example

```python
from pyincusd.models.storage_volume_snapshot_put import StorageVolumeSnapshotPut

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolumeSnapshotPut from a JSON string
storage_volume_snapshot_put_instance = StorageVolumeSnapshotPut.from_json(json)
# print the JSON string representation of the object
print(StorageVolumeSnapshotPut.to_json())

# convert the object into a dict
storage_volume_snapshot_put_dict = storage_volume_snapshot_put_instance.to_dict()
# create an instance of StorageVolumeSnapshotPut from a dict
storage_volume_snapshot_put_from_dict = StorageVolumeSnapshotPut.from_dict(storage_volume_snapshot_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


