# InstanceStateNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[InstanceStateNetworkAddress]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/InstanceStateNetworkAddress.md) | List of IP addresses | [optional] 
**counters** | [**InstanceStateNetworkCounters**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/InstanceStateNetworkCounters.md) |  | [optional] 
**host_name** | **str** | Name of the interface on the host | [optional] 
**hwaddr** | **str** | MAC address | [optional] 
**mtu** | **int** | MTU (maximum transmit unit) for the interface | [optional] 
**state** | **str** | Administrative state of the interface (up/down) | [optional] 
**type** | **str** | Type of interface (broadcast, loopback, point-to-point, ...) | [optional] 

## Example

```python
from pyincusd.models.instance_state_network import InstanceStateNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStateNetwork from a JSON string
instance_state_network_instance = InstanceStateNetwork.from_json(json)
# print the JSON string representation of the object
print(InstanceStateNetwork.to_json())

# convert the object into a dict
instance_state_network_dict = instance_state_network_instance.to_dict()
# create an instance of InstanceStateNetwork from a dict
instance_state_network_from_dict = InstanceStateNetwork.from_dict(instance_state_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


