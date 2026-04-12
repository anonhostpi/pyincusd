# ClusterMembersGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[ClusterMember]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/ClusterMember.md) | List of cluster members | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.cluster_members_get_recursion1200_response import ClusterMembersGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMembersGetRecursion1200Response from a JSON string
cluster_members_get_recursion1200_response_instance = ClusterMembersGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(ClusterMembersGetRecursion1200Response.to_json())

# convert the object into a dict
cluster_members_get_recursion1200_response_dict = cluster_members_get_recursion1200_response_instance.to_dict()
# create an instance of ClusterMembersGetRecursion1200Response from a dict
cluster_members_get_recursion1200_response_from_dict = ClusterMembersGetRecursion1200Response.from_dict(cluster_members_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


