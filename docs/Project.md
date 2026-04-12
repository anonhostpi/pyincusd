# Project

Project represents a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Project configuration map (refer to doc/projects.md) | [optional] 
**description** | **str** | Description of the project | [optional] 
**name** | **str** | The project name | [optional] [readonly] 
**used_by** | **List[str]** | List of URLs of objects using this project | [optional] [readonly] 

## Example

```python
from pyincusd.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


