# CertificatePut

CertificatePut represents the modifiable fields of a certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The certificate itself, as PEM encoded X509 (or as base64 encoded X509 on POST) | [optional] 
**description** | **str** | Certificate description | [optional] 
**name** | **str** | Name associated with the certificate | [optional] 
**projects** | **List[str]** | List of allowed projects (applies when restricted) | [optional] 
**restricted** | **bool** | Whether to limit the certificate to listed projects | [optional] 
**type** | **str** | Usage type for the certificate | [optional] 

## Example

```python
from pyincusd.models.certificate_put import CertificatePut

# TODO update the JSON string below
json = "{}"
# create an instance of CertificatePut from a JSON string
certificate_put_instance = CertificatePut.from_json(json)
# print the JSON string representation of the object
print(CertificatePut.to_json())

# convert the object into a dict
certificate_put_dict = certificate_put_instance.to_dict()
# create an instance of CertificatePut from a dict
certificate_put_from_dict = CertificatePut.from_dict(certificate_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


