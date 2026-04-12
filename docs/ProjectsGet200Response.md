# ProjectsGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **List[str]** | List of endpoints | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.projects_get200_response import ProjectsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsGet200Response from a JSON string
projects_get200_response_instance = ProjectsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ProjectsGet200Response.to_json())

# convert the object into a dict
projects_get200_response_dict = projects_get200_response_instance.to_dict()
# create an instance of ProjectsGet200Response from a dict
projects_get200_response_from_dict = ProjectsGet200Response.from_dict(projects_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


