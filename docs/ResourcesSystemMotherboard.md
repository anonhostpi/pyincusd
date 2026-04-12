# ResourcesSystemMotherboard

ResourcesSystemMotherboard represents the motherboard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Motherboard model | [optional] 
**serial** | **str** | Motherboard serial number | [optional] 
**vendor** | **str** | Motherboard vendor | [optional] 
**version** | **str** | Motherboard version/revision | [optional] 

## Example

```python
from pyincusd.models.resources_system_motherboard import ResourcesSystemMotherboard

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesSystemMotherboard from a JSON string
resources_system_motherboard_instance = ResourcesSystemMotherboard.from_json(json)
# print the JSON string representation of the object
print(ResourcesSystemMotherboard.to_json())

# convert the object into a dict
resources_system_motherboard_dict = resources_system_motherboard_instance.to_dict()
# create an instance of ResourcesSystemMotherboard from a dict
resources_system_motherboard_from_dict = ResourcesSystemMotherboard.from_dict(resources_system_motherboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


