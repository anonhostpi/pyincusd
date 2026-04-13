# Cluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether clustering is enabled | [optional] 
**member_config** | [**List[ClusterMemberConfigKey]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ClusterMemberConfigKey.md) | List of member configuration keys (used during join) | [optional] 
**server_name** | **str** | Name of the cluster member answering the request | [optional] 

## Example

```python
from pyincusd.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print(Cluster.to_json())

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_from_dict = Cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


