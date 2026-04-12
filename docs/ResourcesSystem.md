# ResourcesSystem

ResourcesSystem represents the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis** | [**ResourcesSystemChassis**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/ResourcesSystemChassis.md) |  | [optional] 
**family** | **str** | System family | [optional] 
**firmware** | [**ResourcesSystemFirmware**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/ResourcesSystemFirmware.md) |  | [optional] 
**motherboard** | [**ResourcesSystemMotherboard**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/ResourcesSystemMotherboard.md) |  | [optional] 
**product** | **str** | System model | [optional] 
**serial** | **str** | System serial number | [optional] 
**sku** | **str** | System nanufacturer SKU LENOVO_MT_20HR_BU_Think_FM_ThinkPad X1 Carbon 5th | [optional] 
**type** | **str** | System type (unknown, physical, virtual-machine, container, ...) | [optional] 
**uuid** | **str** | System UUID | [optional] 
**vendor** | **str** | System vendor | [optional] 
**version** | **str** | System version | [optional] 

## Example

```python
from pyincusd.models.resources_system import ResourcesSystem

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesSystem from a JSON string
resources_system_instance = ResourcesSystem.from_json(json)
# print the JSON string representation of the object
print(ResourcesSystem.to_json())

# convert the object into a dict
resources_system_dict = resources_system_instance.to_dict()
# create an instance of ResourcesSystem from a dict
resources_system_from_dict = ResourcesSystem.from_dict(resources_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


