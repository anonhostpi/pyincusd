# InstanceSnapshotsGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **List[str]** | List of endpoints | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.instance_snapshots_get200_response import InstanceSnapshotsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceSnapshotsGet200Response from a JSON string
instance_snapshots_get200_response_instance = InstanceSnapshotsGet200Response.from_json(json)
# print the JSON string representation of the object
print(InstanceSnapshotsGet200Response.to_json())

# convert the object into a dict
instance_snapshots_get200_response_dict = instance_snapshots_get200_response_instance.to_dict()
# create an instance of InstanceSnapshotsGet200Response from a dict
instance_snapshots_get200_response_from_dict = InstanceSnapshotsGet200Response.from_dict(instance_snapshots_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


