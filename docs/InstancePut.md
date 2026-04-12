# InstancePut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | Architecture name | [optional] 
**config** | **object** | Instance configuration (see doc/instances.md) | [optional] 
**description** | **str** | Instance description | [optional] 
**devices** | **object** | Instance devices (see doc/instances.md) | [optional] 
**disk_only** | **bool** | Whether only the instances disk should be restored | [optional] 
**ephemeral** | **bool** | Whether the instance is ephemeral (deleted on shutdown) | [optional] 
**profiles** | **List[str]** | List of profiles applied to the instance | [optional] 
**restore** | **str** | If set, instance will be restored to the provided snapshot name | [optional] 
**stateful** | **bool** | Whether the instance currently has saved state on disk | [optional] 

## Example

```python
from pyincusd.models.instance_put import InstancePut

# TODO update the JSON string below
json = "{}"
# create an instance of InstancePut from a JSON string
instance_put_instance = InstancePut.from_json(json)
# print the JSON string representation of the object
print(InstancePut.to_json())

# convert the object into a dict
instance_put_dict = instance_put_instance.to_dict()
# create an instance of InstancePut from a dict
instance_put_from_dict = InstancePut.from_dict(instance_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


