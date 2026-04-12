# NetworkPeer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Peer configuration map (refer to doc/network-peers.md) | [optional] 
**description** | **str** | Description of the peer | [optional] 
**name** | **str** | Name of the peer | [optional] [readonly] 
**status** | **str** | The state of the peering | [optional] [readonly] 
**target_integration** | **str** | Name of the target integration | [optional] 
**target_network** | **str** | Name of the target network | [optional] [readonly] 
**target_project** | **str** | Name of the target project | [optional] [readonly] 
**type** | **str** | Type of peer | [optional] 
**used_by** | **List[str]** | List of URLs of objects using this network peering | [optional] [readonly] 

## Example

```python
from pyincusd.models.network_peer import NetworkPeer

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPeer from a JSON string
network_peer_instance = NetworkPeer.from_json(json)
# print the JSON string representation of the object
print(NetworkPeer.to_json())

# convert the object into a dict
network_peer_dict = network_peer_instance.to_dict()
# create an instance of NetworkPeer from a dict
network_peer_from_dict = NetworkPeer.from_dict(network_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


