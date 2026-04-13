# ResourcesStorageDisk

ResourcesStorageDisk represents a disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | **int** | Block size | [optional] 
**device** | **str** | Device number | [optional] 
**device_id** | **str** | Device by-id identifier | [optional] 
**device_path** | **str** | Device by-path identifier | [optional] 
**firmware_version** | **str** | Current firmware version | [optional] 
**id** | **str** | ID of the disk (device name) | [optional] 
**model** | **str** | Disk model name | [optional] 
**numa_node** | **int** | NUMA node the disk is a part of | [optional] 
**partitions** | [**List[ResourcesStorageDiskPartition]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post19/docs/ResourcesStorageDiskPartition.md) | List of partitions | [optional] 
**pci_address** | **str** | PCI address | [optional] 
**read_only** | **bool** | Whether the disk is read-only | [optional] 
**removable** | **bool** | Whether the disk is removable (hot-plug) | [optional] 
**rpm** | **int** | Rotation speed (RPM) | [optional] 
**serial** | **str** | Serial number | [optional] 
**size** | **int** | Total size of the disk (bytes) | [optional] 
**type** | **str** | Storage type | [optional] 
**usb_address** | **str** | USB address | [optional] 
**wwn** | **str** | WWN identifier | [optional] 

## Example

```python
from pyincusd.models.resources_storage_disk import ResourcesStorageDisk

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesStorageDisk from a JSON string
resources_storage_disk_instance = ResourcesStorageDisk.from_json(json)
# print the JSON string representation of the object
print(ResourcesStorageDisk.to_json())

# convert the object into a dict
resources_storage_disk_dict = resources_storage_disk_instance.to_dict()
# create an instance of ResourcesStorageDisk from a dict
resources_storage_disk_from_dict = ResourcesStorageDisk.from_dict(resources_storage_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


