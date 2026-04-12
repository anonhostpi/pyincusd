# ResourcesNetwork

ResourcesNetwork represents the network cards available on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**List[ResourcesNetworkCard]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post4/docs/ResourcesNetworkCard.md) | List of network cards | [optional] 
**total** | **int** | Total number of network cards | [optional] 

## Example

```python
from pyincusd.models.resources_network import ResourcesNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesNetwork from a JSON string
resources_network_instance = ResourcesNetwork.from_json(json)
# print the JSON string representation of the object
print(ResourcesNetwork.to_json())

# convert the object into a dict
resources_network_dict = resources_network_instance.to_dict()
# create an instance of ResourcesNetwork from a dict
resources_network_from_dict = ResourcesNetwork.from_dict(resources_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


