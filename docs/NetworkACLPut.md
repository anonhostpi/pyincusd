# NetworkACLPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | ACL configuration map (refer to doc/network-acls.md) | [optional] 
**description** | **str** | Description of the ACL | [optional] 
**egress** | [**List[NetworkACLRule]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkACLRule.md) | List of egress rules (order independent) | [optional] 
**ingress** | [**List[NetworkACLRule]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/NetworkACLRule.md) | List of ingress rules (order independent) | [optional] 

## Example

```python
from pyincusd.models.network_acl_put import NetworkACLPut

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkACLPut from a JSON string
network_acl_put_instance = NetworkACLPut.from_json(json)
# print the JSON string representation of the object
print(NetworkACLPut.to_json())

# convert the object into a dict
network_acl_put_dict = network_acl_put_instance.to_dict()
# create an instance of NetworkACLPut from a dict
network_acl_put_from_dict = NetworkACLPut.from_dict(network_acl_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


