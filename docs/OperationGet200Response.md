# OperationGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Operation**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post20/docs/Operation.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.operation_get200_response import OperationGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OperationGet200Response from a JSON string
operation_get200_response_instance = OperationGet200Response.from_json(json)
# print the JSON string representation of the object
print(OperationGet200Response.to_json())

# convert the object into a dict
operation_get200_response_dict = operation_get200_response_instance.to_dict()
# create an instance of OperationGet200Response from a dict
operation_get200_response_from_dict = OperationGet200Response.from_dict(operation_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


