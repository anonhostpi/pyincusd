# StoragePoolGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**StoragePool**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post4/docs/StoragePool.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.storage_pool_get200_response import StoragePoolGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolGet200Response from a JSON string
storage_pool_get200_response_instance = StoragePoolGet200Response.from_json(json)
# print the JSON string representation of the object
print(StoragePoolGet200Response.to_json())

# convert the object into a dict
storage_pool_get200_response_dict = storage_pool_get200_response_instance.to_dict()
# create an instance of StoragePoolGet200Response from a dict
storage_pool_get200_response_from_dict = StoragePoolGet200Response.from_dict(storage_pool_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


