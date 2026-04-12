# NetworkPeerGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**NetworkPeer**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworkPeer.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.network_peer_get200_response import NetworkPeerGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPeerGet200Response from a JSON string
network_peer_get200_response_instance = NetworkPeerGet200Response.from_json(json)
# print the JSON string representation of the object
print(NetworkPeerGet200Response.to_json())

# convert the object into a dict
network_peer_get200_response_dict = network_peer_get200_response_instance.to_dict()
# create an instance of NetworkPeerGet200Response from a dict
network_peer_get200_response_from_dict = NetworkPeerGet200Response.from_dict(network_peer_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


