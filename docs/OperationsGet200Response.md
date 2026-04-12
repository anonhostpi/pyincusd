# OperationsGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, List[str]]** | JSON object of operation types to operation URLs | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.operations_get200_response import OperationsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OperationsGet200Response from a JSON string
operations_get200_response_instance = OperationsGet200Response.from_json(json)
# print the JSON string representation of the object
print(OperationsGet200Response.to_json())

# convert the object into a dict
operations_get200_response_dict = operations_get200_response_instance.to_dict()
# create an instance of OperationsGet200Response from a dict
operations_get200_response_from_dict = OperationsGet200Response.from_dict(operations_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


