# ProfilesGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[Profile]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/Profile.md) | List of profiles | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.profiles_get_recursion1200_response import ProfilesGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesGetRecursion1200Response from a JSON string
profiles_get_recursion1200_response_instance = ProfilesGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(ProfilesGetRecursion1200Response.to_json())

# convert the object into a dict
profiles_get_recursion1200_response_dict = profiles_get_recursion1200_response_instance.to_dict()
# create an instance of ProfilesGetRecursion1200Response from a dict
profiles_get_recursion1200_response_from_dict = ProfilesGetRecursion1200Response.from_dict(profiles_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


