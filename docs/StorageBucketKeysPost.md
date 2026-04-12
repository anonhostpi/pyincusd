# StorageBucketKeysPost

StorageBucketKeysPost represents the fields of a new storage pool bucket key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | Access key | [optional] 
**description** | **str** | Description of the storage bucket key | [optional] 
**name** | **str** | Key name | [optional] 
**role** | **str** | Whether the key can perform write actions or not. | [optional] 
**secret_key** | **str** | Secret key | [optional] 

## Example

```python
from pyincusd.models.storage_bucket_keys_post import StorageBucketKeysPost

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBucketKeysPost from a JSON string
storage_bucket_keys_post_instance = StorageBucketKeysPost.from_json(json)
# print the JSON string representation of the object
print(StorageBucketKeysPost.to_json())

# convert the object into a dict
storage_bucket_keys_post_dict = storage_bucket_keys_post_instance.to_dict()
# create an instance of StorageBucketKeysPost from a dict
storage_bucket_keys_post_from_dict = StorageBucketKeysPost.from_dict(storage_bucket_keys_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


