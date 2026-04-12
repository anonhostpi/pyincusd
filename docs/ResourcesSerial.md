# ResourcesSerial

ResourcesSerial represents the serial devices available on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[ResourcesSerialDevice]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ResourcesSerialDevice.md) | List of serial devices | [optional] 
**total** | **int** | Total number of serial devices | [optional] 

## Example

```python
from pyincusd.models.resources_serial import ResourcesSerial

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesSerial from a JSON string
resources_serial_instance = ResourcesSerial.from_json(json)
# print the JSON string representation of the object
print(ResourcesSerial.to_json())

# convert the object into a dict
resources_serial_dict = resources_serial_instance.to_dict()
# create an instance of ResourcesSerial from a dict
resources_serial_from_dict = ResourcesSerial.from_dict(resources_serial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


