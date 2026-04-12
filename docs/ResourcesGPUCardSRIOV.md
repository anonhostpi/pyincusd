# ResourcesGPUCardSRIOV

ResourcesGPUCardSRIOV represents the SRIOV configuration of the GPU

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_vfs** | **int** | Number of VFs currently configured | [optional] 
**maximum_vfs** | **int** | Maximum number of supported VFs | [optional] 
**vfs** | [**List[ResourcesGPUCard]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post7/docs/ResourcesGPUCard.md) | List of VFs (as additional GPU devices) | [optional] 

## Example

```python
from pyincusd.models.resources_gpu_card_sriov import ResourcesGPUCardSRIOV

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesGPUCardSRIOV from a JSON string
resources_gpu_card_sriov_instance = ResourcesGPUCardSRIOV.from_json(json)
# print the JSON string representation of the object
print(ResourcesGPUCardSRIOV.to_json())

# convert the object into a dict
resources_gpu_card_sriov_dict = resources_gpu_card_sriov_instance.to_dict()
# create an instance of ResourcesGPUCardSRIOV from a dict
resources_gpu_card_sriov_from_dict = ResourcesGPUCardSRIOV.from_dict(resources_gpu_card_sriov_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


