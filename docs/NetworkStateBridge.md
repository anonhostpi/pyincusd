# NetworkStateBridge

NetworkStateBridge represents bridge specific state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forward_delay** | **int** | Delay on port join (ms) | [optional] 
**id** | **str** | Bridge ID | [optional] 
**stp** | **bool** | Whether STP is enabled | [optional] 
**upper_devices** | **List[str]** | List of devices that are in the bridge | [optional] 
**vlan_default** | **int** | Default VLAN ID | [optional] 
**vlan_filtering** | **bool** | Whether VLAN filtering is enabled | [optional] 

## Example

```python
from pyincusd.models.network_state_bridge import NetworkStateBridge

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkStateBridge from a JSON string
network_state_bridge_instance = NetworkStateBridge.from_json(json)
# print the JSON string representation of the object
print(NetworkStateBridge.to_json())

# convert the object into a dict
network_state_bridge_dict = network_state_bridge_instance.to_dict()
# create an instance of NetworkStateBridge from a dict
network_state_bridge_from_dict = NetworkStateBridge.from_dict(network_state_bridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


