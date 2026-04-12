# NetworkZonesPost

NetworkZonesPost represents the fields of a new network zone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Zone configuration map (refer to doc/network-zones.md) | [optional] 
**description** | **str** | Description of the network zone | [optional] 
**name** | **str** | The name of the zone (DNS domain name) | [optional] 

## Example

```python
from pyincusd.models.network_zones_post import NetworkZonesPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZonesPost from a JSON string
network_zones_post_instance = NetworkZonesPost.from_json(json)
# print the JSON string representation of the object
print(NetworkZonesPost.to_json())

# convert the object into a dict
network_zones_post_dict = network_zones_post_instance.to_dict()
# create an instance of NetworkZonesPost from a dict
network_zones_post_from_dict = NetworkZonesPost.from_dict(network_zones_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


