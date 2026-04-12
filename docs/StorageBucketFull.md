# StorageBucketFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups** | [**List[StorageBucketBackup]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/StorageBucketBackup.md) | List of backups. | [optional] 
**config** | **object** | Storage bucket configuration map | [optional] 
**description** | **str** | Description of the storage bucket | [optional] 
**keys** | [**List[StorageBucketKey]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/StorageBucketKey.md) | List of keys. | [optional] 
**location** | **str** | What cluster member this record was found on | [optional] 
**name** | **str** | Bucket name | [optional] 
**project** | **str** | Project name | [optional] 
**s3_url** | **str** | Bucket S3 URL | [optional] 

## Example

```python
from pyincusd.models.storage_bucket_full import StorageBucketFull

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBucketFull from a JSON string
storage_bucket_full_instance = StorageBucketFull.from_json(json)
# print the JSON string representation of the object
print(StorageBucketFull.to_json())

# convert the object into a dict
storage_bucket_full_dict = storage_bucket_full_instance.to_dict()
# create an instance of StorageBucketFull from a dict
storage_bucket_full_from_dict = StorageBucketFull.from_dict(storage_bucket_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


