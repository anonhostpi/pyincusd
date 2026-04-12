# ResourcesStoragePoolSpace

ResourcesStoragePoolSpace represents the space available to a given storage pool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total disk space (bytes) | [optional] 
**used** | **int** | Used disk space (bytes) | [optional] 

## Example

```python
from pyincusd.models.resources_storage_pool_space import ResourcesStoragePoolSpace

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesStoragePoolSpace from a JSON string
resources_storage_pool_space_instance = ResourcesStoragePoolSpace.from_json(json)
# print the JSON string representation of the object
print(ResourcesStoragePoolSpace.to_json())

# convert the object into a dict
resources_storage_pool_space_dict = resources_storage_pool_space_instance.to_dict()
# create an instance of ResourcesStoragePoolSpace from a dict
resources_storage_pool_space_from_dict = ResourcesStoragePoolSpace.from_dict(resources_storage_pool_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


