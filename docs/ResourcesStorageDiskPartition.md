# ResourcesStorageDiskPartition

ResourcesStorageDiskPartition represents a partition on a disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | Device number | [optional] 
**id** | **str** | ID of the partition (device name) | [optional] 
**partition** | **int** | Partition number | [optional] 
**read_only** | **bool** | Whether the partition is read-only | [optional] 
**size** | **int** | Size of the partition (bytes) | [optional] 

## Example

```python
from pyincusd.models.resources_storage_disk_partition import ResourcesStorageDiskPartition

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesStorageDiskPartition from a JSON string
resources_storage_disk_partition_instance = ResourcesStorageDiskPartition.from_json(json)
# print the JSON string representation of the object
print(ResourcesStorageDiskPartition.to_json())

# convert the object into a dict
resources_storage_disk_partition_dict = resources_storage_disk_partition_instance.to_dict()
# create an instance of ResourcesStorageDiskPartition from a dict
resources_storage_disk_partition_from_dict = ResourcesStorageDiskPartition.from_dict(resources_storage_disk_partition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


