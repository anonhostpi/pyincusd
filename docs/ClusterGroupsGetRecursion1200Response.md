# ClusterGroupsGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[ClusterGroup]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/ClusterGroup.md) | List of cluster groups | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.cluster_groups_get_recursion1200_response import ClusterGroupsGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterGroupsGetRecursion1200Response from a JSON string
cluster_groups_get_recursion1200_response_instance = ClusterGroupsGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(ClusterGroupsGetRecursion1200Response.to_json())

# convert the object into a dict
cluster_groups_get_recursion1200_response_dict = cluster_groups_get_recursion1200_response_instance.to_dict()
# create an instance of ClusterGroupsGetRecursion1200Response from a dict
cluster_groups_get_recursion1200_response_from_dict = ClusterGroupsGetRecursion1200Response.from_dict(cluster_groups_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


