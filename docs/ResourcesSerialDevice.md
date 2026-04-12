# ResourcesSerialDevice

ResourcesSerialDevice represents a serial device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | Device number (major:minor) | [optional] 
**device_id** | **str** | Path to /dev/serial/by-id entry | [optional] 
**device_path** | **str** | Path to /dev/serial/by-path entry | [optional] 
**driver** | **str** | kernel driver name (cdc_acm, ftdi_sio, pl2303, cp210x...) | [optional] 
**id** | **str** | Kernel device name (e.g. ttyUSB0, ttyACM0) | [optional] 
**product** | **str** | USB product name | [optional] 
**product_id** | **str** | USB product ID | [optional] 
**vendor** | **str** | USB vendor name | [optional] 
**vendor_id** | **str** | USB vendor ID | [optional] 

## Example

```python
from pyincusd.models.resources_serial_device import ResourcesSerialDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesSerialDevice from a JSON string
resources_serial_device_instance = ResourcesSerialDevice.from_json(json)
# print the JSON string representation of the object
print(ResourcesSerialDevice.to_json())

# convert the object into a dict
resources_serial_device_dict = resources_serial_device_instance.to_dict()
# create an instance of ResourcesSerialDevice from a dict
resources_serial_device_from_dict = ResourcesSerialDevice.from_dict(resources_serial_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


