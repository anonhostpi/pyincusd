# NetworkForwardsPost

NetworkForwardsPost represents the fields of a new network address forward

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Forward configuration map (refer to doc/network-forwards.md) | [optional] 
**description** | **str** | Description of the forward listen IP | [optional] 
**listen_address** | **str** | The listen address of the forward | [optional] 
**ports** | [**List[NetworkForwardPort]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkForwardPort.md) | Port forwards (optional) | [optional] 

## Example

```python
from pyincusd.models.network_forwards_post import NetworkForwardsPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkForwardsPost from a JSON string
network_forwards_post_instance = NetworkForwardsPost.from_json(json)
# print the JSON string representation of the object
print(NetworkForwardsPost.to_json())

# convert the object into a dict
network_forwards_post_dict = network_forwards_post_instance.to_dict()
# create an instance of NetworkForwardsPost from a dict
network_forwards_post_from_dict = NetworkForwardsPost.from_dict(network_forwards_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


