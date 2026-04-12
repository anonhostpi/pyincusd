# ClusterGroupGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ClusterGroup**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterGroup.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.cluster_group_get200_response import ClusterGroupGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterGroupGet200Response from a JSON string
cluster_group_get200_response_instance = ClusterGroupGet200Response.from_json(json)
# print the JSON string representation of the object
print(ClusterGroupGet200Response.to_json())

# convert the object into a dict
cluster_group_get200_response_dict = cluster_group_get200_response_instance.to_dict()
# create an instance of ClusterGroupGet200Response from a dict
cluster_group_get200_response_from_dict = ClusterGroupGet200Response.from_dict(cluster_group_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


