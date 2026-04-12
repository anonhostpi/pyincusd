# ResourcesGPUCardMdev

ResourcesGPUCardMdev represents the mediated devices configuration of the GPU

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** | The mechanism used by this device | [optional] 
**available** | **int** | Number of available devices of this profile | [optional] 
**description** | **str** | Profile description | [optional] 
**devices** | **List[str]** | List of active devices (UUIDs) | [optional] 
**name** | **str** | Profile name | [optional] 

## Example

```python
from pyincusd.models.resources_gpu_card_mdev import ResourcesGPUCardMdev

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesGPUCardMdev from a JSON string
resources_gpu_card_mdev_instance = ResourcesGPUCardMdev.from_json(json)
# print the JSON string representation of the object
print(ResourcesGPUCardMdev.to_json())

# convert the object into a dict
resources_gpu_card_mdev_dict = resources_gpu_card_mdev_instance.to_dict()
# create an instance of ResourcesGPUCardMdev from a dict
resources_gpu_card_mdev_from_dict = ResourcesGPUCardMdev.from_dict(resources_gpu_card_mdev_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


