# ClusterMemberState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_pools** | [**Dict[str, StoragePoolState]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/StoragePoolState.md) |  | [optional] 
**sysinfo** | [**ClusterMemberSysInfo**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/ClusterMemberSysInfo.md) |  | [optional] 

## Example

```python
from pyincusd.models.cluster_member_state import ClusterMemberState

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMemberState from a JSON string
cluster_member_state_instance = ClusterMemberState.from_json(json)
# print the JSON string representation of the object
print(ClusterMemberState.to_json())

# convert the object into a dict
cluster_member_state_dict = cluster_member_state_instance.to_dict()
# create an instance of ClusterMemberState from a dict
cluster_member_state_from_dict = ClusterMemberState.from_dict(cluster_member_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


