# NetworkLoadBalancerState

NetworkLoadBalancerState is used for showing current state of a load balancer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend_health** | [**Dict[str, NetworkLoadBalancerStateBackendHealth]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkLoadBalancerStateBackendHealth.md) |  | [optional] 

## Example

```python
from pyincusd.models.network_load_balancer_state import NetworkLoadBalancerState

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerState from a JSON string
network_load_balancer_state_instance = NetworkLoadBalancerState.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerState.to_json())

# convert the object into a dict
network_load_balancer_state_dict = network_load_balancer_state_instance.to_dict()
# create an instance of NetworkLoadBalancerState from a dict
network_load_balancer_state_from_dict = NetworkLoadBalancerState.from_dict(network_load_balancer_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


