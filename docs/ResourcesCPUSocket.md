# ResourcesCPUSocket

ResourcesCPUSocket represents a CPU socket on the system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_sizes** | [**ResourcesCPUAddressSizes**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/ResourcesCPUAddressSizes.md) |  | [optional] 
**cache** | [**List[ResourcesCPUCache]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/ResourcesCPUCache.md) | List of CPU caches | [optional] 
**cores** | [**List[ResourcesCPUCore]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post14/docs/ResourcesCPUCore.md) | List of CPU cores | [optional] 
**frequency** | **int** | Current CPU frequency (Mhz) | [optional] 
**frequency_minimum** | **int** | Minimum CPU frequency (Mhz) | [optional] 
**frequency_turbo** | **int** | Maximum CPU frequency (Mhz) | [optional] 
**name** | **str** | Product name | [optional] 
**socket** | **int** | Socket number | [optional] 
**vendor** | **str** | Vendor name | [optional] 

## Example

```python
from pyincusd.models.resources_cpu_socket import ResourcesCPUSocket

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesCPUSocket from a JSON string
resources_cpu_socket_instance = ResourcesCPUSocket.from_json(json)
# print the JSON string representation of the object
print(ResourcesCPUSocket.to_json())

# convert the object into a dict
resources_cpu_socket_dict = resources_cpu_socket_instance.to_dict()
# create an instance of ResourcesCPUSocket from a dict
resources_cpu_socket_from_dict = ResourcesCPUSocket.from_dict(resources_cpu_socket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


