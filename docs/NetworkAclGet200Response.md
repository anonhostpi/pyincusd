# NetworkAclGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**NetworkACL**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post7/docs/NetworkACL.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.network_acl_get200_response import NetworkAclGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAclGet200Response from a JSON string
network_acl_get200_response_instance = NetworkAclGet200Response.from_json(json)
# print the JSON string representation of the object
print(NetworkAclGet200Response.to_json())

# convert the object into a dict
network_acl_get200_response_dict = network_acl_get200_response_instance.to_dict()
# create an instance of NetworkAclGet200Response from a dict
network_acl_get200_response_from_dict = NetworkAclGet200Response.from_dict(network_acl_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


