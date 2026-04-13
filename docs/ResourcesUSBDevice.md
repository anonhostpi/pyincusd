# ResourcesUSBDevice

ResourcesUSBDevice represents a USB device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bus_address** | **int** | USB address (bus) | [optional] 
**device_address** | **int** | USB address (device) | [optional] 
**interfaces** | [**List[ResourcesUSBDeviceInterface]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post19/docs/ResourcesUSBDeviceInterface.md) | List of USB interfaces | [optional] 
**product** | **str** | Name of the product | [optional] 
**product_id** | **str** | USB ID of the product | [optional] 
**serial** | **str** | USB serial number | [optional] 
**speed** | **float** | Transfer speed (Mbit/s) | [optional] 
**vendor** | **str** | Name of the vendor | [optional] 
**vendor_id** | **str** | USB ID of the vendor | [optional] 

## Example

```python
from pyincusd.models.resources_usb_device import ResourcesUSBDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesUSBDevice from a JSON string
resources_usb_device_instance = ResourcesUSBDevice.from_json(json)
# print the JSON string representation of the object
print(ResourcesUSBDevice.to_json())

# convert the object into a dict
resources_usb_device_dict = resources_usb_device_instance.to_dict()
# create an instance of ResourcesUSBDevice from a dict
resources_usb_device_from_dict = ResourcesUSBDevice.from_dict(resources_usb_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


