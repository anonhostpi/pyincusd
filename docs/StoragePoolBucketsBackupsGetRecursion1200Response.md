# StoragePoolBucketsBackupsGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[StorageBucketBackup]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageBucketBackup.md) | List of storage bucket backups | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.storage_pool_buckets_backups_get_recursion1200_response import StoragePoolBucketsBackupsGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolBucketsBackupsGetRecursion1200Response from a JSON string
storage_pool_buckets_backups_get_recursion1200_response_instance = StoragePoolBucketsBackupsGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(StoragePoolBucketsBackupsGetRecursion1200Response.to_json())

# convert the object into a dict
storage_pool_buckets_backups_get_recursion1200_response_dict = storage_pool_buckets_backups_get_recursion1200_response_instance.to_dict()
# create an instance of StoragePoolBucketsBackupsGetRecursion1200Response from a dict
storage_pool_buckets_backups_get_recursion1200_response_from_dict = StoragePoolBucketsBackupsGetRecursion1200Response.from_dict(storage_pool_buckets_backups_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


