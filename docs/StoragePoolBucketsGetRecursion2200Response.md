# StoragePoolBucketsGetRecursion2200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[StorageBucketFull]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/StorageBucketFull.md) | List of storage pool buckets | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.storage_pool_buckets_get_recursion2200_response import StoragePoolBucketsGetRecursion2200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolBucketsGetRecursion2200Response from a JSON string
storage_pool_buckets_get_recursion2200_response_instance = StoragePoolBucketsGetRecursion2200Response.from_json(json)
# print the JSON string representation of the object
print(StoragePoolBucketsGetRecursion2200Response.to_json())

# convert the object into a dict
storage_pool_buckets_get_recursion2200_response_dict = storage_pool_buckets_get_recursion2200_response_instance.to_dict()
# create an instance of StoragePoolBucketsGetRecursion2200Response from a dict
storage_pool_buckets_get_recursion2200_response_from_dict = StoragePoolBucketsGetRecursion2200Response.from_dict(storage_pool_buckets_get_recursion2200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


