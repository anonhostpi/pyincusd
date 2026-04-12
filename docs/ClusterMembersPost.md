# ClusterMembersPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_name** | **str** | The name of the new cluster member | [optional] 

## Example

```python
from pyincusd.models.cluster_members_post import ClusterMembersPost

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMembersPost from a JSON string
cluster_members_post_instance = ClusterMembersPost.from_json(json)
# print the JSON string representation of the object
print(ClusterMembersPost.to_json())

# convert the object into a dict
cluster_members_post_dict = cluster_members_post_instance.to_dict()
# create an instance of ClusterMembersPost from a dict
cluster_members_post_from_dict = ClusterMembersPost.from_dict(cluster_members_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


