# InstanceStateCPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_time** | **int** | CPU time available per second, in nanoseconds | [optional] 
**usage** | **int** | CPU usage in nanoseconds | [optional] 

## Example

```python
from pyincusd.models.instance_state_cpu import InstanceStateCPU

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStateCPU from a JSON string
instance_state_cpu_instance = InstanceStateCPU.from_json(json)
# print the JSON string representation of the object
print(InstanceStateCPU.to_json())

# convert the object into a dict
instance_state_cpu_dict = instance_state_cpu_instance.to_dict()
# create an instance of InstanceStateCPU from a dict
instance_state_cpu_from_dict = InstanceStateCPU.from_dict(instance_state_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


