# ClusterMemberPut

ClusterMemberPut represents the modifiable fields of a cluster member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Additional configuration information | [optional] 
**description** | **str** | Cluster member description | [optional] 
**failure_domain** | **str** | Name of the failure domain for this cluster member | [optional] 
**groups** | **List[str]** | List of cluster groups this member belongs to | [optional] 
**roles** | **List[str]** | List of roles held by this cluster member | [optional] 

## Example

```python
from pyincusd.models.cluster_member_put import ClusterMemberPut

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMemberPut from a JSON string
cluster_member_put_instance = ClusterMemberPut.from_json(json)
# print the JSON string representation of the object
print(ClusterMemberPut.to_json())

# convert the object into a dict
cluster_member_put_dict = cluster_member_put_instance.to_dict()
# create an instance of ClusterMemberPut from a dict
cluster_member_put_from_dict = ClusterMemberPut.from_dict(cluster_member_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


