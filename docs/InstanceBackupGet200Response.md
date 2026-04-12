# InstanceBackupGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**InstanceBackup**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/InstanceBackup.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.instance_backup_get200_response import InstanceBackupGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceBackupGet200Response from a JSON string
instance_backup_get200_response_instance = InstanceBackupGet200Response.from_json(json)
# print the JSON string representation of the object
print(InstanceBackupGet200Response.to_json())

# convert the object into a dict
instance_backup_get200_response_dict = instance_backup_get200_response_instance.to_dict()
# create an instance of InstanceBackupGet200Response from a dict
instance_backup_get200_response_from_dict = InstanceBackupGet200Response.from_dict(instance_backup_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


