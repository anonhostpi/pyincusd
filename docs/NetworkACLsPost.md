# NetworkACLsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | ACL configuration map (refer to doc/network-acls.md) | [optional] 
**description** | **str** | Description of the ACL | [optional] 
**egress** | [**List[NetworkACLRule]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post7/docs/NetworkACLRule.md) | List of egress rules (order independent) | [optional] 
**ingress** | [**List[NetworkACLRule]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post7/docs/NetworkACLRule.md) | List of ingress rules (order independent) | [optional] 
**name** | **str** | The new name for the ACL | [optional] 

## Example

```python
from pyincusd.models.network_acls_post import NetworkACLsPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkACLsPost from a JSON string
network_acls_post_instance = NetworkACLsPost.from_json(json)
# print the JSON string representation of the object
print(NetworkACLsPost.to_json())

# convert the object into a dict
network_acls_post_dict = network_acls_post_instance.to_dict()
# create an instance of NetworkACLsPost from a dict
network_acls_post_from_dict = NetworkACLsPost.from_dict(network_acls_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


