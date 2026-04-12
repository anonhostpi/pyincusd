# NetworkAllocations

NetworkAllocations used for displaying network addresses used by a consuming entity e.g, instance, network forward, load-balancer, network...

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **str** | The network address of the allocation (in CIDR format) | [optional] 
**hwaddr** | **str** | Hwaddr is the MAC address of the entity consuming the network address | [optional] 
**nat** | **bool** | Whether the entity comes from a network that performs egress source NAT | [optional] 
**type** | **str** | Type of the entity consuming the network address | [optional] 
**used_by** | **str** | Name of the entity consuming the network address | [optional] 

## Example

```python
from pyincusd.models.network_allocations import NetworkAllocations

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAllocations from a JSON string
network_allocations_instance = NetworkAllocations.from_json(json)
# print the JSON string representation of the object
print(NetworkAllocations.to_json())

# convert the object into a dict
network_allocations_dict = network_allocations_instance.to_dict()
# create an instance of NetworkAllocations from a dict
network_allocations_from_dict = NetworkAllocations.from_dict(network_allocations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


