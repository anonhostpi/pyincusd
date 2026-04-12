# ResourcesPCIDevice

ResourcesPCIDevice represents a PCI device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | Kernel driver currently associated with the GPU | [optional] 
**driver_version** | **str** | Version of the kernel driver | [optional] 
**iommu_group** | **int** | IOMMU group number | [optional] 
**numa_node** | **int** | NUMA node the card is a part of | [optional] 
**pci_address** | **str** | PCI address | [optional] 
**product** | **str** | Name of the product | [optional] 
**product_id** | **str** | PCI ID of the product | [optional] 
**vendor** | **str** | Name of the vendor | [optional] 
**vendor_id** | **str** | PCI ID of the vendor | [optional] 
**vpd** | [**ResourcesPCIVPD**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post7/docs/ResourcesPCIVPD.md) |  | [optional] 

## Example

```python
from pyincusd.models.resources_pci_device import ResourcesPCIDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesPCIDevice from a JSON string
resources_pci_device_instance = ResourcesPCIDevice.from_json(json)
# print the JSON string representation of the object
print(ResourcesPCIDevice.to_json())

# convert the object into a dict
resources_pci_device_dict = resources_pci_device_instance.to_dict()
# create an instance of ResourcesPCIDevice from a dict
resources_pci_device_from_dict = ResourcesPCIDevice.from_dict(resources_pci_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


