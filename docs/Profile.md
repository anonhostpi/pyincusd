# Profile

Profile represents a profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Instance configuration map (refer to doc/instances.md) | [optional] 
**description** | **str** | Description of the profile | [optional] 
**devices** | **object** | List of devices | [optional] 
**name** | **str** | The profile name | [optional] [readonly] 
**project** | **str** | Project name | [optional] 
**used_by** | **List[str]** | List of URLs of objects using this profile | [optional] [readonly] 

## Example

```python
from pyincusd.models.profile import Profile

# TODO update the JSON string below
json = "{}"
# create an instance of Profile from a JSON string
profile_instance = Profile.from_json(json)
# print the JSON string representation of the object
print(Profile.to_json())

# convert the object into a dict
profile_dict = profile_instance.to_dict()
# create an instance of Profile from a dict
profile_from_dict = Profile.from_dict(profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


