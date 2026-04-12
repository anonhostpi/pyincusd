# InstancesPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | Architecture name | [optional] 
**config** | **object** | Instance configuration (see doc/instances.md) | [optional] 
**description** | **str** | Instance description | [optional] 
**devices** | **object** | Instance devices (see doc/instances.md) | [optional] 
**disk_only** | **bool** | Whether only the instances disk should be restored | [optional] 
**ephemeral** | **bool** | Whether the instance is ephemeral (deleted on shutdown) | [optional] 
**instance_type** | **str** | Cloud instance type (AWS, GCP, Azure, ...) to emulate with limits | [optional] 
**name** | **str** | Instance name | [optional] 
**profiles** | **List[str]** | List of profiles applied to the instance | [optional] 
**restore** | **str** | If set, instance will be restored to the provided snapshot name | [optional] 
**source** | [**InstanceSource**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post9/docs/InstanceSource.md) |  | [optional] 
**start** | **bool** | Whether to start the instance after creation | [optional] 
**stateful** | **bool** | Whether the instance currently has saved state on disk | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pyincusd.models.instances_post import InstancesPost

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesPost from a JSON string
instances_post_instance = InstancesPost.from_json(json)
# print the JSON string representation of the object
print(InstancesPost.to_json())

# convert the object into a dict
instances_post_dict = instances_post_instance.to_dict()
# create an instance of InstancesPost from a dict
instances_post_from_dict = InstancesPost.from_dict(instances_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


