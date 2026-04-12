# ProjectsPost

ProjectsPost represents the fields of a new project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Project configuration map (refer to doc/projects.md) | [optional] 
**description** | **str** | Description of the project | [optional] 
**name** | **str** | The name of the new project | [optional] 

## Example

```python
from pyincusd.models.projects_post import ProjectsPost

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsPost from a JSON string
projects_post_instance = ProjectsPost.from_json(json)
# print the JSON string representation of the object
print(ProjectsPost.to_json())

# convert the object into a dict
projects_post_dict = projects_post_instance.to_dict()
# create an instance of ProjectsPost from a dict
projects_post_from_dict = ProjectsPost.from_dict(projects_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


