# NetworkLoadBalancerStateBackendHealthPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** |  | [optional] 
**protocol** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pyincusd.models.network_load_balancer_state_backend_health_port import NetworkLoadBalancerStateBackendHealthPort

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerStateBackendHealthPort from a JSON string
network_load_balancer_state_backend_health_port_instance = NetworkLoadBalancerStateBackendHealthPort.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerStateBackendHealthPort.to_json())

# convert the object into a dict
network_load_balancer_state_backend_health_port_dict = network_load_balancer_state_backend_health_port_instance.to_dict()
# create an instance of NetworkLoadBalancerStateBackendHealthPort from a dict
network_load_balancer_state_backend_health_port_from_dict = NetworkLoadBalancerStateBackendHealthPort.from_dict(network_load_balancer_state_backend_health_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


