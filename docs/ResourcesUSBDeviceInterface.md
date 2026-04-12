# ResourcesUSBDeviceInterface

ResourcesUSBDeviceInterface represents a USB device interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** | Class of USB interface | [optional] 
**class_id** | **int** | ID of the USB interface class | [optional] 
**driver** | **str** | Kernel driver currently associated with the device | [optional] 
**driver_version** | **str** | Version of the kernel driver | [optional] 
**number** | **int** | Interface number | [optional] 
**subclass** | **str** | Sub class of the interface | [optional] 
**subclass_id** | **int** | ID of the USB interface sub class | [optional] 

## Example

```python
from pyincusd.models.resources_usb_device_interface import ResourcesUSBDeviceInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesUSBDeviceInterface from a JSON string
resources_usb_device_interface_instance = ResourcesUSBDeviceInterface.from_json(json)
# print the JSON string representation of the object
print(ResourcesUSBDeviceInterface.to_json())

# convert the object into a dict
resources_usb_device_interface_dict = resources_usb_device_interface_instance.to_dict()
# create an instance of ResourcesUSBDeviceInterface from a dict
resources_usb_device_interface_from_dict = ResourcesUSBDeviceInterface.from_dict(resources_usb_device_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


