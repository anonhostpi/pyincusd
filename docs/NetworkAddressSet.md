# NetworkAddressSet

Refer to doc/howto/network_address_sets.md for details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | List of addresses in the set | [optional] 
**config** | **object** | Address set configuration map (refer to doc/network-address-sets.md) | [optional] 
**description** | **str** | Description of the address set | [optional] 
**name** | **str** | The new name of the address set | [optional] 
**project** | **str** | Project name | [optional] 
**used_by** | **List[str]** | List of URLs of objects using this profile | [optional] [readonly] 

## Example

```python
from pyincusd.models.network_address_set import NetworkAddressSet

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAddressSet from a JSON string
network_address_set_instance = NetworkAddressSet.from_json(json)
# print the JSON string representation of the object
print(NetworkAddressSet.to_json())

# convert the object into a dict
network_address_set_dict = network_address_set_instance.to_dict()
# create an instance of NetworkAddressSet from a dict
network_address_set_from_dict = NetworkAddressSet.from_dict(network_address_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


