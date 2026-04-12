# NetworkIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Integration configuration map (refer to doc/network-integrations.md) | [optional] 
**description** | **str** | Description of the network integration | [optional] 
**name** | **str** | The name of the integration | [optional] 
**type** | **str** | The type of integration | [optional] 
**used_by** | **List[str]** | List of URLs of objects using this network integration | [optional] [readonly] 

## Example

```python
from pyincusd.models.network_integration import NetworkIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkIntegration from a JSON string
network_integration_instance = NetworkIntegration.from_json(json)
# print the JSON string representation of the object
print(NetworkIntegration.to_json())

# convert the object into a dict
network_integration_dict = network_integration_instance.to_dict()
# create an instance of NetworkIntegration from a dict
network_integration_from_dict = NetworkIntegration.from_dict(network_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


