# ServerPut400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_code** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pyincusd.models.server_put400_response import ServerPut400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPut400Response from a JSON string
server_put400_response_instance = ServerPut400Response.from_json(json)
# print the JSON string representation of the object
print(ServerPut400Response.to_json())

# convert the object into a dict
server_put400_response_dict = server_put400_response_instance.to_dict()
# create an instance of ServerPut400Response from a dict
server_put400_response_from_dict = ServerPut400Response.from_dict(server_put400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


