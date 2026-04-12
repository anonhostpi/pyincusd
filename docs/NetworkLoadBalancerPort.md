# NetworkLoadBalancerPort

NetworkLoadBalancerPort represents a port specification in a network load balancer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the load balancer port | [optional] 
**listen_port** | **str** | ListenPort(s) of load balancer (comma delimited ranges) | [optional] 
**protocol** | **str** | Protocol for load balancer port (either tcp or udp) | [optional] 
**target_backend** | **List[str]** | TargetBackend backend names to load balance ListenPorts to | [optional] 

## Example

```python
from pyincusd.models.network_load_balancer_port import NetworkLoadBalancerPort

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerPort from a JSON string
network_load_balancer_port_instance = NetworkLoadBalancerPort.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerPort.to_json())

# convert the object into a dict
network_load_balancer_port_dict = network_load_balancer_port_instance.to_dict()
# create an instance of NetworkLoadBalancerPort from a dict
network_load_balancer_port_from_dict = NetworkLoadBalancerPort.from_dict(network_load_balancer_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


