# StoragePoolResources200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ResourcesStoragePool**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post7/docs/ResourcesStoragePool.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.storage_pool_resources200_response import StoragePoolResources200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolResources200Response from a JSON string
storage_pool_resources200_response_instance = StoragePoolResources200Response.from_json(json)
# print the JSON string representation of the object
print(StoragePoolResources200Response.to_json())

# convert the object into a dict
storage_pool_resources200_response_dict = storage_pool_resources200_response_instance.to_dict()
# create an instance of StoragePoolResources200Response from a dict
storage_pool_resources200_response_from_dict = StoragePoolResources200Response.from_dict(storage_pool_resources200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


