# InstanceBackupPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New backup name | [optional] 

## Example

```python
from pyincusd.models.instance_backup_post import InstanceBackupPost

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceBackupPost from a JSON string
instance_backup_post_instance = InstanceBackupPost.from_json(json)
# print the JSON string representation of the object
print(InstanceBackupPost.to_json())

# convert the object into a dict
instance_backup_post_dict = instance_backup_post_instance.to_dict()
# create an instance of InstanceBackupPost from a dict
instance_backup_post_from_dict = InstanceBackupPost.from_dict(instance_backup_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


