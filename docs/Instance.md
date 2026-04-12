# Instance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | Architecture name | [optional] 
**config** | **object** | Instance configuration (see doc/instances.md) | [optional] 
**created_at** | **datetime** | Instance creation timestamp | [optional] 
**description** | **str** | Instance description | [optional] 
**devices** | **object** | Instance devices (see doc/instances.md) | [optional] 
**disk_only** | **bool** | Whether only the instances disk should be restored | [optional] 
**ephemeral** | **bool** | Whether the instance is ephemeral (deleted on shutdown) | [optional] 
**expanded_config** | **object** | Expanded configuration (all profiles and local config merged) | [optional] 
**expanded_devices** | **object** | Expanded devices (all profiles and local devices merged) | [optional] 
**last_used_at** | **datetime** | Last start timestamp | [optional] 
**location** | **str** | What cluster member this instance is located on | [optional] 
**name** | **str** | Instance name | [optional] 
**profiles** | **List[str]** | List of profiles applied to the instance | [optional] 
**project** | **str** | Instance project name | [optional] 
**restore** | **str** | If set, instance will be restored to the provided snapshot name | [optional] 
**stateful** | **bool** | Whether the instance currently has saved state on disk | [optional] 
**status** | **str** | Instance status (see instance_state) | [optional] 
**status_code** | **int** |  | [optional] 
**type** | **str** | The type of instance (container or virtual-machine) | [optional] 

## Example

```python
from pyincusd.models.instance import Instance

# TODO update the JSON string below
json = "{}"
# create an instance of Instance from a JSON string
instance_instance = Instance.from_json(json)
# print the JSON string representation of the object
print(Instance.to_json())

# convert the object into a dict
instance_dict = instance_instance.to_dict()
# create an instance of Instance from a dict
instance_from_dict = Instance.from_dict(instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


