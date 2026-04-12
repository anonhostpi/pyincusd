# StoragePoolVolumesTypeBackupsGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[StorageVolumeBackup]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post12/docs/StorageVolumeBackup.md) | List of storage volume backups | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.storage_pool_volumes_type_backups_get_recursion1200_response import StoragePoolVolumesTypeBackupsGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolVolumesTypeBackupsGetRecursion1200Response from a JSON string
storage_pool_volumes_type_backups_get_recursion1200_response_instance = StoragePoolVolumesTypeBackupsGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(StoragePoolVolumesTypeBackupsGetRecursion1200Response.to_json())

# convert the object into a dict
storage_pool_volumes_type_backups_get_recursion1200_response_dict = storage_pool_volumes_type_backups_get_recursion1200_response_instance.to_dict()
# create an instance of StoragePoolVolumesTypeBackupsGetRecursion1200Response from a dict
storage_pool_volumes_type_backups_get_recursion1200_response_from_dict = StoragePoolVolumesTypeBackupsGetRecursion1200Response.from_dict(storage_pool_volumes_type_backups_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


