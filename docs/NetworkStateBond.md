# NetworkStateBond

NetworkStateBond represents bond specific state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**down_delay** | **int** | Delay on link down (ms) | [optional] 
**lower_devices** | **List[str]** | List of devices that are part of the bond | [optional] 
**mii_frequency** | **int** | How often to check for link state (ms) | [optional] 
**mii_state** | **str** | Bond link state | [optional] 
**mode** | **str** | Bonding mode | [optional] 
**transmit_policy** | **str** | Transmit balancing policy | [optional] 
**up_delay** | **int** | Delay on link up (ms) | [optional] 

## Example

```python
from pyincusd.models.network_state_bond import NetworkStateBond

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkStateBond from a JSON string
network_state_bond_instance = NetworkStateBond.from_json(json)
# print the JSON string representation of the object
print(NetworkStateBond.to_json())

# convert the object into a dict
network_state_bond_dict = network_state_bond_instance.to_dict()
# create an instance of NetworkStateBond from a dict
network_state_bond_from_dict = NetworkStateBond.from_dict(network_state_bond_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


