# NetworkStateAddress

NetworkStateAddress represents a network address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | IP address | [optional] 
**family** | **str** | Address family | [optional] 
**netmask** | **str** | IP netmask (CIDR) | [optional] 
**scope** | **str** | Address scope | [optional] 

## Example

```python
from pyincusd.models.network_state_address import NetworkStateAddress

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkStateAddress from a JSON string
network_state_address_instance = NetworkStateAddress.from_json(json)
# print the JSON string representation of the object
print(NetworkStateAddress.to_json())

# convert the object into a dict
network_state_address_dict = network_state_address_instance.to_dict()
# create an instance of NetworkStateAddress from a dict
network_state_address_from_dict = NetworkStateAddress.from_dict(network_state_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


