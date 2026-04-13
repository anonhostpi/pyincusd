# StoragePoolState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inodes** | [**ResourcesStoragePoolInodes**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ResourcesStoragePoolInodes.md) |  | [optional] 
**space** | [**ResourcesStoragePoolSpace**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ResourcesStoragePoolSpace.md) |  | [optional] 

## Example

```python
from pyincusd.models.storage_pool_state import StoragePoolState

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolState from a JSON string
storage_pool_state_instance = StoragePoolState.from_json(json)
# print the JSON string representation of the object
print(StoragePoolState.to_json())

# convert the object into a dict
storage_pool_state_dict = storage_pool_state_instance.to_dict()
# create an instance of StoragePoolState from a dict
storage_pool_state_from_dict = StoragePoolState.from_dict(storage_pool_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


