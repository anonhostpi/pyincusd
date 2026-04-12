# NetworkLoadBalancerStateBackendHealth

NetworkLoadBalancerStateBackendHealth represents the health of a particular load-balancer backend

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**ports** | [**List[NetworkLoadBalancerStateBackendHealthPort]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/NetworkLoadBalancerStateBackendHealthPort.md) |  | [optional] 

## Example

```python
from pyincusd.models.network_load_balancer_state_backend_health import NetworkLoadBalancerStateBackendHealth

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerStateBackendHealth from a JSON string
network_load_balancer_state_backend_health_instance = NetworkLoadBalancerStateBackendHealth.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerStateBackendHealth.to_json())

# convert the object into a dict
network_load_balancer_state_backend_health_dict = network_load_balancer_state_backend_health_instance.to_dict()
# create an instance of NetworkLoadBalancerStateBackendHealth from a dict
network_load_balancer_state_backend_health_from_dict = NetworkLoadBalancerStateBackendHealth.from_dict(network_load_balancer_state_backend_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


