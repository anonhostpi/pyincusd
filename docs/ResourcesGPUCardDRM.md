# ResourcesGPUCardDRM

ResourcesGPUCardDRM represents the Linux DRM configuration of the GPU

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_device** | **str** | Card device number | [optional] 
**card_name** | **str** | Card device name | [optional] 
**control_device** | **str** | Control device number | [optional] 
**control_name** | **str** | Control device name | [optional] 
**id** | **int** | DRM card ID | [optional] 
**render_device** | **str** | Render device number | [optional] 
**render_name** | **str** | Render device name | [optional] 

## Example

```python
from pyincusd.models.resources_gpu_card_drm import ResourcesGPUCardDRM

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesGPUCardDRM from a JSON string
resources_gpu_card_drm_instance = ResourcesGPUCardDRM.from_json(json)
# print the JSON string representation of the object
print(ResourcesGPUCardDRM.to_json())

# convert the object into a dict
resources_gpu_card_drm_dict = resources_gpu_card_drm_instance.to_dict()
# create an instance of ResourcesGPUCardDRM from a dict
resources_gpu_card_drm_from_dict = ResourcesGPUCardDRM.from_dict(resources_gpu_card_drm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


