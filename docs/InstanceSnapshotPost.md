# InstanceSnapshotPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live** | **bool** | Whether to perform a live migration (requires migration) | [optional] 
**migration** | **bool** | Whether this is a migration request | [optional] 
**name** | **str** | New name for the snapshot | [optional] 
**target** | [**InstancePostTarget**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/InstancePostTarget.md) |  | [optional] 

## Example

```python
from pyincusd.models.instance_snapshot_post import InstanceSnapshotPost

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceSnapshotPost from a JSON string
instance_snapshot_post_instance = InstanceSnapshotPost.from_json(json)
# print the JSON string representation of the object
print(InstanceSnapshotPost.to_json())

# convert the object into a dict
instance_snapshot_post_dict = instance_snapshot_post_instance.to_dict()
# create an instance of InstanceSnapshotPost from a dict
instance_snapshot_post_from_dict = InstanceSnapshotPost.from_dict(instance_snapshot_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


