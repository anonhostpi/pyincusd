# ServerPut200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pyincusd.models.server_put200_response import ServerPut200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPut200Response from a JSON string
server_put200_response_instance = ServerPut200Response.from_json(json)
# print the JSON string representation of the object
print(ServerPut200Response.to_json())

# convert the object into a dict
server_put200_response_dict = server_put200_response_instance.to_dict()
# create an instance of ServerPut200Response from a dict
server_put200_response_from_dict = ServerPut200Response.from_dict(server_put200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


