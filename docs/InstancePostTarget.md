# InstancePostTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The certificate of the migration target | [optional] 
**operation** | **str** | The operation URL on the remote target | [optional] 
**secrets** | **Dict[str, str]** | Migration websockets credentials | [optional] 

## Example

```python
from pyincusd.models.instance_post_target import InstancePostTarget

# TODO update the JSON string below
json = "{}"
# create an instance of InstancePostTarget from a JSON string
instance_post_target_instance = InstancePostTarget.from_json(json)
# print the JSON string representation of the object
print(InstancePostTarget.to_json())

# convert the object into a dict
instance_post_target_dict = instance_post_target_instance.to_dict()
# create an instance of InstancePostTarget from a dict
instance_post_target_from_dict = InstancePostTarget.from_dict(instance_post_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


