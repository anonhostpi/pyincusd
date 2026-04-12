# ResourcesCPUAddressSizes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physical_bits** | **int** |  | [optional] 
**virtual_bits** | **int** |  | [optional] 

## Example

```python
from pyincusd.models.resources_cpu_address_sizes import ResourcesCPUAddressSizes

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesCPUAddressSizes from a JSON string
resources_cpu_address_sizes_instance = ResourcesCPUAddressSizes.from_json(json)
# print the JSON string representation of the object
print(ResourcesCPUAddressSizes.to_json())

# convert the object into a dict
resources_cpu_address_sizes_dict = resources_cpu_address_sizes_instance.to_dict()
# create an instance of ResourcesCPUAddressSizes from a dict
resources_cpu_address_sizes_from_dict = ResourcesCPUAddressSizes.from_dict(resources_cpu_address_sizes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


