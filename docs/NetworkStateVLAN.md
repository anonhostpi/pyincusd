# NetworkStateVLAN

NetworkStateVLAN represents VLAN specific state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lower_device** | **str** | Parent device | [optional] 
**vid** | **int** | VLAN ID | [optional] 

## Example

```python
from pyincusd.models.network_state_vlan import NetworkStateVLAN

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkStateVLAN from a JSON string
network_state_vlan_instance = NetworkStateVLAN.from_json(json)
# print the JSON string representation of the object
print(NetworkStateVLAN.to_json())

# convert the object into a dict
network_state_vlan_dict = network_state_vlan_instance.to_dict()
# create an instance of NetworkStateVLAN from a dict
network_state_vlan_from_dict = NetworkStateVLAN.from_dict(network_state_vlan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


