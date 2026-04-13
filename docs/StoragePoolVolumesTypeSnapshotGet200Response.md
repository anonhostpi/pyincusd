# StoragePoolVolumesTypeSnapshotGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**StorageVolumeSnapshot**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/StorageVolumeSnapshot.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.storage_pool_volumes_type_snapshot_get200_response import StoragePoolVolumesTypeSnapshotGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolVolumesTypeSnapshotGet200Response from a JSON string
storage_pool_volumes_type_snapshot_get200_response_instance = StoragePoolVolumesTypeSnapshotGet200Response.from_json(json)
# print the JSON string representation of the object
print(StoragePoolVolumesTypeSnapshotGet200Response.to_json())

# convert the object into a dict
storage_pool_volumes_type_snapshot_get200_response_dict = storage_pool_volumes_type_snapshot_get200_response_instance.to_dict()
# create an instance of StoragePoolVolumesTypeSnapshotGet200Response from a dict
storage_pool_volumes_type_snapshot_get200_response_from_dict = StoragePoolVolumesTypeSnapshotGet200Response.from_dict(storage_pool_volumes_type_snapshot_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


