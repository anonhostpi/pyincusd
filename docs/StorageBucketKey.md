# StorageBucketKey

StorageBucketKey represents the fields of a storage pool bucket key

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
from pyincusd.models.storage_bucket_key import StorageBucketKey

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBucketKey from a JSON string
storage_bucket_key_instance = StorageBucketKey.from_json(json)
# print the JSON string representation of the object
print(StorageBucketKey.to_json())

# convert the object into a dict
storage_bucket_key_dict = storage_bucket_key_instance.to_dict()
# create an instance of StorageBucketKey from a dict
storage_bucket_key_from_dict = StorageBucketKey.from_dict(storage_bucket_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


