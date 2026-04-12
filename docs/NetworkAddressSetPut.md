# NetworkAddressSetPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | List of addresses in the set | [optional] 
**config** | **object** | Address set configuration map (refer to doc/network-address-sets.md) | [optional] 
**description** | **str** | Description of the address set | [optional] 

## Example

```python
from pyincusd.models.network_address_set_put import NetworkAddressSetPut

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAddressSetPut from a JSON string
network_address_set_put_instance = NetworkAddressSetPut.from_json(json)
# print the JSON string representation of the object
print(NetworkAddressSetPut.to_json())

# convert the object into a dict
network_address_set_put_dict = network_address_set_put_instance.to_dict()
# create an instance of NetworkAddressSetPut from a dict
network_address_set_put_from_dict = NetworkAddressSetPut.from_dict(network_address_set_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


