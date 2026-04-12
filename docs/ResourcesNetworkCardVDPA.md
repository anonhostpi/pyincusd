# ResourcesNetworkCardVDPA

ResourcesNetworkCardVDPA represents the VDPA configuration of the network card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | Device identifier of the VDPA device | [optional] 
**name** | **str** | Name of the VDPA device | [optional] 

## Example

```python
from pyincusd.models.resources_network_card_vdpa import ResourcesNetworkCardVDPA

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesNetworkCardVDPA from a JSON string
resources_network_card_vdpa_instance = ResourcesNetworkCardVDPA.from_json(json)
# print the JSON string representation of the object
print(ResourcesNetworkCardVDPA.to_json())

# convert the object into a dict
resources_network_card_vdpa_dict = resources_network_card_vdpa_instance.to_dict()
# create an instance of ResourcesNetworkCardVDPA from a dict
resources_network_card_vdpa_from_dict = ResourcesNetworkCardVDPA.from_dict(resources_network_card_vdpa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


