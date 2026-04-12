# ServerPut

ServerPut represents the modifiable fields of a server configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Server configuration map (refer to doc/server.md) | [optional] 

## Example

```python
from pyincusd.models.server_put import ServerPut

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPut from a JSON string
server_put_instance = ServerPut.from_json(json)
# print the JSON string representation of the object
print(ServerPut.to_json())

# convert the object into a dict
server_put_dict = server_put_instance.to_dict()
# create an instance of ServerPut from a dict
server_put_from_dict = ServerPut.from_dict(server_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


