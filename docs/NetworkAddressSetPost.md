# NetworkAddressSetPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the address set | [optional] 

## Example

```python
from pyincusd.models.network_address_set_post import NetworkAddressSetPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAddressSetPost from a JSON string
network_address_set_post_instance = NetworkAddressSetPost.from_json(json)
# print the JSON string representation of the object
print(NetworkAddressSetPost.to_json())

# convert the object into a dict
network_address_set_post_dict = network_address_set_post_instance.to_dict()
# create an instance of NetworkAddressSetPost from a dict
network_address_set_post_from_dict = NetworkAddressSetPost.from_dict(network_address_set_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


