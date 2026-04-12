# InstanceSnapshotsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | When the snapshot expires (gets auto-deleted) | [optional] 
**name** | **str** | Snapshot name | [optional] 
**stateful** | **bool** | Whether the snapshot should include runtime state | [optional] 

## Example

```python
from pyincusd.models.instance_snapshots_post import InstanceSnapshotsPost

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceSnapshotsPost from a JSON string
instance_snapshots_post_instance = InstanceSnapshotsPost.from_json(json)
# print the JSON string representation of the object
print(InstanceSnapshotsPost.to_json())

# convert the object into a dict
instance_snapshots_post_dict = instance_snapshots_post_instance.to_dict()
# create an instance of InstanceSnapshotsPost from a dict
instance_snapshots_post_from_dict = InstanceSnapshotsPost.from_dict(instance_snapshots_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


