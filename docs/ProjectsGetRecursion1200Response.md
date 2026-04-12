# ProjectsGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[Project]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/Project.md) | List of projects | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.projects_get_recursion1200_response import ProjectsGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsGetRecursion1200Response from a JSON string
projects_get_recursion1200_response_instance = ProjectsGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(ProjectsGetRecursion1200Response.to_json())

# convert the object into a dict
projects_get_recursion1200_response_dict = projects_get_recursion1200_response_instance.to_dict()
# create an instance of ProjectsGetRecursion1200Response from a dict
projects_get_recursion1200_response_from_dict = ProjectsGetRecursion1200Response.from_dict(projects_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


