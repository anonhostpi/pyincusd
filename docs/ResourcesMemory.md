# ResourcesMemory

ResourcesMemory represents the memory resources available on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hugepages_size** | **int** | Size of memory huge pages (bytes) | [optional] 
**hugepages_total** | **int** | Total of memory huge pages (bytes) | [optional] 
**hugepages_used** | **int** | Used memory huge pages (bytes) | [optional] 
**nodes** | [**List[ResourcesMemoryNode]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post15/docs/ResourcesMemoryNode.md) | List of NUMA memory nodes | [optional] 
**total** | **int** | Total system memory (bytes) | [optional] 
**used** | **int** | Used system memory (bytes) | [optional] 

## Example

```python
from pyincusd.models.resources_memory import ResourcesMemory

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesMemory from a JSON string
resources_memory_instance = ResourcesMemory.from_json(json)
# print the JSON string representation of the object
print(ResourcesMemory.to_json())

# convert the object into a dict
resources_memory_dict = resources_memory_instance.to_dict()
# create an instance of ResourcesMemory from a dict
resources_memory_from_dict = ResourcesMemory.from_dict(resources_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


