# StorageBucket

StorageBucket represents the fields of a storage pool bucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Storage bucket configuration map | [optional] 
**description** | **str** | Description of the storage bucket | [optional] 
**location** | **str** | What cluster member this record was found on | [optional] 
**name** | **str** | Bucket name | [optional] 
**project** | **str** | Project name | [optional] 
**s3_url** | **str** | Bucket S3 URL | [optional] 

## Example

```python
from pyincusd.models.storage_bucket import StorageBucket

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBucket from a JSON string
storage_bucket_instance = StorageBucket.from_json(json)
# print the JSON string representation of the object
print(StorageBucket.to_json())

# convert the object into a dict
storage_bucket_dict = storage_bucket_instance.to_dict()
# create an instance of StorageBucket from a dict
storage_bucket_from_dict = StorageBucket.from_dict(storage_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


