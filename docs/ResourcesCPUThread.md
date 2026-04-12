# ResourcesCPUThread

ResourcesCPUThread represents a CPU thread on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Thread ID (used for CPU pinning) | [optional] 
**isolated** | **bool** | Whether the thread has been isolated (outside of normal scheduling) | [optional] 
**numa_node** | **int** | NUMA node the thread is a part of | [optional] 
**online** | **bool** | Whether the thread is online (enabled) | [optional] 
**thread** | **int** | Thread identifier within the core | [optional] 

## Example

```python
from pyincusd.models.resources_cpu_thread import ResourcesCPUThread

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesCPUThread from a JSON string
resources_cpu_thread_instance = ResourcesCPUThread.from_json(json)
# print the JSON string representation of the object
print(ResourcesCPUThread.to_json())

# convert the object into a dict
resources_cpu_thread_dict = resources_cpu_thread_instance.to_dict()
# create an instance of ResourcesCPUThread from a dict
resources_cpu_thread_from_dict = ResourcesCPUThread.from_dict(resources_cpu_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


