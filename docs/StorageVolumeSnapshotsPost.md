# StorageVolumeSnapshotsPost

StorageVolumeSnapshotsPost represents the fields available for a new storage volume snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | When the snapshot expires (gets auto-deleted) | [optional] 
**name** | **str** | Snapshot name | [optional] 

## Example

```python
from pyincusd.models.storage_volume_snapshots_post import StorageVolumeSnapshotsPost

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolumeSnapshotsPost from a JSON string
storage_volume_snapshots_post_instance = StorageVolumeSnapshotsPost.from_json(json)
# print the JSON string representation of the object
print(StorageVolumeSnapshotsPost.to_json())

# convert the object into a dict
storage_volume_snapshots_post_dict = storage_volume_snapshots_post_instance.to_dict()
# create an instance of StorageVolumeSnapshotsPost from a dict
storage_volume_snapshots_post_from_dict = StorageVolumeSnapshotsPost.from_dict(storage_volume_snapshots_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


