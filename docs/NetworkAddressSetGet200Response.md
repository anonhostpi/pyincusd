# NetworkAddressSetGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**NetworkAddressSet**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/NetworkAddressSet.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.network_address_set_get200_response import NetworkAddressSetGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAddressSetGet200Response from a JSON string
network_address_set_get200_response_instance = NetworkAddressSetGet200Response.from_json(json)
# print the JSON string representation of the object
print(NetworkAddressSetGet200Response.to_json())

# convert the object into a dict
network_address_set_get200_response_dict = network_address_set_get200_response_instance.to_dict()
# create an instance of NetworkAddressSetGet200Response from a dict
network_address_set_get200_response_from_dict = NetworkAddressSetGet200Response.from_dict(network_address_set_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


