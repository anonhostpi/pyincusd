# NetworkForward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Forward configuration map (refer to doc/network-forwards.md) | [optional] 
**description** | **str** | Description of the forward listen IP | [optional] 
**listen_address** | **str** | The listen address of the forward | [optional] 
**location** | **str** | What cluster member this record was found on | [optional] 
**ports** | [**List[NetworkForwardPort]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post4/docs/NetworkForwardPort.md) | Port forwards (optional) | [optional] 

## Example

```python
from pyincusd.models.network_forward import NetworkForward

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkForward from a JSON string
network_forward_instance = NetworkForward.from_json(json)
# print the JSON string representation of the object
print(NetworkForward.to_json())

# convert the object into a dict
network_forward_dict = network_forward_instance.to_dict()
# create an instance of NetworkForward from a dict
network_forward_from_dict = NetworkForward.from_dict(network_forward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


