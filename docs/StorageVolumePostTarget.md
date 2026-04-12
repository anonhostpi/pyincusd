# StorageVolumePostTarget

StorageVolumePostTarget represents the migration target host and operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The certificate of the migration target | [optional] 
**operation** | **str** | Remote operation URL (for migration) | [optional] 
**secrets** | **Dict[str, str]** | Migration websockets credentials | [optional] 

## Example

```python
from pyincusd.models.storage_volume_post_target import StorageVolumePostTarget

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolumePostTarget from a JSON string
storage_volume_post_target_instance = StorageVolumePostTarget.from_json(json)
# print the JSON string representation of the object
print(StorageVolumePostTarget.to_json())

# convert the object into a dict
storage_volume_post_target_dict = storage_volume_post_target_instance.to_dict()
# create an instance of StorageVolumePostTarget from a dict
storage_volume_post_target_from_dict = StorageVolumePostTarget.from_dict(storage_volume_post_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


