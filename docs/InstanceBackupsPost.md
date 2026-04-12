# InstanceBackupsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression_algorithm** | **str** | What compression algorithm to use | [optional] 
**expires_at** | **datetime** | When the backup expires (gets auto-deleted) | [optional] 
**instance_only** | **bool** | Whether to ignore snapshots | [optional] 
**name** | **str** | Backup name | [optional] 
**optimized_storage** | **bool** | Whether to use a pool-optimized binary format (instead of plain tarball) | [optional] 
**root_only** | **bool** | Whether to ignore dependent volumes | [optional] 
**target** | [**BackupTarget**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/BackupTarget.md) |  | [optional] 

## Example

```python
from pyincusd.models.instance_backups_post import InstanceBackupsPost

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceBackupsPost from a JSON string
instance_backups_post_instance = InstanceBackupsPost.from_json(json)
# print the JSON string representation of the object
print(InstanceBackupsPost.to_json())

# convert the object into a dict
instance_backups_post_dict = instance_backups_post_instance.to_dict()
# create an instance of InstanceBackupsPost from a dict
instance_backups_post_from_dict = InstanceBackupsPost.from_dict(instance_backups_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


