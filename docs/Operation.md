# Operation

Operation represents a background operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** | Type of operation (task, token or websocket) | [optional] 
**created_at** | **datetime** | Operation creation time | [optional] 
**description** | **str** | Description of the operation | [optional] 
**err** | **str** | Operation error message | [optional] 
**id** | **str** | UUID of the operation | [optional] 
**location** | **str** | What cluster member this record was found on | [optional] 
**may_cancel** | **bool** | Whether the operation can be canceled | [optional] 
**metadata** | **object** | Operation specific metadata | [optional] 
**resources** | **object** | Affected resources | [optional] 
**status** | **str** | Status name | [optional] 
**status_code** | **int** |  | [optional] 
**updated_at** | **datetime** | Operation last change | [optional] 

## Example

```python
from pyincusd.models.operation import Operation

# TODO update the JSON string below
json = "{}"
# create an instance of Operation from a JSON string
operation_instance = Operation.from_json(json)
# print the JSON string representation of the object
print(Operation.to_json())

# convert the object into a dict
operation_dict = operation_instance.to_dict()
# create an instance of Operation from a dict
operation_from_dict = Operation.from_dict(operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


