# InstanceSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | Architecture name | [optional] 
**config** | **object** | Instance configuration (see doc/instances.md) | [optional] 
**created_at** | **datetime** | Instance creation timestamp | [optional] 
**description** | **str** | Instance description | [optional] 
**devices** | **object** | Instance devices (see doc/instances.md) | [optional] 
**ephemeral** | **bool** | Whether the instance is ephemeral (deleted on shutdown) | [optional] 
**expanded_config** | **object** | Expanded configuration (all profiles and local config merged) | [optional] 
**expanded_devices** | **object** | Expanded devices (all profiles and local devices merged) | [optional] 
**expires_at** | **datetime** | When the snapshot expires (gets auto-deleted) | [optional] 
**last_used_at** | **datetime** | Last start timestamp | [optional] 
**name** | **str** | Snapshot name | [optional] 
**profiles** | **List[str]** | List of profiles applied to the instance | [optional] 
**size** | **int** | Size of the snapshot in bytes | [optional] 
**stateful** | **bool** | Whether the instance currently has saved state on disk | [optional] 

## Example

```python
from pyincusd.models.instance_snapshot import InstanceSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceSnapshot from a JSON string
instance_snapshot_instance = InstanceSnapshot.from_json(json)
# print the JSON string representation of the object
print(InstanceSnapshot.to_json())

# convert the object into a dict
instance_snapshot_dict = instance_snapshot_instance.to_dict()
# create an instance of InstanceSnapshot from a dict
instance_snapshot_from_dict = InstanceSnapshot.from_dict(instance_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


