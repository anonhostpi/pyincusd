# InstanceState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**InstanceStateCPU**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/InstanceStateCPU.md) |  | [optional] 
**disk** | [**Dict[str, InstanceStateDisk]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/InstanceStateDisk.md) | Disk usage key/value pairs | [optional] 
**memory** | [**InstanceStateMemory**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/InstanceStateMemory.md) |  | [optional] 
**network** | [**Dict[str, InstanceStateNetwork]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/InstanceStateNetwork.md) | Network usage key/value pairs | [optional] 
**os_info** | [**InstanceStateOSInfo**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/InstanceStateOSInfo.md) |  | [optional] 
**pid** | **int** | PID of the runtime | [optional] 
**processes** | **int** | Number of processes in the instance | [optional] 
**started_at** | **datetime** | The time that the instance started at  API extension: instance_state_started_at. | [optional] 
**status** | **str** | Current status (Running, Stopped, Frozen or Error) | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from pyincusd.models.instance_state import InstanceState

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceState from a JSON string
instance_state_instance = InstanceState.from_json(json)
# print the JSON string representation of the object
print(InstanceState.to_json())

# convert the object into a dict
instance_state_dict = instance_state_instance.to_dict()
# create an instance of InstanceState from a dict
instance_state_from_dict = InstanceState.from_dict(instance_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


