# Event

Event represents an event entry (over websocket)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Originating cluster member | [optional] 
**metadata** | **object** | JSON encoded metadata (see EventLogging, EventLifecycle or Operation) | [optional] 
**project** | **str** | Project the event belongs to. | [optional] 
**timestamp** | **datetime** | Time at which the event was sent | [optional] 
**type** | **str** | Event type (one of operation, logging or lifecycle) | [optional] 

## Example

```python
from pyincusd.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


