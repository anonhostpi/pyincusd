# ResourcesStoragePool

ResourcesStoragePool represents the resources available to a given storage pool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inodes** | [**ResourcesStoragePoolInodes**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ResourcesStoragePoolInodes.md) |  | [optional] 
**space** | [**ResourcesStoragePoolSpace**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/ResourcesStoragePoolSpace.md) |  | [optional] 

## Example

```python
from pyincusd.models.resources_storage_pool import ResourcesStoragePool

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesStoragePool from a JSON string
resources_storage_pool_instance = ResourcesStoragePool.from_json(json)
# print the JSON string representation of the object
print(ResourcesStoragePool.to_json())

# convert the object into a dict
resources_storage_pool_dict = resources_storage_pool_instance.to_dict()
# create an instance of ResourcesStoragePool from a dict
resources_storage_pool_from_dict = ResourcesStoragePool.from_dict(resources_storage_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


