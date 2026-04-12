# NetworkStateOVN

NetworkStateOVN represents OVN specific state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis** | **str** | OVN network chassis name | [optional] 
**logical_router** | **str** | OVN logical router name | [optional] 
**logical_switch** | **str** | OVN logical switch name | [optional] 
**uplink_ipv4** | **str** | OVN network uplink ipv4 address | [optional] 
**uplink_ipv6** | **str** | OVN network uplink ipv6 address | [optional] 

## Example

```python
from pyincusd.models.network_state_ovn import NetworkStateOVN

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkStateOVN from a JSON string
network_state_ovn_instance = NetworkStateOVN.from_json(json)
# print the JSON string representation of the object
print(NetworkStateOVN.to_json())

# convert the object into a dict
network_state_ovn_dict = network_state_ovn_instance.to_dict()
# create an instance of NetworkStateOVN from a dict
network_state_ovn_from_dict = NetworkStateOVN.from_dict(network_state_ovn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


