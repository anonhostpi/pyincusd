# NetworkZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Zone configuration map (refer to doc/network-zones.md) | [optional] 
**description** | **str** | Description of the network zone | [optional] 
**name** | **str** | The name of the zone (DNS domain name) | [optional] 
**project** | **str** | Project name | [optional] 
**used_by** | **List[str]** | List of URLs of objects using this network zone | [optional] [readonly] 

## Example

```python
from pyincusd.models.network_zone import NetworkZone

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZone from a JSON string
network_zone_instance = NetworkZone.from_json(json)
# print the JSON string representation of the object
print(NetworkZone.to_json())

# convert the object into a dict
network_zone_dict = network_zone_instance.to_dict()
# create an instance of NetworkZone from a dict
network_zone_from_dict = NetworkZone.from_dict(network_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


