# ResourcesMemoryNode

ResourcesMemoryNode represents the node-specific memory resources available on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hugepages_total** | **int** | Total of memory huge pages (bytes) | [optional] 
**hugepages_used** | **int** | Used memory huge pages (bytes) | [optional] 
**numa_node** | **int** | NUMA node identifier | [optional] 
**total** | **int** | Total system memory (bytes) | [optional] 
**used** | **int** | Used system memory (bytes) | [optional] 

## Example

```python
from pyincusd.models.resources_memory_node import ResourcesMemoryNode

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesMemoryNode from a JSON string
resources_memory_node_instance = ResourcesMemoryNode.from_json(json)
# print the JSON string representation of the object
print(ResourcesMemoryNode.to_json())

# convert the object into a dict
resources_memory_node_dict = resources_memory_node_instance.to_dict()
# create an instance of ResourcesMemoryNode from a dict
resources_memory_node_from_dict = ResourcesMemoryNode.from_dict(resources_memory_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


