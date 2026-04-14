# ProfileGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Profile**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/Profile.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.profile_get200_response import ProfileGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileGet200Response from a JSON string
profile_get200_response_instance = ProfileGet200Response.from_json(json)
# print the JSON string representation of the object
print(ProfileGet200Response.to_json())

# convert the object into a dict
profile_get200_response_dict = profile_get200_response_instance.to_dict()
# create an instance of ProfileGet200Response from a dict
profile_get200_response_from_dict = ProfileGet200Response.from_dict(profile_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


