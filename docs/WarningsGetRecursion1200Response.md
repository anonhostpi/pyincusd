# WarningsGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[Warning]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/Warning.md) | List of warnings | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.warnings_get_recursion1200_response import WarningsGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WarningsGetRecursion1200Response from a JSON string
warnings_get_recursion1200_response_instance = WarningsGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(WarningsGetRecursion1200Response.to_json())

# convert the object into a dict
warnings_get_recursion1200_response_dict = warnings_get_recursion1200_response_instance.to_dict()
# create an instance of WarningsGetRecursion1200Response from a dict
warnings_get_recursion1200_response_from_dict = WarningsGetRecursion1200Response.from_dict(warnings_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


