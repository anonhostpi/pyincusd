# InstanceStateGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**InstanceState**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/InstanceState.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.instance_state_get200_response import InstanceStateGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStateGet200Response from a JSON string
instance_state_get200_response_instance = InstanceStateGet200Response.from_json(json)
# print the JSON string representation of the object
print(InstanceStateGet200Response.to_json())

# convert the object into a dict
instance_state_get200_response_dict = instance_state_get200_response_instance.to_dict()
# create an instance of InstanceStateGet200Response from a dict
instance_state_get200_response_from_dict = InstanceStateGet200Response.from_dict(instance_state_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


