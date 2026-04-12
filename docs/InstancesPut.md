# InstancesPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**InstanceStatePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post11/docs/InstanceStatePut.md) |  | [optional] 

## Example

```python
from pyincusd.models.instances_put import InstancesPut

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesPut from a JSON string
instances_put_instance = InstancesPut.from_json(json)
# print the JSON string representation of the object
print(InstancesPut.to_json())

# convert the object into a dict
instances_put_dict = instances_put_instance.to_dict()
# create an instance of InstancesPut from a dict
instances_put_from_dict = InstancesPut.from_dict(instances_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


