# InstanceGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Instance**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/Instance.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.instance_get200_response import InstanceGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceGet200Response from a JSON string
instance_get200_response_instance = InstanceGet200Response.from_json(json)
# print the JSON string representation of the object
print(InstanceGet200Response.to_json())

# convert the object into a dict
instance_get200_response_dict = instance_get200_response_instance.to_dict()
# create an instance of InstanceGet200Response from a dict
instance_get200_response_from_dict = InstanceGet200Response.from_dict(instance_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


