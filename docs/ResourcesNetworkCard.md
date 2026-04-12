# ResourcesNetworkCard

ResourcesNetworkCard represents a network card on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | Kernel driver currently associated with the card | [optional] 
**driver_version** | **str** | Version of the kernel driver | [optional] 
**firmware_version** | **str** | Current firmware version | [optional] 
**numa_node** | **int** | NUMA node the card is a part of | [optional] 
**pci_address** | **str** | PCI address (for PCI cards) | [optional] 
**ports** | [**List[ResourcesNetworkCardPort]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ResourcesNetworkCardPort.md) | List of ports on the card | [optional] 
**product** | **str** | Name of the product | [optional] 
**product_id** | **str** | PCI ID of the product | [optional] 
**sriov** | [**ResourcesNetworkCardSRIOV**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ResourcesNetworkCardSRIOV.md) |  | [optional] 
**usb_address** | **str** | USB address (for USB cards) | [optional] 
**vdpa** | [**ResourcesNetworkCardVDPA**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ResourcesNetworkCardVDPA.md) |  | [optional] 
**vendor** | **str** | Name of the vendor | [optional] 
**vendor_id** | **str** | PCI ID of the vendor | [optional] 

## Example

```python
from pyincusd.models.resources_network_card import ResourcesNetworkCard

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesNetworkCard from a JSON string
resources_network_card_instance = ResourcesNetworkCard.from_json(json)
# print the JSON string representation of the object
print(ResourcesNetworkCard.to_json())

# convert the object into a dict
resources_network_card_dict = resources_network_card_instance.to_dict()
# create an instance of ResourcesNetworkCard from a dict
resources_network_card_from_dict = ResourcesNetworkCard.from_dict(resources_network_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


