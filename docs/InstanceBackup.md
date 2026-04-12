# InstanceBackup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | When the backup was created | [optional] 
**expires_at** | **datetime** | When the backup expires (gets auto-deleted) | [optional] 
**instance_only** | **bool** | Whether to ignore snapshots | [optional] 
**name** | **str** | Backup name | [optional] 
**optimized_storage** | **bool** | Whether to use a pool-optimized binary format (instead of plain tarball) | [optional] 

## Example

```python
from pyincusd.models.instance_backup import InstanceBackup

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceBackup from a JSON string
instance_backup_instance = InstanceBackup.from_json(json)
# print the JSON string representation of the object
print(InstanceBackup.to_json())

# convert the object into a dict
instance_backup_dict = instance_backup_instance.to_dict()
# create an instance of InstanceBackup from a dict
instance_backup_from_dict = InstanceBackup.from_dict(instance_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


