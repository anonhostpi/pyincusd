# ClusterMemberConfigKey

The Value field is empty when getting clustering information with GET 1.0/cluster, and should be filled by the joining server when performing a PUT 1.0/cluster join request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A human friendly description key | [optional] 
**entity** | **str** | The kind of configuration key (network, storage-pool, ...) | [optional] 
**key** | **str** | The name of the key | [optional] 
**name** | **str** | The name of the object requiring this key | [optional] 
**value** | **str** | The value on the answering cluster member | [optional] 

## Example

```python
from pyincusd.models.cluster_member_config_key import ClusterMemberConfigKey

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMemberConfigKey from a JSON string
cluster_member_config_key_instance = ClusterMemberConfigKey.from_json(json)
# print the JSON string representation of the object
print(ClusterMemberConfigKey.to_json())

# convert the object into a dict
cluster_member_config_key_dict = cluster_member_config_key_instance.to_dict()
# create an instance of ClusterMemberConfigKey from a dict
cluster_member_config_key_from_dict = ClusterMemberConfigKey.from_dict(cluster_member_config_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


