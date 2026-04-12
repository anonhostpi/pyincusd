# Resources

Resources represents the system hardware resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**ResourcesCPU**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ResourcesCPU.md) |  | [optional] 
**gpu** | [**ResourcesGPU**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ResourcesGPU.md) |  | [optional] 
**load** | [**ResourcesLoad**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ResourcesLoad.md) |  | [optional] 
**memory** | [**ResourcesMemory**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ResourcesMemory.md) |  | [optional] 
**network** | [**ResourcesNetwork**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ResourcesNetwork.md) |  | [optional] 
**pci** | [**ResourcesPCI**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ResourcesPCI.md) |  | [optional] 
**serial** | [**ResourcesSerial**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ResourcesSerial.md) |  | [optional] 
**storage** | [**ResourcesStorage**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ResourcesStorage.md) |  | [optional] 
**system** | [**ResourcesSystem**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ResourcesSystem.md) |  | [optional] 
**usb** | [**ResourcesUSB**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/ResourcesUSB.md) |  | [optional] 

## Example

```python
from pyincusd.models.resources import Resources

# TODO update the JSON string below
json = "{}"
# create an instance of Resources from a JSON string
resources_instance = Resources.from_json(json)
# print the JSON string representation of the object
print(Resources.to_json())

# convert the object into a dict
resources_dict = resources_instance.to_dict()
# create an instance of Resources from a dict
resources_from_dict = Resources.from_dict(resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


