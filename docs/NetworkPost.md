# NetworkPost

NetworkPost represents the fields required to rename a network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name for the network | [optional] 

## Example

```python
from pyincusd.models.network_post import NetworkPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPost from a JSON string
network_post_instance = NetworkPost.from_json(json)
# print the JSON string representation of the object
print(NetworkPost.to_json())

# convert the object into a dict
network_post_dict = network_post_instance.to_dict()
# create an instance of NetworkPost from a dict
network_post_from_dict = NetworkPost.from_dict(network_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


