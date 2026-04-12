# ResourcesLoad

ResourcesLoad represents system load information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average1_min** | **float** | Load average in the past minute | [optional] 
**average5_min** | **float** | Load average in the past 5 minutes | [optional] 
**average10_min** | **float** | Load average in the past 10 minutes | [optional] 
**processes** | **int** | The number of active processes | [optional] 

## Example

```python
from pyincusd.models.resources_load import ResourcesLoad

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesLoad from a JSON string
resources_load_instance = ResourcesLoad.from_json(json)
# print the JSON string representation of the object
print(ResourcesLoad.to_json())

# convert the object into a dict
resources_load_dict = resources_load_instance.to_dict()
# create an instance of ResourcesLoad from a dict
resources_load_from_dict = ResourcesLoad.from_dict(resources_load_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


