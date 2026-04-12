# ProjectStateResource

ProjectStateResource represents the state of a particular resource in a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Limit for the resource (-1 if none) | [optional] 
**usage** | **int** | Current usage for the resource | [optional] 

## Example

```python
from pyincusd.models.project_state_resource import ProjectStateResource

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStateResource from a JSON string
project_state_resource_instance = ProjectStateResource.from_json(json)
# print the JSON string representation of the object
print(ProjectStateResource.to_json())

# convert the object into a dict
project_state_resource_dict = project_state_resource_instance.to_dict()
# create an instance of ProjectStateResource from a dict
project_state_resource_from_dict = ProjectStateResource.from_dict(project_state_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


