# StorageBucketsPost

StorageBucketsPost represents the fields of a new storage pool bucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Storage bucket configuration map | [optional] 
**description** | **str** | Description of the storage bucket | [optional] 
**name** | **str** | Bucket name | [optional] 

## Example

```python
from pyincusd.models.storage_buckets_post import StorageBucketsPost

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBucketsPost from a JSON string
storage_buckets_post_instance = StorageBucketsPost.from_json(json)
# print the JSON string representation of the object
print(StorageBucketsPost.to_json())

# convert the object into a dict
storage_buckets_post_dict = storage_buckets_post_instance.to_dict()
# create an instance of StorageBucketsPost from a dict
storage_buckets_post_from_dict = StorageBucketsPost.from_dict(storage_buckets_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


