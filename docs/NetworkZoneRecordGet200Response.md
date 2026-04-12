# NetworkZoneRecordGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**NetworkZoneRecord**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post13/docs/NetworkZoneRecord.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.network_zone_record_get200_response import NetworkZoneRecordGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZoneRecordGet200Response from a JSON string
network_zone_record_get200_response_instance = NetworkZoneRecordGet200Response.from_json(json)
# print the JSON string representation of the object
print(NetworkZoneRecordGet200Response.to_json())

# convert the object into a dict
network_zone_record_get200_response_dict = network_zone_record_get200_response_instance.to_dict()
# create an instance of NetworkZoneRecordGet200Response from a dict
network_zone_record_get200_response_from_dict = NetworkZoneRecordGet200Response.from_dict(network_zone_record_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


