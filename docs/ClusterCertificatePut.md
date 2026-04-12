# ClusterCertificatePut

ClusterCertificatePut represents the certificate and key pair for all cluster members

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_certificate** | **str** | The new certificate (X509 PEM encoded) for the cluster | [optional] 
**cluster_certificate_key** | **str** | The new certificate key (X509 PEM encoded) for the cluster | [optional] 

## Example

```python
from pyincusd.models.cluster_certificate_put import ClusterCertificatePut

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCertificatePut from a JSON string
cluster_certificate_put_instance = ClusterCertificatePut.from_json(json)
# print the JSON string representation of the object
print(ClusterCertificatePut.to_json())

# convert the object into a dict
cluster_certificate_put_dict = cluster_certificate_put_instance.to_dict()
# create an instance of ClusterCertificatePut from a dict
cluster_certificate_put_from_dict = ClusterCertificatePut.from_dict(cluster_certificate_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


