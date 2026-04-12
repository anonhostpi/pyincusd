# NetworkAddressSetsGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[NetworkAddressSet]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post2/docs/NetworkAddressSet.md) | List of network address sets | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.network_address_sets_get_recursion1200_response import NetworkAddressSetsGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAddressSetsGetRecursion1200Response from a JSON string
network_address_sets_get_recursion1200_response_instance = NetworkAddressSetsGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(NetworkAddressSetsGetRecursion1200Response.to_json())

# convert the object into a dict
network_address_sets_get_recursion1200_response_dict = network_address_sets_get_recursion1200_response_instance.to_dict()
# create an instance of NetworkAddressSetsGetRecursion1200Response from a dict
network_address_sets_get_recursion1200_response_from_dict = NetworkAddressSetsGetRecursion1200Response.from_dict(network_address_sets_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


