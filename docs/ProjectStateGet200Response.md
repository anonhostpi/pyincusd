# ProjectStateGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ProjectState**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/ProjectState.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.project_state_get200_response import ProjectStateGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStateGet200Response from a JSON string
project_state_get200_response_instance = ProjectStateGet200Response.from_json(json)
# print the JSON string representation of the object
print(ProjectStateGet200Response.to_json())

# convert the object into a dict
project_state_get200_response_dict = project_state_get200_response_instance.to_dict()
# create an instance of ProjectStateGet200Response from a dict
project_state_get200_response_from_dict = ProjectStateGet200Response.from_dict(project_state_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


