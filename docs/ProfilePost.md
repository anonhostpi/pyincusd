# ProfilePost

ProfilePost represents the fields required to rename a profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name for the profile | [optional] 

## Example

```python
from pyincusd.models.profile_post import ProfilePost

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePost from a JSON string
profile_post_instance = ProfilePost.from_json(json)
# print the JSON string representation of the object
print(ProfilePost.to_json())

# convert the object into a dict
profile_post_dict = profile_post_instance.to_dict()
# create an instance of ProfilePost from a dict
profile_post_from_dict = ProfilePost.from_dict(profile_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


