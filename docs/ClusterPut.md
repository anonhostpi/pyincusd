# ClusterPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_address** | **str** | The address of the cluster you wish to join | [optional] 
**cluster_certificate** | **str** | The expected certificate (X509 PEM encoded) for the cluster | [optional] 
**cluster_token** | **str** | The cluster join token for the cluster you&#39;re trying to join | [optional] 
**enabled** | **bool** | Whether clustering is enabled | [optional] 
**member_config** | [**List[ClusterMemberConfigKey]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/ClusterMemberConfigKey.md) | List of member configuration keys (used during join) | [optional] 
**server_address** | **str** | The local address to use for cluster communication | [optional] 
**server_name** | **str** | Name of the cluster member answering the request | [optional] 

## Example

```python
from pyincusd.models.cluster_put import ClusterPut

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterPut from a JSON string
cluster_put_instance = ClusterPut.from_json(json)
# print the JSON string representation of the object
print(ClusterPut.to_json())

# convert the object into a dict
cluster_put_dict = cluster_put_instance.to_dict()
# create an instance of ClusterPut from a dict
cluster_put_from_dict = ClusterPut.from_dict(cluster_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


