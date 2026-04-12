# ServerStorageDriverInfo

ServerStorageDriverInfo represents the read-only info about a storage driver

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the driver | [optional] 
**remote** | **bool** | Whether the driver has remote volumes | [optional] 
**version** | **str** | Version of the driver | [optional] 

## Example

```python
from pyincusd.models.server_storage_driver_info import ServerStorageDriverInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServerStorageDriverInfo from a JSON string
server_storage_driver_info_instance = ServerStorageDriverInfo.from_json(json)
# print the JSON string representation of the object
print(ServerStorageDriverInfo.to_json())

# convert the object into a dict
server_storage_driver_info_dict = server_storage_driver_info_instance.to_dict()
# create an instance of ServerStorageDriverInfo from a dict
server_storage_driver_info_from_dict = ServerStorageDriverInfo.from_dict(server_storage_driver_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


