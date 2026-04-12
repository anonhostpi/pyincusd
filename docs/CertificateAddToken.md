# CertificateAddToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | The addresses of the server | [optional] 
**client_name** | **str** | The name of the new client | [optional] 
**expires_at** | **datetime** | The token&#39;s expiry date. | [optional] 
**fingerprint** | **str** | The fingerprint of the network certificate | [optional] 
**secret** | **str** | The random join secret | [optional] 

## Example

```python
from pyincusd.models.certificate_add_token import CertificateAddToken

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateAddToken from a JSON string
certificate_add_token_instance = CertificateAddToken.from_json(json)
# print the JSON string representation of the object
print(CertificateAddToken.to_json())

# convert the object into a dict
certificate_add_token_dict = certificate_add_token_instance.to_dict()
# create an instance of CertificateAddToken from a dict
certificate_add_token_from_dict = CertificateAddToken.from_dict(certificate_add_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


