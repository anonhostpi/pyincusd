# ClusterGroupPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Cluster group configuration map | [optional] 
**description** | **str** | The description of the cluster group | [optional] 
**members** | **List[str]** | List of members in this group | [optional] 

## Example

```python
from pyincusd.models.cluster_group_put import ClusterGroupPut

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterGroupPut from a JSON string
cluster_group_put_instance = ClusterGroupPut.from_json(json)
# print the JSON string representation of the object
print(ClusterGroupPut.to_json())

# convert the object into a dict
cluster_group_put_dict = cluster_group_put_instance.to_dict()
# create an instance of ClusterGroupPut from a dict
cluster_group_put_from_dict = ClusterGroupPut.from_dict(cluster_group_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


