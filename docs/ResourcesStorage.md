# ResourcesStorage

ResourcesStorage represents the local storage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disks** | [**List[ResourcesStorageDisk]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ResourcesStorageDisk.md) | List of disks | [optional] 
**total** | **int** | Total number of partitions | [optional] 

## Example

```python
from pyincusd.models.resources_storage import ResourcesStorage

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesStorage from a JSON string
resources_storage_instance = ResourcesStorage.from_json(json)
# print the JSON string representation of the object
print(ResourcesStorage.to_json())

# convert the object into a dict
resources_storage_dict = resources_storage_instance.to_dict()
# create an instance of ResourcesStorage from a dict
resources_storage_from_dict = ResourcesStorage.from_dict(resources_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


