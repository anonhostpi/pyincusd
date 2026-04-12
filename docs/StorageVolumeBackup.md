# StorageVolumeBackup

StorageVolumeBackup represents a volume backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | When the backup was created | [optional] 
**expires_at** | **datetime** | When the backup expires (gets auto-deleted) | [optional] 
**name** | **str** | Backup name | [optional] 
**optimized_storage** | **bool** | Whether to use a pool-optimized binary format (instead of plain tarball) | [optional] 
**volume_only** | **bool** | Whether to ignore snapshots | [optional] 

## Example

```python
from pyincusd.models.storage_volume_backup import StorageVolumeBackup

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolumeBackup from a JSON string
storage_volume_backup_instance = StorageVolumeBackup.from_json(json)
# print the JSON string representation of the object
print(StorageVolumeBackup.to_json())

# convert the object into a dict
storage_volume_backup_dict = storage_volume_backup_instance.to_dict()
# create an instance of StorageVolumeBackup from a dict
storage_volume_backup_from_dict = StorageVolumeBackup.from_dict(storage_volume_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


