# NetworkZoneRecordsPost

NetworkZoneRecordsPost represents the fields of a new network zone record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Advanced configuration for the record | [optional] 
**description** | **str** | Description of the record | [optional] 
**entries** | [**List[NetworkZoneRecordEntry]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post15/docs/NetworkZoneRecordEntry.md) | Entries in the record | [optional] 
**name** | **str** | The record name in the zone | [optional] 

## Example

```python
from pyincusd.models.network_zone_records_post import NetworkZoneRecordsPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZoneRecordsPost from a JSON string
network_zone_records_post_instance = NetworkZoneRecordsPost.from_json(json)
# print the JSON string representation of the object
print(NetworkZoneRecordsPost.to_json())

# convert the object into a dict
network_zone_records_post_dict = network_zone_records_post_instance.to_dict()
# create an instance of NetworkZoneRecordsPost from a dict
network_zone_records_post_from_dict = NetworkZoneRecordsPost.from_dict(network_zone_records_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


