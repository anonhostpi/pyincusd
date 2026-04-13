# InitClusterPreseed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_address** | **str** | The address of the cluster you wish to join | [optional] 
**cluster_certificate** | **str** | The expected certificate (X509 PEM encoded) for the cluster | [optional] 
**cluster_certificate_path** | **str** | The path to the cluster certificate | [optional] 
**cluster_token** | **str** | The cluster join token for the cluster you&#39;re trying to join | [optional] 
**enabled** | **bool** | Whether clustering is enabled | [optional] 
**member_config** | [**List[ClusterMemberConfigKey]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/ClusterMemberConfigKey.md) | List of member configuration keys (used during join) | [optional] 
**server_address** | **str** | The local address to use for cluster communication | [optional] 
**server_name** | **str** | Name of the cluster member answering the request | [optional] 

## Example

```python
from pyincusd.models.init_cluster_preseed import InitClusterPreseed

# TODO update the JSON string below
json = "{}"
# create an instance of InitClusterPreseed from a JSON string
init_cluster_preseed_instance = InitClusterPreseed.from_json(json)
# print the JSON string representation of the object
print(InitClusterPreseed.to_json())

# convert the object into a dict
init_cluster_preseed_dict = init_cluster_preseed_instance.to_dict()
# create an instance of InitClusterPreseed from a dict
init_cluster_preseed_from_dict = InitClusterPreseed.from_dict(init_cluster_preseed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


