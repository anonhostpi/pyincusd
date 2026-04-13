# NetworkACL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | ACL configuration map (refer to doc/network-acls.md) | [optional] 
**description** | **str** | Description of the ACL | [optional] 
**egress** | [**List[NetworkACLRule]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkACLRule.md) | List of egress rules (order independent) | [optional] 
**ingress** | [**List[NetworkACLRule]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/NetworkACLRule.md) | List of ingress rules (order independent) | [optional] 
**name** | **str** | The new name for the ACL | [optional] 
**project** | **str** | Project name | [optional] 
**used_by** | **List[str]** | List of URLs of objects using this profile | [optional] [readonly] 

## Example

```python
from pyincusd.models.network_acl import NetworkACL

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkACL from a JSON string
network_acl_instance = NetworkACL.from_json(json)
# print the JSON string representation of the object
print(NetworkACL.to_json())

# convert the object into a dict
network_acl_dict = network_acl_instance.to_dict()
# create an instance of NetworkACL from a dict
network_acl_from_dict = NetworkACL.from_dict(network_acl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


