# NetworkLoadBalancersPost

NetworkLoadBalancersPost represents the fields of a new network load balancer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backends** | [**List[NetworkLoadBalancerBackend]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post19/docs/NetworkLoadBalancerBackend.md) | Backends (optional) | [optional] 
**config** | **object** | Load balancer configuration map (refer to doc/network-load-balancers.md) | [optional] 
**description** | **str** | Description of the load balancer listen IP | [optional] 
**listen_address** | **str** | The listen address of the load balancer | [optional] 
**ports** | [**List[NetworkLoadBalancerPort]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post19/docs/NetworkLoadBalancerPort.md) | Port forwards (optional) | [optional] 

## Example

```python
from pyincusd.models.network_load_balancers_post import NetworkLoadBalancersPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLoadBalancersPost from a JSON string
network_load_balancers_post_instance = NetworkLoadBalancersPost.from_json(json)
# print the JSON string representation of the object
print(NetworkLoadBalancersPost.to_json())

# convert the object into a dict
network_load_balancers_post_dict = network_load_balancers_post_instance.to_dict()
# create an instance of NetworkLoadBalancersPost from a dict
network_load_balancers_post_from_dict = NetworkLoadBalancersPost.from_dict(network_load_balancers_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


