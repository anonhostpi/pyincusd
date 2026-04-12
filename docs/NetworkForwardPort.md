# NetworkForwardPort

NetworkForwardPort represents a port specification in a network address forward

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the forward port | [optional] 
**listen_port** | **str** | ListenPort(s) to forward (comma delimited ranges) | [optional] 
**protocol** | **str** | Protocol for port forward (either tcp or udp) | [optional] 
**snat** | **bool** | SNAT controls whether to apply a matching SNAT rule to new outgoing traffic from the target | [optional] 
**target_address** | **str** | TargetAddress to forward ListenPorts to | [optional] 
**target_port** | **str** | TargetPort(s) to forward ListenPorts to (allows for many-to-one) | [optional] 

## Example

```python
from pyincusd.models.network_forward_port import NetworkForwardPort

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkForwardPort from a JSON string
network_forward_port_instance = NetworkForwardPort.from_json(json)
# print the JSON string representation of the object
print(NetworkForwardPort.to_json())

# convert the object into a dict
network_forward_port_dict = network_forward_port_instance.to_dict()
# create an instance of NetworkForwardPort from a dict
network_forward_port_from_dict = NetworkForwardPort.from_dict(network_forward_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


