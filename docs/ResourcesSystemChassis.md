# ResourcesSystemChassis

ResourcesSystemChassis represents the system chassis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** | Chassis serial number | [optional] 
**type** | **str** | Chassis type | [optional] 
**vendor** | **str** | Chassis vendor | [optional] 
**version** | **str** | Chassis version/revision | [optional] 

## Example

```python
from pyincusd.models.resources_system_chassis import ResourcesSystemChassis

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesSystemChassis from a JSON string
resources_system_chassis_instance = ResourcesSystemChassis.from_json(json)
# print the JSON string representation of the object
print(ResourcesSystemChassis.to_json())

# convert the object into a dict
resources_system_chassis_dict = resources_system_chassis_instance.to_dict()
# create an instance of ResourcesSystemChassis from a dict
resources_system_chassis_from_dict = ResourcesSystemChassis.from_dict(resources_system_chassis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


