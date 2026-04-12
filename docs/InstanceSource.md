# InstanceSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Image alias name (for image source) | [optional] 
**allow_inconsistent** | **bool** | Whether to ignore errors when copying (e.g. for volatile files) | [optional] 
**base_image** | **str** | Base image fingerprint (for faster migration) | [optional] 
**certificate** | **str** | Certificate (for remote images or migration) | [optional] 
**fingerprint** | **str** | Image fingerprint (for image source) | [optional] 
**instance_only** | **bool** | Whether the copy should skip the snapshots (for copy) | [optional] 
**live** | **bool** | Whether this is a live migration (for migration) | [optional] 
**mode** | **str** | Whether to use pull or push mode (for migration) | [optional] 
**operation** | **str** | Remote operation URL (for migration) | [optional] 
**project** | **str** | Source project name (for copy and local image) | [optional] 
**properties** | **Dict[str, str]** | Image filters (for image source) | [optional] 
**protocol** | **str** | Protocol name (for remote image) | [optional] 
**refresh** | **bool** | Whether this is refreshing an existing instance (for migration and copy) | [optional] 
**refresh_exclude_older** | **bool** | Whether to exclude source snapshots earlier than latest target snapshot | [optional] 
**secret** | **str** | Remote server secret (for remote private images) | [optional] 
**secrets** | **Dict[str, str]** | Map of migration websockets (for migration) | [optional] 
**server** | **str** | Remote server URL (for remote images) | [optional] 
**source** | **str** | Existing instance name or snapshot (for copy) | [optional] 
**type** | **str** | Source type | [optional] 

## Example

```python
from pyincusd.models.instance_source import InstanceSource

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceSource from a JSON string
instance_source_instance = InstanceSource.from_json(json)
# print the JSON string representation of the object
print(InstanceSource.to_json())

# convert the object into a dict
instance_source_dict = instance_source_instance.to_dict()
# create an instance of InstanceSource from a dict
instance_source_from_dict = InstanceSource.from_dict(instance_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


