# ResourcesCPU

ResourcesCPU represents the cpu resources available on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | Architecture name | [optional] 
**sockets** | [**List[ResourcesCPUSocket]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post15/docs/ResourcesCPUSocket.md) | List of CPU sockets | [optional] 
**total** | **int** | Total number of CPU threads (from all sockets and cores) | [optional] 

## Example

```python
from pyincusd.models.resources_cpu import ResourcesCPU

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesCPU from a JSON string
resources_cpu_instance = ResourcesCPU.from_json(json)
# print the JSON string representation of the object
print(ResourcesCPU.to_json())

# convert the object into a dict
resources_cpu_dict = resources_cpu_instance.to_dict()
# create an instance of ResourcesCPU from a dict
resources_cpu_from_dict = ResourcesCPU.from_dict(resources_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


