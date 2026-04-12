# Server

Server represents a server configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_extensions** | **List[str]** | List of supported API extensions | [optional] [readonly] 
**api_status** | **str** | Support status of the current API (one of \&quot;devel\&quot;, \&quot;stable\&quot; or \&quot;deprecated\&quot;) | [optional] [readonly] 
**api_version** | **str** | API version number | [optional] [readonly] 
**auth** | **str** | Whether the client is trusted (one of \&quot;trusted\&quot; or \&quot;untrusted\&quot;) | [optional] [readonly] 
**auth_methods** | **List[str]** | List of supported authentication methods | [optional] [readonly] 
**auth_user_method** | **str** | The current API user login method | [optional] [readonly] 
**auth_user_name** | **str** | The current API user identifier | [optional] [readonly] 
**config** | **object** | Server configuration map (refer to doc/server.md) | [optional] 
**environment** | [**ServerEnvironment**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerEnvironment.md) |  | [optional] 
**public** | **bool** | Whether the server is public-only (only public endpoints are implemented) | [optional] [readonly] 

## Example

```python
from pyincusd.models.server import Server

# TODO update the JSON string below
json = "{}"
# create an instance of Server from a JSON string
server_instance = Server.from_json(json)
# print the JSON string representation of the object
print(Server.to_json())

# convert the object into a dict
server_dict = server_instance.to_dict()
# create an instance of Server from a dict
server_from_dict = Server.from_dict(server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


