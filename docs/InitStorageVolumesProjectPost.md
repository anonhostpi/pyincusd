# InitStorageVolumesProjectPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | **str** | Storage pool in which the volume will reside | [optional] 
**project** | **str** | Project in which the volume will reside | [optional] 
**config** | **object** | Storage volume configuration map (refer to doc/storage.md) | [optional] 
**content_type** | **str** | Volume content type (filesystem or block) | [optional] 
**description** | **str** | Description of the storage volume | [optional] 
**name** | **str** | Volume name | [optional] 
**restore** | **str** | Name of a snapshot to restore | [optional] 
**source** | [**StorageVolumeSource**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post3/docs/StorageVolumeSource.md) |  | [optional] 
**type** | **str** | Volume type (container, custom, image or virtual-machine) | [optional] 

## Example

```python
from pyincusd.models.init_storage_volumes_project_post import InitStorageVolumesProjectPost

# TODO update the JSON string below
json = "{}"
# create an instance of InitStorageVolumesProjectPost from a JSON string
init_storage_volumes_project_post_instance = InitStorageVolumesProjectPost.from_json(json)
# print the JSON string representation of the object
print(InitStorageVolumesProjectPost.to_json())

# convert the object into a dict
init_storage_volumes_project_post_dict = init_storage_volumes_project_post_instance.to_dict()
# create an instance of InitStorageVolumesProjectPost from a dict
init_storage_volumes_project_post_from_dict = InitStorageVolumesProjectPost.from_dict(init_storage_volumes_project_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


