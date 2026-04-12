# Warning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of times this warning occurred | [optional] 
**entity_url** | **str** | The entity affected by this warning | [optional] 
**first_seen_at** | **datetime** | The first time this warning occurred | [optional] 
**last_message** | **str** | The warning message | [optional] 
**last_seen_at** | **datetime** | The last time this warning occurred | [optional] 
**location** | **str** | What cluster member this warning occurred on | [optional] 
**project** | **str** | The project the warning occurred in | [optional] 
**severity** | **str** | The severity of this warning | [optional] 
**status** | **str** | Status of the warning (new, acknowledged, or resolved) | [optional] 
**type** | **str** | Type type of warning | [optional] 
**uuid** | **str** | UUID of the warning | [optional] 

## Example

```python
from pyincusd.models.warning import Warning

# TODO update the JSON string below
json = "{}"
# create an instance of Warning from a JSON string
warning_instance = Warning.from_json(json)
# print the JSON string representation of the object
print(Warning.to_json())

# convert the object into a dict
warning_dict = warning_instance.to_dict()
# create an instance of Warning from a dict
warning_from_dict = Warning.from_dict(warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


