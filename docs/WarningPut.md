# WarningPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the warning (new, acknowledged, or resolved) | [optional] 

## Example

```python
from pyincusd.models.warning_put import WarningPut

# TODO update the JSON string below
json = "{}"
# create an instance of WarningPut from a JSON string
warning_put_instance = WarningPut.from_json(json)
# print the JSON string representation of the object
print(WarningPut.to_json())

# convert the object into a dict
warning_put_dict = warning_put_instance.to_dict()
# create an instance of WarningPut from a dict
warning_put_from_dict = WarningPut.from_dict(warning_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


