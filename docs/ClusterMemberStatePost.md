# ClusterMemberStatePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be performed. Valid actions are \&quot;evacuate\&quot; and \&quot;restore\&quot;. | [optional] 
**mode** | **str** | Override the configured evacuation mode. | [optional] 

## Example

```python
from pyincusd.models.cluster_member_state_post import ClusterMemberStatePost

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMemberStatePost from a JSON string
cluster_member_state_post_instance = ClusterMemberStatePost.from_json(json)
# print the JSON string representation of the object
print(ClusterMemberStatePost.to_json())

# convert the object into a dict
cluster_member_state_post_dict = cluster_member_state_post_instance.to_dict()
# create an instance of ClusterMemberStatePost from a dict
cluster_member_state_post_from_dict = ClusterMemberStatePost.from_dict(cluster_member_state_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


