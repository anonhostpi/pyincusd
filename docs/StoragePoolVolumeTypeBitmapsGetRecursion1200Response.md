# StoragePoolVolumeTypeBitmapsGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[StorageVolumeBitmap]**](https://github.com/anonhostpi/pyincusd/blob/v7.1.0/docs/StorageVolumeBitmap.md) | List of storage volume bitmaps | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.storage_pool_volume_type_bitmaps_get_recursion1200_response import StoragePoolVolumeTypeBitmapsGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePoolVolumeTypeBitmapsGetRecursion1200Response from a JSON string
storage_pool_volume_type_bitmaps_get_recursion1200_response_instance = StoragePoolVolumeTypeBitmapsGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(StoragePoolVolumeTypeBitmapsGetRecursion1200Response.to_json())

# convert the object into a dict
storage_pool_volume_type_bitmaps_get_recursion1200_response_dict = storage_pool_volume_type_bitmaps_get_recursion1200_response_instance.to_dict()
# create an instance of StoragePoolVolumeTypeBitmapsGetRecursion1200Response from a dict
storage_pool_volume_type_bitmaps_get_recursion1200_response_from_dict = StoragePoolVolumeTypeBitmapsGetRecursion1200Response.from_dict(storage_pool_volume_type_bitmaps_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


