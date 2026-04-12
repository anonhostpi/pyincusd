# ServerUntrusted

ServerUntrusted represents a server configuration for an untrusted client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_extensions** | **List[str]** | List of supported API extensions | [optional] [readonly] 
**api_status** | **str** | Support status of the current API (one of \&quot;devel\&quot;, \&quot;stable\&quot; or \&quot;deprecated\&quot;) | [optional] [readonly] 
**api_version** | **str** | API version number | [optional] [readonly] 
**auth** | **str** | Whether the client is trusted (one of \&quot;trusted\&quot; or \&quot;untrusted\&quot;) | [optional] [readonly] 
**auth_methods** | **List[str]** | List of supported authentication methods | [optional] [readonly] 
**config** | **object** | Server configuration map (refer to doc/server.md) | [optional] 
**public** | **bool** | Whether the server is public-only (only public endpoints are implemented) | [optional] [readonly] 

## Example

```python
from pyincusd.models.server_untrusted import ServerUntrusted

# TODO update the JSON string below
json = "{}"
# create an instance of ServerUntrusted from a JSON string
server_untrusted_instance = ServerUntrusted.from_json(json)
# print the JSON string representation of the object
print(ServerUntrusted.to_json())

# convert the object into a dict
server_untrusted_dict = server_untrusted_instance.to_dict()
# create an instance of ServerUntrusted from a dict
server_untrusted_from_dict = ServerUntrusted.from_dict(server_untrusted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


