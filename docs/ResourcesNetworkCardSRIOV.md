# ResourcesNetworkCardSRIOV

ResourcesNetworkCardSRIOV represents the SRIOV configuration of the network card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_vfs** | **int** | Number of VFs currently configured | [optional] 
**maximum_vfs** | **int** | Maximum number of supported VFs | [optional] 
**vfs** | [**List[ResourcesNetworkCard]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post6/docs/ResourcesNetworkCard.md) | List of VFs (as additional Network devices) | [optional] 

## Example

```python
from pyincusd.models.resources_network_card_sriov import ResourcesNetworkCardSRIOV

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesNetworkCardSRIOV from a JSON string
resources_network_card_sriov_instance = ResourcesNetworkCardSRIOV.from_json(json)
# print the JSON string representation of the object
print(ResourcesNetworkCardSRIOV.to_json())

# convert the object into a dict
resources_network_card_sriov_dict = resources_network_card_sriov_instance.to_dict()
# create an instance of ResourcesNetworkCardSRIOV from a dict
resources_network_card_sriov_from_dict = ResourcesNetworkCardSRIOV.from_dict(resources_network_card_sriov_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


