# ResourcesUSB

ResourcesUSB represents the USB devices available on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[ResourcesUSBDevice]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/ResourcesUSBDevice.md) | List of USB devices | [optional] 
**total** | **int** | Total number of USB devices | [optional] 

## Example

```python
from pyincusd.models.resources_usb import ResourcesUSB

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesUSB from a JSON string
resources_usb_instance = ResourcesUSB.from_json(json)
# print the JSON string representation of the object
print(ResourcesUSB.to_json())

# convert the object into a dict
resources_usb_dict = resources_usb_instance.to_dict()
# create an instance of ResourcesUSB from a dict
resources_usb_from_dict = ResourcesUSB.from_dict(resources_usb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


