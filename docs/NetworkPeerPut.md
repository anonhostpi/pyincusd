# NetworkPeerPut

NetworkPeerPut represents the modifiable fields of a network peering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Peer configuration map (refer to doc/network-peers.md) | [optional] 
**description** | **str** | Description of the peer | [optional] 

## Example

```python
from pyincusd.models.network_peer_put import NetworkPeerPut

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPeerPut from a JSON string
network_peer_put_instance = NetworkPeerPut.from_json(json)
# print the JSON string representation of the object
print(NetworkPeerPut.to_json())

# convert the object into a dict
network_peer_put_dict = network_peer_put_instance.to_dict()
# create an instance of NetworkPeerPut from a dict
network_peer_put_from_dict = NetworkPeerPut.from_dict(network_peer_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


