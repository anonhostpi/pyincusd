# InstanceStateMemory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**swap_usage** | **int** | SWAP usage in bytes | [optional] 
**swap_usage_peak** | **int** | Peak SWAP usage in bytes | [optional] 
**total** | **int** | Total memory size in bytes | [optional] 
**usage** | **int** | Memory usage in bytes | [optional] 
**usage_peak** | **int** | Peak memory usage in bytes | [optional] 

## Example

```python
from pyincusd.models.instance_state_memory import InstanceStateMemory

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStateMemory from a JSON string
instance_state_memory_instance = InstanceStateMemory.from_json(json)
# print the JSON string representation of the object
print(InstanceStateMemory.to_json())

# convert the object into a dict
instance_state_memory_dict = instance_state_memory_instance.to_dict()
# create an instance of InstanceStateMemory from a dict
instance_state_memory_from_dict = InstanceStateMemory.from_dict(instance_state_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


