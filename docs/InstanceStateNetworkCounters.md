# InstanceStateNetworkCounters

InstanceStateNetworkCounters represents packet counters as part of the network section of an instance's state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_received** | **int** | Number of bytes received | [optional] 
**bytes_sent** | **int** | Number of bytes sent | [optional] 
**errors_received** | **int** | Number of errors received | [optional] 
**errors_sent** | **int** | Number of errors sent | [optional] 
**packets_dropped_inbound** | **int** | Number of inbound packets dropped | [optional] 
**packets_dropped_outbound** | **int** | Number of outbound packets dropped | [optional] 
**packets_received** | **int** | Number of packets received | [optional] 
**packets_sent** | **int** | Number of packets sent | [optional] 

## Example

```python
from pyincusd.models.instance_state_network_counters import InstanceStateNetworkCounters

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStateNetworkCounters from a JSON string
instance_state_network_counters_instance = InstanceStateNetworkCounters.from_json(json)
# print the JSON string representation of the object
print(InstanceStateNetworkCounters.to_json())

# convert the object into a dict
instance_state_network_counters_dict = instance_state_network_counters_instance.to_dict()
# create an instance of InstanceStateNetworkCounters from a dict
instance_state_network_counters_from_dict = InstanceStateNetworkCounters.from_dict(instance_state_network_counters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


