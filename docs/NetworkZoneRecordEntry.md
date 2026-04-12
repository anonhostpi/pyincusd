# NetworkZoneRecordEntry

NetworkZoneRecordEntry represents the fields in a record entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **int** | TTL for the entry | [optional] 
**type** | **str** | Type of DNS entry | [optional] 
**value** | **str** | Value for the record | [optional] 

## Example

```python
from pyincusd.models.network_zone_record_entry import NetworkZoneRecordEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZoneRecordEntry from a JSON string
network_zone_record_entry_instance = NetworkZoneRecordEntry.from_json(json)
# print the JSON string representation of the object
print(NetworkZoneRecordEntry.to_json())

# convert the object into a dict
network_zone_record_entry_dict = network_zone_record_entry_instance.to_dict()
# create an instance of NetworkZoneRecordEntry from a dict
network_zone_record_entry_from_dict = NetworkZoneRecordEntry.from_dict(network_zone_record_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


