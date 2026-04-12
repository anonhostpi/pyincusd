# ResourcesSystemFirmware

ResourcesSystemFirmware represents the system firmware

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Firmware build date | [optional] 
**vendor** | **str** | Firmware vendor | [optional] 
**version** | **str** | Firmware version | [optional] 

## Example

```python
from pyincusd.models.resources_system_firmware import ResourcesSystemFirmware

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesSystemFirmware from a JSON string
resources_system_firmware_instance = ResourcesSystemFirmware.from_json(json)
# print the JSON string representation of the object
print(ResourcesSystemFirmware.to_json())

# convert the object into a dict
resources_system_firmware_dict = resources_system_firmware_instance.to_dict()
# create an instance of ResourcesSystemFirmware from a dict
resources_system_firmware_from_dict = ResourcesSystemFirmware.from_dict(resources_system_firmware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


