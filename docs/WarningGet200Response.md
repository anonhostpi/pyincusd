# WarningGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Warning**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/Warning.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.warning_get200_response import WarningGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WarningGet200Response from a JSON string
warning_get200_response_instance = WarningGet200Response.from_json(json)
# print the JSON string representation of the object
print(WarningGet200Response.to_json())

# convert the object into a dict
warning_get200_response_dict = warning_get200_response_instance.to_dict()
# create an instance of WarningGet200Response from a dict
warning_get200_response_from_dict = WarningGet200Response.from_dict(warning_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


