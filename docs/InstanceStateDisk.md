# InstanceStateDisk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total size in bytes | [optional] 
**usage** | **int** | Disk usage in bytes | [optional] 

## Example

```python
from pyincusd.models.instance_state_disk import InstanceStateDisk

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStateDisk from a JSON string
instance_state_disk_instance = InstanceStateDisk.from_json(json)
# print the JSON string representation of the object
print(InstanceStateDisk.to_json())

# convert the object into a dict
instance_state_disk_dict = instance_state_disk_instance.to_dict()
# create an instance of InstanceStateDisk from a dict
instance_state_disk_from_dict = InstanceStateDisk.from_dict(instance_state_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


