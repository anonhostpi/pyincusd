# StoragePoolPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Storage pool configuration map (refer to doc/storage.md) | [optional] 
**description** | **str** | Description of the storage pool | [optional] 

## Example

```python
from pyincusd.models.storage_pool_put import StoragePoolPut

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolPut from a JSON string
storage_pool_put_instance = StoragePoolPut.from_json(json)
# print the JSON string representation of the object
print(StoragePoolPut.to_json())

# convert the object into a dict
storage_pool_put_dict = storage_pool_put_instance.to_dict()
# create an instance of StoragePoolPut from a dict
storage_pool_put_from_dict = StoragePoolPut.from_dict(storage_pool_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


