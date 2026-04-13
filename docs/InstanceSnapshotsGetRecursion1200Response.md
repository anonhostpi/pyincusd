# InstanceSnapshotsGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[InstanceSnapshot]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post15/docs/InstanceSnapshot.md) | List of instance snapshots | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.instance_snapshots_get_recursion1200_response import InstanceSnapshotsGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceSnapshotsGetRecursion1200Response from a JSON string
instance_snapshots_get_recursion1200_response_instance = InstanceSnapshotsGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(InstanceSnapshotsGetRecursion1200Response.to_json())

# convert the object into a dict
instance_snapshots_get_recursion1200_response_dict = instance_snapshots_get_recursion1200_response_instance.to_dict()
# create an instance of InstanceSnapshotsGetRecursion1200Response from a dict
instance_snapshots_get_recursion1200_response_from_dict = InstanceSnapshotsGetRecursion1200Response.from_dict(instance_snapshots_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


