# StorageBucketBackupsPost

StorageBucketBackupsPost represents the fields available for a new storage bucket backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression_algorithm** | **str** | What compression algorithm to use | [optional] 
**expires_at** | **datetime** | When the backup expires (gets auto-deleted) | [optional] 
**name** | **str** | Backup name | [optional] 

## Example

```python
from pyincusd.models.storage_bucket_backups_post import StorageBucketBackupsPost

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBucketBackupsPost from a JSON string
storage_bucket_backups_post_instance = StorageBucketBackupsPost.from_json(json)
# print the JSON string representation of the object
print(StorageBucketBackupsPost.to_json())

# convert the object into a dict
storage_bucket_backups_post_dict = storage_bucket_backups_post_instance.to_dict()
# create an instance of StorageBucketBackupsPost from a dict
storage_bucket_backups_post_from_dict = StorageBucketBackupsPost.from_dict(storage_bucket_backups_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


