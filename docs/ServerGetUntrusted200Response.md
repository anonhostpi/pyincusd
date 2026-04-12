# ServerGetUntrusted200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ServerUntrusted**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post12/docs/ServerUntrusted.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.server_get_untrusted200_response import ServerGetUntrusted200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ServerGetUntrusted200Response from a JSON string
server_get_untrusted200_response_instance = ServerGetUntrusted200Response.from_json(json)
# print the JSON string representation of the object
print(ServerGetUntrusted200Response.to_json())

# convert the object into a dict
server_get_untrusted200_response_dict = server_get_untrusted200_response_instance.to_dict()
# create an instance of ServerGetUntrusted200Response from a dict
server_get_untrusted200_response_from_dict = ServerGetUntrusted200Response.from_dict(server_get_untrusted200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


