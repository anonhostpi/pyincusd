# NetworkZoneRecordPut

NetworkZoneRecordPut represents the modifiable fields of a network zone record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Advanced configuration for the record | [optional] 
**description** | **str** | Description of the record | [optional] 
**entries** | [**List[NetworkZoneRecordEntry]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post22/docs/NetworkZoneRecordEntry.md) | Entries in the record | [optional] 

## Example

```python
from pyincusd.models.network_zone_record_put import NetworkZoneRecordPut

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZoneRecordPut from a JSON string
network_zone_record_put_instance = NetworkZoneRecordPut.from_json(json)
# print the JSON string representation of the object
print(NetworkZoneRecordPut.to_json())

# convert the object into a dict
network_zone_record_put_dict = network_zone_record_put_instance.to_dict()
# create an instance of NetworkZoneRecordPut from a dict
network_zone_record_put_from_dict = NetworkZoneRecordPut.from_dict(network_zone_record_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


