# ProjectGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Project**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/Project.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.project_get200_response import ProjectGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectGet200Response from a JSON string
project_get200_response_instance = ProjectGet200Response.from_json(json)
# print the JSON string representation of the object
print(ProjectGet200Response.to_json())

# convert the object into a dict
project_get200_response_dict = project_get200_response_instance.to_dict()
# create an instance of ProjectGet200Response from a dict
project_get200_response_from_dict = ProjectGet200Response.from_dict(project_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


