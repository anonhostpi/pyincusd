# StorageBucketPut

StorageBucketPut represents the modifiable fields of a storage pool bucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Storage bucket configuration map | [optional] 
**description** | **str** | Description of the storage bucket | [optional] 

## Example

```python
from pyincusd.models.storage_bucket_put import StorageBucketPut

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBucketPut from a JSON string
storage_bucket_put_instance = StorageBucketPut.from_json(json)
# print the JSON string representation of the object
print(StorageBucketPut.to_json())

# convert the object into a dict
storage_bucket_put_dict = storage_bucket_put_instance.to_dict()
# create an instance of StorageBucketPut from a dict
storage_bucket_put_from_dict = StorageBucketPut.from_dict(storage_bucket_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


