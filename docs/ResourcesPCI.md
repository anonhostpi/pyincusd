# ResourcesPCI

ResourcesPCI represents the PCI devices available on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[ResourcesPCIDevice]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/ResourcesPCIDevice.md) | List of PCI devices | [optional] 
**total** | **int** | Total number of PCI devices | [optional] 

## Example

```python
from pyincusd.models.resources_pci import ResourcesPCI

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesPCI from a JSON string
resources_pci_instance = ResourcesPCI.from_json(json)
# print the JSON string representation of the object
print(ResourcesPCI.to_json())

# convert the object into a dict
resources_pci_dict = resources_pci_instance.to_dict()
# create an instance of ResourcesPCI from a dict
resources_pci_from_dict = ResourcesPCI.from_dict(resources_pci_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


