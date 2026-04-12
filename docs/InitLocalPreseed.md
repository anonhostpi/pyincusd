# InitLocalPreseed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**List[CertificatesPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/CertificatesPost.md) | Certificates to add | [optional] 
**cluster_groups** | [**List[ClusterGroupsPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterGroupsPost.md) | Cluster groups to add  API extension: init_preseed_cluster_groups. | [optional] 
**config** | **object** | Server configuration map (refer to doc/server.md) | [optional] 
**networks** | [**List[InitNetworksProjectPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InitNetworksProjectPost.md) | Networks by project to add | [optional] 
**profiles** | [**List[InitProfileProjectPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InitProfileProjectPost.md) | Profiles to add | [optional] 
**projects** | [**List[ProjectsPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ProjectsPost.md) | Projects to add | [optional] 
**storage_pools** | [**List[StoragePoolsPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/StoragePoolsPost.md) | Storage Pools to add | [optional] 
**storage_volumes** | [**List[InitStorageVolumesProjectPost]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InitStorageVolumesProjectPost.md) | Storage Volumes to add | [optional] 

## Example

```python
from pyincusd.models.init_local_preseed import InitLocalPreseed

# TODO update the JSON string below
json = "{}"
# create an instance of InitLocalPreseed from a JSON string
init_local_preseed_instance = InitLocalPreseed.from_json(json)
# print the JSON string representation of the object
print(InitLocalPreseed.to_json())

# convert the object into a dict
init_local_preseed_dict = init_local_preseed_instance.to_dict()
# create an instance of InitLocalPreseed from a dict
init_local_preseed_from_dict = InitLocalPreseed.from_dict(init_local_preseed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


