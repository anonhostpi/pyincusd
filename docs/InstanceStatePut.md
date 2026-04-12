# InstanceStatePut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | State change action (start, stop, restart, freeze, unfreeze) | [optional] 
**force** | **bool** | Whether to force the action (for stop and restart) | [optional] 
**stateful** | **bool** | Whether to store the runtime state (for stop) | [optional] 
**timeout** | **int** | How long to wait (in s) before giving up (when force isn&#39;t set) | [optional] 

## Example

```python
from pyincusd.models.instance_state_put import InstanceStatePut

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStatePut from a JSON string
instance_state_put_instance = InstanceStatePut.from_json(json)
# print the JSON string representation of the object
print(InstanceStatePut.to_json())

# convert the object into a dict
instance_state_put_dict = instance_state_put_instance.to_dict()
# create an instance of InstanceStatePut from a dict
instance_state_put_from_dict = InstanceStatePut.from_dict(instance_state_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


