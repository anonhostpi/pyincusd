# NetworksStateGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**NetworkState**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkState.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.networks_state_get200_response import NetworksStateGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworksStateGet200Response from a JSON string
networks_state_get200_response_instance = NetworksStateGet200Response.from_json(json)
# print the JSON string representation of the object
print(NetworksStateGet200Response.to_json())

# convert the object into a dict
networks_state_get200_response_dict = networks_state_get200_response_instance.to_dict()
# create an instance of NetworksStateGet200Response from a dict
networks_state_get200_response_from_dict = NetworksStateGet200Response.from_dict(networks_state_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


