# InstanceRebuildPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**InstanceSource**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/InstanceSource.md) |  | [optional] 

## Example

```python
from pyincusd.models.instance_rebuild_post import InstanceRebuildPost

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceRebuildPost from a JSON string
instance_rebuild_post_instance = InstanceRebuildPost.from_json(json)
# print the JSON string representation of the object
print(InstanceRebuildPost.to_json())

# convert the object into a dict
instance_rebuild_post_dict = instance_rebuild_post_instance.to_dict()
# create an instance of InstanceRebuildPost from a dict
instance_rebuild_post_from_dict = InstanceRebuildPost.from_dict(instance_rebuild_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


