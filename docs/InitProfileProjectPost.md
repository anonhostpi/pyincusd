# InitProfileProjectPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** | Project in which the profile will reside | [optional] 
**config** | **object** | Instance configuration map (refer to doc/instances.md) | [optional] 
**description** | **str** | Description of the profile | [optional] 
**devices** | **object** | List of devices | [optional] 
**name** | **str** | The name of the new profile | [optional] 

## Example

```python
from pyincusd.models.init_profile_project_post import InitProfileProjectPost

# TODO update the JSON string below
json = "{}"
# create an instance of InitProfileProjectPost from a JSON string
init_profile_project_post_instance = InitProfileProjectPost.from_json(json)
# print the JSON string representation of the object
print(InitProfileProjectPost.to_json())

# convert the object into a dict
init_profile_project_post_dict = init_profile_project_post_instance.to_dict()
# create an instance of InitProfileProjectPost from a dict
init_profile_project_post_from_dict = InitProfileProjectPost.from_dict(init_profile_project_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


