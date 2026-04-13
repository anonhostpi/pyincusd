# NetworkZoneRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Advanced configuration for the record | [optional] 
**description** | **str** | Description of the record | [optional] 
**entries** | [**List[NetworkZoneRecordEntry]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/NetworkZoneRecordEntry.md) | Entries in the record | [optional] 
**name** | **str** | The name of the record | [optional] 

## Example

```python
from pyincusd.models.network_zone_record import NetworkZoneRecord

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZoneRecord from a JSON string
network_zone_record_instance = NetworkZoneRecord.from_json(json)
# print the JSON string representation of the object
print(NetworkZoneRecord.to_json())

# convert the object into a dict
network_zone_record_dict = network_zone_record_instance.to_dict()
# create an instance of NetworkZoneRecord from a dict
network_zone_record_from_dict = NetworkZoneRecord.from_dict(network_zone_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


