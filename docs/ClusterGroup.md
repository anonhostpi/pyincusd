# ClusterGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Cluster group configuration map | [optional] 
**description** | **str** | The description of the cluster group | [optional] 
**members** | **List[str]** | List of members in this group | [optional] 
**name** | **str** | The new name of the cluster group | [optional] 
**used_by** | **List[str]** | List of URLs of objects using this cluster group | [optional] [readonly] 

## Example

```python
from pyincusd.models.cluster_group import ClusterGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterGroup from a JSON string
cluster_group_instance = ClusterGroup.from_json(json)
# print the JSON string representation of the object
print(ClusterGroup.to_json())

# convert the object into a dict
cluster_group_dict = cluster_group_instance.to_dict()
# create an instance of ClusterGroup from a dict
cluster_group_from_dict = ClusterGroup.from_dict(cluster_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


