# StoragePool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Storage pool configuration map (refer to doc/storage.md) | [optional] 
**description** | **str** | Description of the storage pool | [optional] 
**driver** | **str** | Storage pool driver (btrfs, ceph, cephfs, cephobject, dir, lvm, lvmcluster or zfs) | [optional] 
**locations** | **List[str]** | Cluster members on which the storage pool has been defined | [optional] [readonly] 
**name** | **str** | Storage pool name | [optional] 
**status** | **str** | Pool status (Pending, Created, Errored or Unknown) | [optional] [readonly] 
**used_by** | **List[str]** | List of URLs of objects using this storage pool | [optional] 

## Example

```python
from pyincusd.models.storage_pool import StoragePool

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePool from a JSON string
storage_pool_instance = StoragePool.from_json(json)
# print the JSON string representation of the object
print(StoragePool.to_json())

# convert the object into a dict
storage_pool_dict = storage_pool_instance.to_dict()
# create an instance of StoragePool from a dict
storage_pool_from_dict = StoragePool.from_dict(storage_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


