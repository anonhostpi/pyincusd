# NetworkPeersGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **List[str]** | List of endpoints | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.network_peers_get200_response import NetworkPeersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPeersGet200Response from a JSON string
network_peers_get200_response_instance = NetworkPeersGet200Response.from_json(json)
# print the JSON string representation of the object
print(NetworkPeersGet200Response.to_json())

# convert the object into a dict
network_peers_get200_response_dict = network_peers_get200_response_instance.to_dict()
# create an instance of NetworkPeersGet200Response from a dict
network_peers_get200_response_from_dict = NetworkPeersGet200Response.from_dict(network_peers_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


