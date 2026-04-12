# ResourcesPCIVPD

ResourcesPCIVPD represents VPD entries for a device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | **Dict[str, str]** | Vendor provided key/value pairs. | [optional] 
**product_name** | **str** | Hardware provided product name. | [optional] 

## Example

```python
from pyincusd.models.resources_pcivpd import ResourcesPCIVPD

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesPCIVPD from a JSON string
resources_pcivpd_instance = ResourcesPCIVPD.from_json(json)
# print the JSON string representation of the object
print(ResourcesPCIVPD.to_json())

# convert the object into a dict
resources_pcivpd_dict = resources_pcivpd_instance.to_dict()
# create an instance of ResourcesPCIVPD from a dict
resources_pcivpd_from_dict = ResourcesPCIVPD.from_dict(resources_pcivpd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


