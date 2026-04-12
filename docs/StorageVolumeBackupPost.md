# StorageVolumeBackupPost

StorageVolumeBackupPost represents the fields available for the renaming of a volume backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New backup name | [optional] 

## Example

```python
from pyincusd.models.storage_volume_backup_post import StorageVolumeBackupPost

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolumeBackupPost from a JSON string
storage_volume_backup_post_instance = StorageVolumeBackupPost.from_json(json)
# print the JSON string representation of the object
print(StorageVolumeBackupPost.to_json())

# convert the object into a dict
storage_volume_backup_post_dict = storage_volume_backup_post_instance.to_dict()
# create an instance of StorageVolumeBackupPost from a dict
storage_volume_backup_post_from_dict = StorageVolumeBackupPost.from_dict(storage_volume_backup_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


