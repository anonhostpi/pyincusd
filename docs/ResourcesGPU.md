# ResourcesGPU

ResourcesGPU represents the GPU resources available on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**List[ResourcesGPUCard]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/ResourcesGPUCard.md) | List of GPUs | [optional] 
**total** | **int** | Total number of GPUs | [optional] 

## Example

```python
from pyincusd.models.resources_gpu import ResourcesGPU

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesGPU from a JSON string
resources_gpu_instance = ResourcesGPU.from_json(json)
# print the JSON string representation of the object
print(ResourcesGPU.to_json())

# convert the object into a dict
resources_gpu_dict = resources_gpu_instance.to_dict()
# create an instance of ResourcesGPU from a dict
resources_gpu_from_dict = ResourcesGPU.from_dict(resources_gpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


