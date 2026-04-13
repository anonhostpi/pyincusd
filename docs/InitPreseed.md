# InitPreseed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**List[CertificatesPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/CertificatesPost.md) | Certificates to add | [optional] 
**cluster** | [**InitClusterPreseed**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/InitClusterPreseed.md) |  | [optional] 
**cluster_groups** | [**List[ClusterGroupsPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ClusterGroupsPost.md) | Cluster groups to add  API extension: init_preseed_cluster_groups. | [optional] 
**config** | **object** | Server configuration map (refer to doc/server.md) | [optional] 
**networks** | [**List[InitNetworksProjectPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/InitNetworksProjectPost.md) | Networks by project to add | [optional] 
**profiles** | [**List[InitProfileProjectPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/InitProfileProjectPost.md) | Profiles to add | [optional] 
**projects** | [**List[ProjectsPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ProjectsPost.md) | Projects to add | [optional] 
**storage_pools** | [**List[StoragePoolsPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/StoragePoolsPost.md) | Storage Pools to add | [optional] 
**storage_volumes** | [**List[InitStorageVolumesProjectPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/InitStorageVolumesProjectPost.md) | Storage Volumes to add | [optional] 

## Example

```python
from pyincusd.models.init_preseed import InitPreseed

# TODO update the JSON string below
json = "{}"
# create an instance of InitPreseed from a JSON string
init_preseed_instance = InitPreseed.from_json(json)
# print the JSON string representation of the object
print(InitPreseed.to_json())

# convert the object into a dict
init_preseed_dict = init_preseed_instance.to_dict()
# create an instance of InitPreseed from a dict
init_preseed_from_dict = InitPreseed.from_dict(init_preseed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


