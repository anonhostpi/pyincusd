# InstanceStateOSInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | FQDN of the instance. | [optional] 
**hostname** | **str** | Hostname of the instance. | [optional] 
**kernel_version** | **str** | Version of the kernel running in the instance. | [optional] 
**os** | **str** | Operating system running in the instance. | [optional] 
**os_version** | **str** | Version of the operating system. | [optional] 

## Example

```python
from pyincusd.models.instance_state_os_info import InstanceStateOSInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStateOSInfo from a JSON string
instance_state_os_info_instance = InstanceStateOSInfo.from_json(json)
# print the JSON string representation of the object
print(InstanceStateOSInfo.to_json())

# convert the object into a dict
instance_state_os_info_dict = instance_state_os_info_instance.to_dict()
# create an instance of InstanceStateOSInfo from a dict
instance_state_os_info_from_dict = InstanceStateOSInfo.from_dict(instance_state_os_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


