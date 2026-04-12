# InstanceBackupsGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[InstanceBackup]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/InstanceBackup.md) | List of instance backups | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.instance_backups_get_recursion1200_response import InstanceBackupsGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceBackupsGetRecursion1200Response from a JSON string
instance_backups_get_recursion1200_response_instance = InstanceBackupsGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(InstanceBackupsGetRecursion1200Response.to_json())

# convert the object into a dict
instance_backups_get_recursion1200_response_dict = instance_backups_get_recursion1200_response_instance.to_dict()
# create an instance of InstanceBackupsGetRecursion1200Response from a dict
instance_backups_get_recursion1200_response_from_dict = InstanceBackupsGetRecursion1200Response.from_dict(instance_backups_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


