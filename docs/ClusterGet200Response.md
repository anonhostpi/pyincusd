# ClusterGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Cluster**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/Cluster.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.cluster_get200_response import ClusterGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterGet200Response from a JSON string
cluster_get200_response_instance = ClusterGet200Response.from_json(json)
# print the JSON string representation of the object
print(ClusterGet200Response.to_json())

# convert the object into a dict
cluster_get200_response_dict = cluster_get200_response_instance.to_dict()
# create an instance of ClusterGet200Response from a dict
cluster_get200_response_from_dict = ClusterGet200Response.from_dict(cluster_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


