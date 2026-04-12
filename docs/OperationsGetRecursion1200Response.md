# OperationsGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[Operation]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/Operation.md) | List of operations | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.operations_get_recursion1200_response import OperationsGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OperationsGetRecursion1200Response from a JSON string
operations_get_recursion1200_response_instance = OperationsGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(OperationsGetRecursion1200Response.to_json())

# convert the object into a dict
operations_get_recursion1200_response_dict = operations_get_recursion1200_response_instance.to_dict()
# create an instance of OperationsGetRecursion1200Response from a dict
operations_get_recursion1200_response_from_dict = OperationsGetRecursion1200Response.from_dict(operations_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


