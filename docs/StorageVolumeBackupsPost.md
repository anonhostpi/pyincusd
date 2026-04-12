# StorageVolumeBackupsPost

StorageVolumeBackupsPost represents the fields available for a new volume backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression_algorithm** | **str** | What compression algorithm to use | [optional] 
**expires_at** | **datetime** | When the backup expires (gets auto-deleted) | [optional] 
**name** | **str** | Backup name | [optional] 
**optimized_storage** | **bool** | Whether to use a pool-optimized binary format (instead of plain tarball) | [optional] 
**target** | [**BackupTarget**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post7/docs/BackupTarget.md) |  | [optional] 
**volume_only** | **bool** | Whether to ignore snapshots | [optional] 

## Example

```python
from pyincusd.models.storage_volume_backups_post import StorageVolumeBackupsPost

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolumeBackupsPost from a JSON string
storage_volume_backups_post_instance = StorageVolumeBackupsPost.from_json(json)
# print the JSON string representation of the object
print(StorageVolumeBackupsPost.to_json())

# convert the object into a dict
storage_volume_backups_post_dict = storage_volume_backups_post_instance.to_dict()
# create an instance of StorageVolumeBackupsPost from a dict
storage_volume_backups_post_from_dict = StorageVolumeBackupsPost.from_dict(storage_volume_backups_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


