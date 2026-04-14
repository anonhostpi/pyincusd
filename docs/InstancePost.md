# InstancePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Instance configuration file. | [optional] 
**devices** | **object** | Instance devices. | [optional] 
**profiles** | **List[str]** | List of profiles applied to the instance. | [optional] 
**allow_inconsistent** | **bool** | AllowInconsistent allow inconsistent copies when migrating. | [optional] 
**instance_only** | **bool** | Whether snapshots should be discarded (migration only) | [optional] 
**live** | **bool** | Whether to perform a live migration (migration only) | [optional] 
**migration** | **bool** | Whether the instance is being migrated to another server | [optional] 
**name** | **str** | New name for the instance | [optional] 
**pool** | **str** | Target pool for local cross-pool move | [optional] 
**project** | **str** | Target project for local cross-project move | [optional] 
**target** | [**InstancePostTarget**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/InstancePostTarget.md) |  | [optional] 

## Example

```python
from pyincusd.models.instance_post import InstancePost

# TODO update the JSON string below
json = "{}"
# create an instance of InstancePost from a JSON string
instance_post_instance = InstancePost.from_json(json)
# print the JSON string representation of the object
print(InstancePost.to_json())

# convert the object into a dict
instance_post_dict = instance_post_instance.to_dict()
# create an instance of InstancePost from a dict
instance_post_from_dict = InstancePost.from_dict(instance_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


