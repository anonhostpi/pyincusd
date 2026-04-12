# ResourcesNetworkCardPortInfiniband

ResourcesNetworkCardPortInfiniband represents the Linux Infiniband configuration for the port

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issm_device** | **str** | ISSM device number | [optional] 
**issm_name** | **str** | ISSM device name | [optional] 
**mad_device** | **str** | MAD device number | [optional] 
**mad_name** | **str** | MAD device name | [optional] 
**verb_device** | **str** | Verb device number | [optional] 
**verb_name** | **str** | Verb device name | [optional] 

## Example

```python
from pyincusd.models.resources_network_card_port_infiniband import ResourcesNetworkCardPortInfiniband

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesNetworkCardPortInfiniband from a JSON string
resources_network_card_port_infiniband_instance = ResourcesNetworkCardPortInfiniband.from_json(json)
# print the JSON string representation of the object
print(ResourcesNetworkCardPortInfiniband.to_json())

# convert the object into a dict
resources_network_card_port_infiniband_dict = resources_network_card_port_infiniband_instance.to_dict()
# create an instance of ResourcesNetworkCardPortInfiniband from a dict
resources_network_card_port_infiniband_from_dict = ResourcesNetworkCardPortInfiniband.from_dict(resources_network_card_port_infiniband_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


