# ResourcesGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Resources**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/Resources.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.resources_get200_response import ResourcesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesGet200Response from a JSON string
resources_get200_response_instance = ResourcesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ResourcesGet200Response.to_json())

# convert the object into a dict
resources_get200_response_dict = resources_get200_response_instance.to_dict()
# create an instance of ResourcesGet200Response from a dict
resources_get200_response_from_dict = ResourcesGet200Response.from_dict(resources_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


