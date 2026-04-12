# StoragePoolBucketsGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[StorageBucket]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/StorageBucket.md) | List of storage pool buckets | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.storage_pool_buckets_get_recursion1200_response import StoragePoolBucketsGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolBucketsGetRecursion1200Response from a JSON string
storage_pool_buckets_get_recursion1200_response_instance = StoragePoolBucketsGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(StoragePoolBucketsGetRecursion1200Response.to_json())

# convert the object into a dict
storage_pool_buckets_get_recursion1200_response_dict = storage_pool_buckets_get_recursion1200_response_instance.to_dict()
# create an instance of StoragePoolBucketsGetRecursion1200Response from a dict
storage_pool_buckets_get_recursion1200_response_from_dict = StoragePoolBucketsGetRecursion1200Response.from_dict(storage_pool_buckets_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


