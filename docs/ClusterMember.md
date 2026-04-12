# ClusterMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | The primary architecture of the cluster member | [optional] 
**config** | **object** | Additional configuration information | [optional] 
**database** | **bool** | Whether the cluster member is a database server | [optional] 
**description** | **str** | Cluster member description | [optional] 
**failure_domain** | **str** | Name of the failure domain for this cluster member | [optional] 
**groups** | **List[str]** | List of cluster groups this member belongs to | [optional] 
**message** | **str** | Additional status information | [optional] 
**roles** | **List[str]** | List of roles held by this cluster member | [optional] 
**server_name** | **str** | Name of the cluster member | [optional] 
**status** | **str** | Current status | [optional] 
**url** | **str** | URL at which the cluster member can be reached | [optional] 

## Example

```python
from pyincusd.models.cluster_member import ClusterMember

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMember from a JSON string
cluster_member_instance = ClusterMember.from_json(json)
# print the JSON string representation of the object
print(ClusterMember.to_json())

# convert the object into a dict
cluster_member_dict = cluster_member_instance.to_dict()
# create an instance of ClusterMember from a dict
cluster_member_from_dict = ClusterMember.from_dict(cluster_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


