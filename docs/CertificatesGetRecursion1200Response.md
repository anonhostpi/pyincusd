# CertificatesGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[Certificate]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/Certificate.md) | List of certificates | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.certificates_get_recursion1200_response import CertificatesGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CertificatesGetRecursion1200Response from a JSON string
certificates_get_recursion1200_response_instance = CertificatesGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(CertificatesGetRecursion1200Response.to_json())

# convert the object into a dict
certificates_get_recursion1200_response_dict = certificates_get_recursion1200_response_instance.to_dict()
# create an instance of CertificatesGetRecursion1200Response from a dict
certificates_get_recursion1200_response_from_dict = CertificatesGetRecursion1200Response.from_dict(certificates_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


