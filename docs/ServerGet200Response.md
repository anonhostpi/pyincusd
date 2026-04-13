# ServerGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Server**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/Server.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.server_get200_response import ServerGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ServerGet200Response from a JSON string
server_get200_response_instance = ServerGet200Response.from_json(json)
# print the JSON string representation of the object
print(ServerGet200Response.to_json())

# convert the object into a dict
server_get200_response_dict = server_get200_response_instance.to_dict()
# create an instance of ServerGet200Response from a dict
server_get200_response_from_dict = ServerGet200Response.from_dict(server_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


