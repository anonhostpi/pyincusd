# NetworkLease

NetworkLease represents a DHCP lease

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address | [optional] 
**hostname** | **str** | The hostname associated with the record | [optional] 
**hwaddr** | **str** | The MAC address | [optional] 
**location** | **str** | What cluster member this record was found on | [optional] 
**type** | **str** | The type of record (static or dynamic) | [optional] 

## Example

```python
from pyincusd.models.network_lease import NetworkLease

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLease from a JSON string
network_lease_instance = NetworkLease.from_json(json)
# print the JSON string representation of the object
print(NetworkLease.to_json())

# convert the object into a dict
network_lease_dict = network_lease_instance.to_dict()
# create an instance of NetworkLease from a dict
network_lease_from_dict = NetworkLease.from_dict(network_lease_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


