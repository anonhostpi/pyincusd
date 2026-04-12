# ClusterGroupPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the cluster group | [optional] 

## Example

```python
from pyincusd.models.cluster_group_post import ClusterGroupPost

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterGroupPost from a JSON string
cluster_group_post_instance = ClusterGroupPost.from_json(json)
# print the JSON string representation of the object
print(ClusterGroupPost.to_json())

# convert the object into a dict
cluster_group_post_dict = cluster_group_post_instance.to_dict()
# create an instance of ClusterGroupPost from a dict
cluster_group_post_from_dict = ClusterGroupPost.from_dict(cluster_group_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


