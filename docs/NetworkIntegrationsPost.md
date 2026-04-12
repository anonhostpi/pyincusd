# NetworkIntegrationsPost

NetworkIntegrationsPost represents the fields of a new network integration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Integration configuration map (refer to doc/network-integrations.md) | [optional] 
**description** | **str** | Description of the network integration | [optional] 
**name** | **str** | The name of the integration | [optional] 
**type** | **str** | The type of integration | [optional] 

## Example

```python
from pyincusd.models.network_integrations_post import NetworkIntegrationsPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkIntegrationsPost from a JSON string
network_integrations_post_instance = NetworkIntegrationsPost.from_json(json)
# print the JSON string representation of the object
print(NetworkIntegrationsPost.to_json())

# convert the object into a dict
network_integrations_post_dict = network_integrations_post_instance.to_dict()
# create an instance of NetworkIntegrationsPost from a dict
network_integrations_post_from_dict = NetworkIntegrationsPost.from_dict(network_integrations_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


