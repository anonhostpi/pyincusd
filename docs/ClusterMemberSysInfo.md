# ClusterMemberSysInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buffered_ram** | **int** |  | [optional] 
**free_ram** | **int** |  | [optional] 
**free_swap** | **int** |  | [optional] 
**load_averages** | **List[float]** |  | [optional] 
**processes** | **int** |  | [optional] 
**shared_ram** | **int** |  | [optional] 
**total_ram** | **int** |  | [optional] 
**total_swap** | **int** |  | [optional] 
**uptime** | **int** |  | [optional] 

## Example

```python
from pyincusd.models.cluster_member_sys_info import ClusterMemberSysInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMemberSysInfo from a JSON string
cluster_member_sys_info_instance = ClusterMemberSysInfo.from_json(json)
# print the JSON string representation of the object
print(ClusterMemberSysInfo.to_json())

# convert the object into a dict
cluster_member_sys_info_dict = cluster_member_sys_info_instance.to_dict()
# create an instance of ClusterMemberSysInfo from a dict
cluster_member_sys_info_from_dict = ClusterMemberSysInfo.from_dict(cluster_member_sys_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


