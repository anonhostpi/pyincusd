# ResourcesCPUCore

ResourcesCPUCore represents a CPU core on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core** | **int** | Core identifier within the socket | [optional] 
**die** | **int** | What die the CPU is a part of (for chiplet designs) | [optional] 
**flags** | **List[str]** | List of CPU flags | [optional] 
**frequency** | **int** | Current frequency | [optional] 
**threads** | [**List[ResourcesCPUThread]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ResourcesCPUThread.md) | List of threads | [optional] 

## Example

```python
from pyincusd.models.resources_cpu_core import ResourcesCPUCore

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesCPUCore from a JSON string
resources_cpu_core_instance = ResourcesCPUCore.from_json(json)
# print the JSON string representation of the object
print(ResourcesCPUCore.to_json())

# convert the object into a dict
resources_cpu_core_dict = resources_cpu_core_instance.to_dict()
# create an instance of ResourcesCPUCore from a dict
resources_cpu_core_from_dict = ResourcesCPUCore.from_dict(resources_cpu_core_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


