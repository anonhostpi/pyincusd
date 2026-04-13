# ClusterMembersPost202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Operation**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post19/docs/Operation.md) |  | [optional] 
**operation** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMembersPost202Response from a JSON string
cluster_members_post202_response_instance = ClusterMembersPost202Response.from_json(json)
# print the JSON string representation of the object
print(ClusterMembersPost202Response.to_json())

# convert the object into a dict
cluster_members_post202_response_dict = cluster_members_post202_response_instance.to_dict()
# create an instance of ClusterMembersPost202Response from a dict
cluster_members_post202_response_from_dict = ClusterMembersPost202Response.from_dict(cluster_members_post202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


