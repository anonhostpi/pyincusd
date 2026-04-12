# NetworkZonePut

NetworkZonePut represents the modifiable fields of a network zone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Zone configuration map (refer to doc/network-zones.md) | [optional] 
**description** | **str** | Description of the network zone | [optional] 

## Example

```python
from pyincusd.models.network_zone_put import NetworkZonePut

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZonePut from a JSON string
network_zone_put_instance = NetworkZonePut.from_json(json)
# print the JSON string representation of the object
print(NetworkZonePut.to_json())

# convert the object into a dict
network_zone_put_dict = network_zone_put_instance.to_dict()
# create an instance of NetworkZonePut from a dict
network_zone_put_from_dict = NetworkZonePut.from_dict(network_zone_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


