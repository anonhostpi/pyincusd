# ResourcesNetworkCardPort

ResourcesNetworkCardPort represents a network port on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | MAC address | [optional] 
**auto_negotiation** | **bool** | Whether auto negotiation is used | [optional] 
**id** | **str** | Port identifier (interface name) | [optional] 
**infiniband** | [**ResourcesNetworkCardPortInfiniband**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ResourcesNetworkCardPortInfiniband.md) |  | [optional] 
**link_detected** | **bool** | Whether a link was detected | [optional] 
**link_duplex** | **str** | Duplex type | [optional] 
**link_speed** | **int** | Current speed (Mbit/s) | [optional] 
**port** | **int** | Port number | [optional] 
**port_type** | **str** | Current port type | [optional] 
**protocol** | **str** | Transport protocol | [optional] 
**supported_modes** | **List[str]** | List of supported modes | [optional] 
**supported_ports** | **List[str]** | List of supported port types | [optional] 
**transceiver_type** | **str** | Type of transceiver used | [optional] 

## Example

```python
from pyincusd.models.resources_network_card_port import ResourcesNetworkCardPort

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesNetworkCardPort from a JSON string
resources_network_card_port_instance = ResourcesNetworkCardPort.from_json(json)
# print the JSON string representation of the object
print(ResourcesNetworkCardPort.to_json())

# convert the object into a dict
resources_network_card_port_dict = resources_network_card_port_instance.to_dict()
# create an instance of ResourcesNetworkCardPort from a dict
resources_network_card_port_from_dict = ResourcesNetworkCardPort.from_dict(resources_network_card_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


