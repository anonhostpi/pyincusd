# ResourcesGPUCard

ResourcesGPUCard represents a GPU card on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | Kernel driver currently associated with the GPU | [optional] 
**driver_version** | **str** | Version of the kernel driver | [optional] 
**drm** | [**ResourcesGPUCardDRM**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/ResourcesGPUCardDRM.md) |  | [optional] 
**mdev** | [**Dict[str, ResourcesGPUCardMdev]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/ResourcesGPUCardMdev.md) | Map of available mediated device profiles | [optional] 
**numa_node** | **int** | NUMA node the GPU is a part of | [optional] 
**nvidia** | [**ResourcesGPUCardNvidia**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/ResourcesGPUCardNvidia.md) |  | [optional] 
**pci_address** | **str** | PCI address | [optional] 
**product** | **str** | Name of the product | [optional] 
**product_id** | **str** | PCI ID of the product | [optional] 
**sriov** | [**ResourcesGPUCardSRIOV**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/ResourcesGPUCardSRIOV.md) |  | [optional] 
**usb_address** | **str** | USB address (for USB cards) | [optional] 
**vendor** | **str** | Name of the vendor | [optional] 
**vendor_id** | **str** | PCI ID of the vendor | [optional] 

## Example

```python
from pyincusd.models.resources_gpu_card import ResourcesGPUCard

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesGPUCard from a JSON string
resources_gpu_card_instance = ResourcesGPUCard.from_json(json)
# print the JSON string representation of the object
print(ResourcesGPUCard.to_json())

# convert the object into a dict
resources_gpu_card_dict = resources_gpu_card_instance.to_dict()
# create an instance of ResourcesGPUCard from a dict
resources_gpu_card_from_dict = ResourcesGPUCard.from_dict(resources_gpu_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


