# NetworkACLRule

Refer to doc/network-acls.md for details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action to perform on rule match | [optional] 
**description** | **str** | Description of the rule | [optional] 
**destination** | **str** | Destination address | [optional] 
**destination_port** | **str** | Destination port | [optional] 
**icmp_code** | **str** | ICMP message code (for ICMP protocol) | [optional] 
**icmp_type** | **str** | Type of ICMP message (for ICMP protocol) | [optional] 
**protocol** | **str** | Protocol | [optional] 
**source** | **str** | Source address | [optional] 
**source_port** | **str** | Source port | [optional] 
**state** | **str** | State of the rule | [optional] 

## Example

```python
from pyincusd.models.network_acl_rule import NetworkACLRule

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkACLRule from a JSON string
network_acl_rule_instance = NetworkACLRule.from_json(json)
# print the JSON string representation of the object
print(NetworkACLRule.to_json())

# convert the object into a dict
network_acl_rule_dict = network_acl_rule_instance.to_dict()
# create an instance of NetworkACLRule from a dict
network_acl_rule_from_dict = NetworkACLRule.from_dict(network_acl_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


