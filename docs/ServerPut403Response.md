# ServerPut403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_code** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pyincusd.models.server_put403_response import ServerPut403Response

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPut403Response from a JSON string
server_put403_response_instance = ServerPut403Response.from_json(json)
# print the JSON string representation of the object
print(ServerPut403Response.to_json())

# convert the object into a dict
server_put403_response_dict = server_put403_response_instance.to_dict()
# create an instance of ServerPut403Response from a dict
server_put403_response_from_dict = ServerPut403Response.from_dict(server_put403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


