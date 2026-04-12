# InstanceConsoleGet404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_code** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pyincusd.models.instance_console_get404_response import InstanceConsoleGet404Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConsoleGet404Response from a JSON string
instance_console_get404_response_instance = InstanceConsoleGet404Response.from_json(json)
# print the JSON string representation of the object
print(InstanceConsoleGet404Response.to_json())

# convert the object into a dict
instance_console_get404_response_dict = instance_console_get404_response_instance.to_dict()
# create an instance of InstanceConsoleGet404Response from a dict
instance_console_get404_response_from_dict = InstanceConsoleGet404Response.from_dict(instance_console_get404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


