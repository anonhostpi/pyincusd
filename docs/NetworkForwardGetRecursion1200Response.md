# NetworkForwardGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[NetworkForward]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post4/docs/NetworkForward.md) | List of network address forwards | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.network_forward_get_recursion1200_response import NetworkForwardGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkForwardGetRecursion1200Response from a JSON string
network_forward_get_recursion1200_response_instance = NetworkForwardGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(NetworkForwardGetRecursion1200Response.to_json())

# convert the object into a dict
network_forward_get_recursion1200_response_dict = network_forward_get_recursion1200_response_instance.to_dict()
# create an instance of NetworkForwardGetRecursion1200Response from a dict
network_forward_get_recursion1200_response_from_dict = NetworkForwardGetRecursion1200Response.from_dict(network_forward_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


