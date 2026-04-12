# NetworkState

NetworkState represents the network state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[NetworkStateAddress]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/NetworkStateAddress.md) | List of addresses | [optional] 
**bond** | [**NetworkStateBond**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/NetworkStateBond.md) |  | [optional] 
**bridge** | [**NetworkStateBridge**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/NetworkStateBridge.md) |  | [optional] 
**counters** | [**NetworkStateCounters**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/NetworkStateCounters.md) |  | [optional] 
**hwaddr** | **str** | MAC address | [optional] 
**mtu** | **int** | MTU | [optional] 
**ovn** | [**NetworkStateOVN**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/NetworkStateOVN.md) |  | [optional] 
**state** | **str** | Link state | [optional] 
**type** | **str** | Interface type | [optional] 
**vlan** | [**NetworkStateVLAN**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/NetworkStateVLAN.md) |  | [optional] 

## Example

```python
from pyincusd.models.network_state import NetworkState

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkState from a JSON string
network_state_instance = NetworkState.from_json(json)
# print the JSON string representation of the object
print(NetworkState.to_json())

# convert the object into a dict
network_state_dict = network_state_instance.to_dict()
# create an instance of NetworkState from a dict
network_state_from_dict = NetworkState.from_dict(network_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


