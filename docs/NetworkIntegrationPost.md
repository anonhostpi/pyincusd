# NetworkIntegrationPost

NetworkIntegrationPost represents the fields required to rename a network integration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name for the network integration | [optional] 

## Example

```python
from pyincusd.models.network_integration_post import NetworkIntegrationPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkIntegrationPost from a JSON string
network_integration_post_instance = NetworkIntegrationPost.from_json(json)
# print the JSON string representation of the object
print(NetworkIntegrationPost.to_json())

# convert the object into a dict
network_integration_post_dict = network_integration_post_instance.to_dict()
# create an instance of NetworkIntegrationPost from a dict
network_integration_post_from_dict = NetworkIntegrationPost.from_dict(network_integration_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


