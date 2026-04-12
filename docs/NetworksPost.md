# NetworksPost

NetworksPost represents the fields of a new network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Network configuration map (refer to doc/networks.md) | [optional] 
**description** | **str** | Description of the profile | [optional] 
**name** | **str** | The name of the new network | [optional] 
**type** | **str** | The network type (refer to doc/networks.md) | [optional] 

## Example

```python
from pyincusd.models.networks_post import NetworksPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworksPost from a JSON string
networks_post_instance = NetworksPost.from_json(json)
# print the JSON string representation of the object
print(NetworksPost.to_json())

# convert the object into a dict
networks_post_dict = networks_post_instance.to_dict()
# create an instance of NetworksPost from a dict
networks_post_from_dict = NetworksPost.from_dict(networks_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


