# ClusterMemberJoinToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | The addresses of existing online cluster members | [optional] 
**expires_at** | **datetime** | The token&#39;s expiry date. | [optional] 
**fingerprint** | **str** | The fingerprint of the network certificate | [optional] 
**secret** | **str** | The random join secret. | [optional] 
**server_name** | **str** | The name of the new cluster member | [optional] 

## Example

```python
from pyincusd.models.cluster_member_join_token import ClusterMemberJoinToken

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMemberJoinToken from a JSON string
cluster_member_join_token_instance = ClusterMemberJoinToken.from_json(json)
# print the JSON string representation of the object
print(ClusterMemberJoinToken.to_json())

# convert the object into a dict
cluster_member_join_token_dict = cluster_member_join_token_instance.to_dict()
# create an instance of ClusterMemberJoinToken from a dict
cluster_member_join_token_from_dict = ClusterMemberJoinToken.from_dict(cluster_member_join_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


