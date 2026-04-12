# InstanceConsolePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Forces a connection to the console | [optional] 
**height** | **int** | Console height in rows (console type only) | [optional] 
**type** | **str** | Type of console to attach to (console or vga) | [optional] 
**width** | **int** | Console width in columns (console type only) | [optional] 

## Example

```python
from pyincusd.models.instance_console_post import InstanceConsolePost

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConsolePost from a JSON string
instance_console_post_instance = InstanceConsolePost.from_json(json)
# print the JSON string representation of the object
print(InstanceConsolePost.to_json())

# convert the object into a dict
instance_console_post_dict = instance_console_post_instance.to_dict()
# create an instance of InstanceConsolePost from a dict
instance_console_post_from_dict = InstanceConsolePost.from_dict(instance_console_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


