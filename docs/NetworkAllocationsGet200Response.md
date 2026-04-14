# NetworkAllocationsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[NetworkAllocations]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/NetworkAllocations.md) | List of network allocations used by a consuming entity | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.network_allocations_get200_response import NetworkAllocationsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAllocationsGet200Response from a JSON string
network_allocations_get200_response_instance = NetworkAllocationsGet200Response.from_json(json)
# print the JSON string representation of the object
print(NetworkAllocationsGet200Response.to_json())

# convert the object into a dict
network_allocations_get200_response_dict = network_allocations_get200_response_instance.to_dict()
# create an instance of NetworkAllocationsGet200Response from a dict
network_allocations_get200_response_from_dict = NetworkAllocationsGet200Response.from_dict(network_allocations_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


