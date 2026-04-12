# StorageBucketBackupPost

StorageBucketBackupPost represents the fields available for the renaming of a bucket backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New backup name | [optional] 

## Example

```python
from pyincusd.models.storage_bucket_backup_post import StorageBucketBackupPost

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBucketBackupPost from a JSON string
storage_bucket_backup_post_instance = StorageBucketBackupPost.from_json(json)
# print the JSON string representation of the object
print(StorageBucketBackupPost.to_json())

# convert the object into a dict
storage_bucket_backup_post_dict = storage_bucket_backup_post_instance.to_dict()
# create an instance of StorageBucketBackupPost from a dict
storage_bucket_backup_post_from_dict = StorageBucketBackupPost.from_dict(storage_bucket_backup_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


