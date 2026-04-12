# NetworksLeasesGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[NetworkLease]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post5/docs/NetworkLease.md) | List of DHCP leases | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.networks_leases_get200_response import NetworksLeasesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworksLeasesGet200Response from a JSON string
networks_leases_get200_response_instance = NetworksLeasesGet200Response.from_json(json)
# print the JSON string representation of the object
print(NetworksLeasesGet200Response.to_json())

# convert the object into a dict
networks_leases_get200_response_dict = networks_leases_get200_response_instance.to_dict()
# create an instance of NetworksLeasesGet200Response from a dict
networks_leases_get200_response_from_dict = NetworksLeasesGet200Response.from_dict(networks_leases_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


