# ResourcesStoragePoolInodes

ResourcesStoragePoolInodes represents the inodes available to a given storage pool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total inodes | [optional] 
**used** | **int** | Used inodes | [optional] 

## Example

```python
from pyincusd.models.resources_storage_pool_inodes import ResourcesStoragePoolInodes

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesStoragePoolInodes from a JSON string
resources_storage_pool_inodes_instance = ResourcesStoragePoolInodes.from_json(json)
# print the JSON string representation of the object
print(ResourcesStoragePoolInodes.to_json())

# convert the object into a dict
resources_storage_pool_inodes_dict = resources_storage_pool_inodes_instance.to_dict()
# create an instance of ResourcesStoragePoolInodes from a dict
resources_storage_pool_inodes_from_dict = ResourcesStoragePoolInodes.from_dict(resources_storage_pool_inodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


