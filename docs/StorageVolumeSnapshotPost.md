# StorageVolumeSnapshotPost

StorageVolumeSnapshotPost represents the fields required to rename/move a storage volume snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration** | **bool** | Initiate volume snapshot migration | [optional] 
**name** | **str** | New snapshot name | [optional] 
**target** | [**StorageVolumePostTarget**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/StorageVolumePostTarget.md) |  | [optional] 

## Example

```python
from pyincusd.models.storage_volume_snapshot_post import StorageVolumeSnapshotPost

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolumeSnapshotPost from a JSON string
storage_volume_snapshot_post_instance = StorageVolumeSnapshotPost.from_json(json)
# print the JSON string representation of the object
print(StorageVolumeSnapshotPost.to_json())

# convert the object into a dict
storage_volume_snapshot_post_dict = storage_volume_snapshot_post_instance.to_dict()
# create an instance of StorageVolumeSnapshotPost from a dict
storage_volume_snapshot_post_from_dict = StorageVolumeSnapshotPost.from_dict(storage_volume_snapshot_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


