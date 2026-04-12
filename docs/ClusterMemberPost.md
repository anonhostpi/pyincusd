# ClusterMemberPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_name** | **str** | The new name of the cluster member | [optional] 

## Example

```python
from pyincusd.models.cluster_member_post import ClusterMemberPost

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMemberPost from a JSON string
cluster_member_post_instance = ClusterMemberPost.from_json(json)
# print the JSON string representation of the object
print(ClusterMemberPost.to_json())

# convert the object into a dict
cluster_member_post_dict = cluster_member_post_instance.to_dict()
# create an instance of ClusterMemberPost from a dict
cluster_member_post_from_dict = ClusterMemberPost.from_dict(cluster_member_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


