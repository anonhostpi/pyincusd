# NetworksGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[Network]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/Network.md) | List of networks | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.networks_get_recursion1200_response import NetworksGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworksGetRecursion1200Response from a JSON string
networks_get_recursion1200_response_instance = NetworksGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(NetworksGetRecursion1200Response.to_json())

# convert the object into a dict
networks_get_recursion1200_response_dict = networks_get_recursion1200_response_instance.to_dict()
# create an instance of NetworksGetRecursion1200Response from a dict
networks_get_recursion1200_response_from_dict = NetworksGetRecursion1200Response.from_dict(networks_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


