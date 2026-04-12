# NetworkIntegrationPut

NetworkIntegrationPut represents the modifiable fields of a network integration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Integration configuration map (refer to doc/network-integrations.md) | [optional] 
**description** | **str** | Description of the network integration | [optional] 

## Example

```python
from pyincusd.models.network_integration_put import NetworkIntegrationPut

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkIntegrationPut from a JSON string
network_integration_put_instance = NetworkIntegrationPut.from_json(json)
# print the JSON string representation of the object
print(NetworkIntegrationPut.to_json())

# convert the object into a dict
network_integration_put_dict = network_integration_put_instance.to_dict()
# create an instance of NetworkIntegrationPut from a dict
network_integration_put_from_dict = NetworkIntegrationPut.from_dict(network_integration_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


