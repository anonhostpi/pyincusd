# CertificatesPost

CertificatesPost represents the fields of a new certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The certificate itself, as PEM encoded X509 (or as base64 encoded X509 on POST) | [optional] 
**description** | **str** | Certificate description | [optional] 
**name** | **str** | Name associated with the certificate | [optional] 
**projects** | **List[str]** | List of allowed projects (applies when restricted) | [optional] 
**restricted** | **bool** | Whether to limit the certificate to listed projects | [optional] 
**token** | **bool** | Whether to create a certificate add token | [optional] 
**trust_token** | **str** | Trust token (used to add an untrusted client) | [optional] 
**type** | **str** | Usage type for the certificate | [optional] 

## Example

```python
from pyincusd.models.certificates_post import CertificatesPost

# TODO update the JSON string below
json = "{}"
# create an instance of CertificatesPost from a JSON string
certificates_post_instance = CertificatesPost.from_json(json)
# print the JSON string representation of the object
print(CertificatesPost.to_json())

# convert the object into a dict
certificates_post_dict = certificates_post_instance.to_dict()
# create an instance of CertificatesPost from a dict
certificates_post_from_dict = CertificatesPost.from_dict(certificates_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


