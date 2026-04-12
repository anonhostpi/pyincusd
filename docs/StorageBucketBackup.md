# StorageBucketBackup

StorageBucketBackup represents the fields available for a new storage bucket backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | When the backup was created | [optional] 
**expires_at** | **datetime** | When the backup expires (gets auto-deleted) | [optional] 
**name** | **str** | Backup name | [optional] 

## Example

```python
from pyincusd.models.storage_bucket_backup import StorageBucketBackup

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBucketBackup from a JSON string
storage_bucket_backup_instance = StorageBucketBackup.from_json(json)
# print the JSON string representation of the object
print(StorageBucketBackup.to_json())

# convert the object into a dict
storage_bucket_backup_dict = storage_bucket_backup_instance.to_dict()
# create an instance of StorageBucketBackup from a dict
storage_bucket_backup_from_dict = StorageBucketBackup.from_dict(storage_bucket_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


