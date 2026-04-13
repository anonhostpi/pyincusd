# StorageVolumesPost

StorageVolumesPost represents the fields of a new storage pool volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Storage volume configuration map (refer to doc/storage.md) | [optional] 
**content_type** | **str** | Volume content type (filesystem or block) | [optional] 
**description** | **str** | Description of the storage volume | [optional] 
**name** | **str** | Volume name | [optional] 
**restore** | **str** | Name of a snapshot to restore | [optional] 
**source** | [**StorageVolumeSource**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post18/docs/StorageVolumeSource.md) |  | [optional] 
**type** | **str** | Volume type (container, custom, image or virtual-machine) | [optional] 

## Example

```python
from pyincusd.models.storage_volumes_post import StorageVolumesPost

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolumesPost from a JSON string
storage_volumes_post_instance = StorageVolumesPost.from_json(json)
# print the JSON string representation of the object
print(StorageVolumesPost.to_json())

# convert the object into a dict
storage_volumes_post_dict = storage_volumes_post_instance.to_dict()
# create an instance of StorageVolumesPost from a dict
storage_volumes_post_from_dict = StorageVolumesPost.from_dict(storage_volumes_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


