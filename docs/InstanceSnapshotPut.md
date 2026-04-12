# InstanceSnapshotPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | When the snapshot expires (gets auto-deleted) | [optional] 

## Example

```python
from pyincusd.models.instance_snapshot_put import InstanceSnapshotPut

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceSnapshotPut from a JSON string
instance_snapshot_put_instance = InstanceSnapshotPut.from_json(json)
# print the JSON string representation of the object
print(InstanceSnapshotPut.to_json())

# convert the object into a dict
instance_snapshot_put_dict = instance_snapshot_put_instance.to_dict()
# create an instance of InstanceSnapshotPut from a dict
instance_snapshot_put_from_dict = InstanceSnapshotPut.from_dict(instance_snapshot_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


