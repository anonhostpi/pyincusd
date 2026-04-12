# ResourcesCPUCache

ResourcesCPUCache represents a CPU cache

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** | Cache level (usually a number from 1 to 3) | [optional] 
**size** | **int** | Size of the cache (in bytes) | [optional] 
**type** | **str** | Type of cache (Data, Instruction, Unified, ...) | [optional] 

## Example

```python
from pyincusd.models.resources_cpu_cache import ResourcesCPUCache

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesCPUCache from a JSON string
resources_cpu_cache_instance = ResourcesCPUCache.from_json(json)
# print the JSON string representation of the object
print(ResourcesCPUCache.to_json())

# convert the object into a dict
resources_cpu_cache_dict = resources_cpu_cache_instance.to_dict()
# create an instance of ResourcesCPUCache from a dict
resources_cpu_cache_from_dict = ResourcesCPUCache.from_dict(resources_cpu_cache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


