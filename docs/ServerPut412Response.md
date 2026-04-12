# ServerPut412Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_code** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pyincusd.models.server_put412_response import ServerPut412Response

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPut412Response from a JSON string
server_put412_response_instance = ServerPut412Response.from_json(json)
# print the JSON string representation of the object
print(ServerPut412Response.to_json())

# convert the object into a dict
server_put412_response_dict = server_put412_response_instance.to_dict()
# create an instance of ServerPut412Response from a dict
server_put412_response_from_dict = ServerPut412Response.from_dict(server_put412_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


