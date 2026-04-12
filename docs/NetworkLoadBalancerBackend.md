# NetworkLoadBalancerBackend

NetworkLoadBalancerBackend represents a target backend specification in a network load balancer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the load balancer backend | [optional] 
**name** | **str** | Name of the load balancer backend | [optional] 
**target_address** | **str** | TargetAddress to forward ListenPorts to | [optional] 
**target_port** | **str** | TargetPort(s) to forward ListenPorts to (allows for many-to-one) | [optional] 

## Example

```python
from pyincusd.models.network_load_balancer_backend import NetworkLoadBalancerBackend

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerBackend from a JSON string
network_load_balancer_backend_instance = NetworkLoadBalancerBackend.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerBackend.to_json())

# convert the object into a dict
network_load_balancer_backend_dict = network_load_balancer_backend_instance.to_dict()
# create an instance of NetworkLoadBalancerBackend from a dict
network_load_balancer_backend_from_dict = NetworkLoadBalancerBackend.from_dict(network_load_balancer_backend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


