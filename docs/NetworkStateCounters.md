# NetworkStateCounters

NetworkStateCounters represents packet counters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_received** | **int** | Number of bytes received | [optional] 
**bytes_sent** | **int** | Number of bytes sent | [optional] 
**packets_received** | **int** | Number of packets received | [optional] 
**packets_sent** | **int** | Number of packets sent | [optional] 

## Example

```python
from pyincusd.models.network_state_counters import NetworkStateCounters

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkStateCounters from a JSON string
network_state_counters_instance = NetworkStateCounters.from_json(json)
# print the JSON string representation of the object
print(NetworkStateCounters.to_json())

# convert the object into a dict
network_state_counters_dict = network_state_counters_instance.to_dict()
# create an instance of NetworkStateCounters from a dict
network_state_counters_from_dict = NetworkStateCounters.from_dict(network_state_counters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


