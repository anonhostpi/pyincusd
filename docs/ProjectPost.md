# ProjectPost

ProjectPost represents the fields required to rename a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name for the project | [optional] 

## Example

```python
from pyincusd.models.project_post import ProjectPost

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPost from a JSON string
project_post_instance = ProjectPost.from_json(json)
# print the JSON string representation of the object
print(ProjectPost.to_json())

# convert the object into a dict
project_post_dict = project_post_instance.to_dict()
# create an instance of ProjectPost from a dict
project_post_from_dict = ProjectPost.from_dict(project_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


