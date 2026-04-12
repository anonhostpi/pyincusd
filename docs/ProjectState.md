# ProjectState

ProjectState represents the current running state of a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**Dict[str, ProjectStateResource]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/ProjectStateResource.md) | Allocated and used resources | [optional] [readonly] 

## Example

```python
from pyincusd.models.project_state import ProjectState

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectState from a JSON string
project_state_instance = ProjectState.from_json(json)
# print the JSON string representation of the object
print(ProjectState.to_json())

# convert the object into a dict
project_state_dict = project_state_instance.to_dict()
# create an instance of ProjectState from a dict
project_state_from_dict = ProjectState.from_dict(project_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


