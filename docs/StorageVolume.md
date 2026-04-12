# StorageVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Storage volume configuration map (refer to doc/storage.md) | [optional] 
**content_type** | **str** | Volume content type (filesystem or block) | [optional] 
**created_at** | **datetime** | Volume creation timestamp | [optional] 
**description** | **str** | Description of the storage volume | [optional] 
**location** | **str** | What cluster member this record was found on | [optional] 
**name** | **str** | Volume name | [optional] 
**project** | **str** | Project containing the volume. | [optional] 
**restore** | **str** | Name of a snapshot to restore | [optional] 
**type** | **str** | Volume type | [optional] 
**used_by** | **List[str]** | List of URLs of objects using this storage volume | [optional] 

## Example

```python
from pyincusd.models.storage_volume import StorageVolume

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVolume from a JSON string
storage_volume_instance = StorageVolume.from_json(json)
# print the JSON string representation of the object
print(StorageVolume.to_json())

# convert the object into a dict
storage_volume_dict = storage_volume_instance.to_dict()
# create an instance of StorageVolume from a dict
storage_volume_from_dict = StorageVolume.from_dict(storage_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


