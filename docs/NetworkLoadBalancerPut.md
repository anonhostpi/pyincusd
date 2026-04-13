# NetworkLoadBalancerPut

NetworkLoadBalancerPut represents the modifiable fields of a network load balancer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backends** | [**List[NetworkLoadBalancerBackend]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancerBackend.md) | Backends (optional) | [optional] 
**config** | **object** | Load balancer configuration map (refer to doc/network-load-balancers.md) | [optional] 
**description** | **str** | Description of the load balancer listen IP | [optional] 
**ports** | [**List[NetworkLoadBalancerPort]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkLoadBalancerPort.md) | Port forwards (optional) | [optional] 

## Example

```python
from pyincusd.models.network_load_balancer_put import NetworkLoadBalancerPut

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancerPut from a JSON string
network_load_balancer_put_instance = NetworkLoadBalancerPut.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancerPut.to_json())

# convert the object into a dict
network_load_balancer_put_dict = network_load_balancer_put_instance.to_dict()
# create an instance of NetworkLoadBalancerPut from a dict
network_load_balancer_put_from_dict = NetworkLoadBalancerPut.from_dict(network_load_balancer_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


