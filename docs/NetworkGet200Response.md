# NetworkGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Network**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/Network.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.network_get200_response import NetworkGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkGet200Response from a JSON string
network_get200_response_instance = NetworkGet200Response.from_json(json)
# print the JSON string representation of the object
print(NetworkGet200Response.to_json())

# convert the object into a dict
network_get200_response_dict = network_get200_response_instance.to_dict()
# create an instance of NetworkGet200Response from a dict
network_get200_response_from_dict = NetworkGet200Response.from_dict(network_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


