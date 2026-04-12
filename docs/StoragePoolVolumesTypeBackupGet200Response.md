# StoragePoolVolumesTypeBackupGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**StorageVolumeBackup**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post10/docs/StorageVolumeBackup.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.storage_pool_volumes_type_backup_get200_response import StoragePoolVolumesTypeBackupGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolVolumesTypeBackupGet200Response from a JSON string
storage_pool_volumes_type_backup_get200_response_instance = StoragePoolVolumesTypeBackupGet200Response.from_json(json)
# print the JSON string representation of the object
print(StoragePoolVolumesTypeBackupGet200Response.to_json())

# convert the object into a dict
storage_pool_volumes_type_backup_get200_response_dict = storage_pool_volumes_type_backup_get200_response_instance.to_dict()
# create an instance of StoragePoolVolumesTypeBackupGet200Response from a dict
storage_pool_volumes_type_backup_get200_response_from_dict = StoragePoolVolumesTypeBackupGet200Response.from_dict(storage_pool_volumes_type_backup_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


