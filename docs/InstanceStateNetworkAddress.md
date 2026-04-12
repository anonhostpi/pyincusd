# InstanceStateNetworkAddress

InstanceStateNetworkAddress represents a network address as part of the network section of an instance's state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | IP address | [optional] 
**family** | **str** | Network family (inet or inet6) | [optional] 
**netmask** | **str** | Network mask | [optional] 
**scope** | **str** | Address scope (local, link or global) | [optional] 

## Example

```python
from pyincusd.models.instance_state_network_address import InstanceStateNetworkAddress

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStateNetworkAddress from a JSON string
instance_state_network_address_instance = InstanceStateNetworkAddress.from_json(json)
# print the JSON string representation of the object
print(InstanceStateNetworkAddress.to_json())

# convert the object into a dict
instance_state_network_address_dict = instance_state_network_address_instance.to_dict()
# create an instance of InstanceStateNetworkAddress from a dict
instance_state_network_address_from_dict = InstanceStateNetworkAddress.from_dict(instance_state_network_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


