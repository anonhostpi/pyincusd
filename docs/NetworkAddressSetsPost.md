# NetworkAddressSetsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | List of addresses in the set | [optional] 
**config** | **object** | Address set configuration map (refer to doc/network-address-sets.md) | [optional] 
**description** | **str** | Description of the address set | [optional] 
**name** | **str** | The new name of the address set | [optional] 

## Example

```python
from pyincusd.models.network_address_sets_post import NetworkAddressSetsPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAddressSetsPost from a JSON string
network_address_sets_post_instance = NetworkAddressSetsPost.from_json(json)
# print the JSON string representation of the object
print(NetworkAddressSetsPost.to_json())

# convert the object into a dict
network_address_sets_post_dict = network_address_sets_post_instance.to_dict()
# create an instance of NetworkAddressSetsPost from a dict
network_address_sets_post_from_dict = NetworkAddressSetsPost.from_dict(network_address_sets_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


