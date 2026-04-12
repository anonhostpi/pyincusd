# AccessEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Certificate fingerprint | [optional] 
**provider** | **str** | Which authorization method the certificate uses | [optional] 
**role** | **str** | The role associated with the certificate | [optional] 

## Example

```python
from pyincusd.models.access_entry import AccessEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AccessEntry from a JSON string
access_entry_instance = AccessEntry.from_json(json)
# print the JSON string representation of the object
print(AccessEntry.to_json())

# convert the object into a dict
access_entry_dict = access_entry_instance.to_dict()
# create an instance of AccessEntry from a dict
access_entry_from_dict = AccessEntry.from_dict(access_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


