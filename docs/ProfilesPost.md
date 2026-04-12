# ProfilesPost

ProfilesPost represents the fields of a new profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Instance configuration map (refer to doc/instances.md) | [optional] 
**description** | **str** | Description of the profile | [optional] 
**devices** | **object** | List of devices | [optional] 
**name** | **str** | The name of the new profile | [optional] 

## Example

```python
from pyincusd.models.profiles_post import ProfilesPost

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesPost from a JSON string
profiles_post_instance = ProfilesPost.from_json(json)
# print the JSON string representation of the object
print(ProfilesPost.to_json())

# convert the object into a dict
profiles_post_dict = profiles_post_instance.to_dict()
# create an instance of ProfilesPost from a dict
profiles_post_from_dict = ProfilesPost.from_dict(profiles_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


