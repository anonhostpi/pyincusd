# ResourcesGPUCardNvidia

ResourcesGPUCardNvidia represents additional information for NVIDIA GPUs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | Architecture (generation) | [optional] 
**brand** | **str** | Brand name | [optional] 
**card_device** | **str** | Card device number | [optional] 
**card_name** | **str** | Card device name | [optional] 
**cuda_version** | **str** | Version of the CUDA API | [optional] 
**model** | **str** | Model name | [optional] 
**nvrm_version** | **str** | Version of the NVRM (usually driver version) | [optional] 
**uuid** | **str** | GPU UUID | [optional] 

## Example

```python
from pyincusd.models.resources_gpu_card_nvidia import ResourcesGPUCardNvidia

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesGPUCardNvidia from a JSON string
resources_gpu_card_nvidia_instance = ResourcesGPUCardNvidia.from_json(json)
# print the JSON string representation of the object
print(ResourcesGPUCardNvidia.to_json())

# convert the object into a dict
resources_gpu_card_nvidia_dict = resources_gpu_card_nvidia_instance.to_dict()
# create an instance of ResourcesGPUCardNvidia from a dict
resources_gpu_card_nvidia_from_dict = ResourcesGPUCardNvidia.from_dict(resources_gpu_card_nvidia_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


