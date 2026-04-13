# CertificateGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Certificate**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post19/docs/Certificate.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.certificate_get200_response import CertificateGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateGet200Response from a JSON string
certificate_get200_response_instance = CertificateGet200Response.from_json(json)
# print the JSON string representation of the object
print(CertificateGet200Response.to_json())

# convert the object into a dict
certificate_get200_response_dict = certificate_get200_response_instance.to_dict()
# create an instance of CertificateGet200Response from a dict
certificate_get200_response_from_dict = CertificateGet200Response.from_dict(certificate_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


