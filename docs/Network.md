# Network

Network represents a network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Network configuration map (refer to doc/networks.md) | [optional] 
**description** | **str** | Description of the profile | [optional] 
**locations** | **List[str]** | Cluster members on which the network has been defined | [optional] [readonly] 
**managed** | **bool** | Whether this is a managed network | [optional] [readonly] 
**name** | **str** | The network name | [optional] [readonly] 
**project** | **str** | Project name | [optional] 
**status** | **str** | The state of the network (for managed network in clusters) | [optional] [readonly] 
**type** | **str** | The network type | [optional] [readonly] 
**used_by** | **List[str]** | List of URLs of objects using this profile | [optional] [readonly] 

## Example

```python
from pyincusd.models.network import Network

# TODO update the JSON string below
json = "{}"
# create an instance of Network from a JSON string
network_instance = Network.from_json(json)
# print the JSON string representation of the object
print(Network.to_json())

# convert the object into a dict
network_dict = network_instance.to_dict()
# create an instance of Network from a dict
network_from_dict = Network.from_dict(network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


