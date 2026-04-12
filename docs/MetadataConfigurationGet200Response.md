# MetadataConfigurationGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **str** | The generated metadata configuration | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.metadata_configuration_get200_response import MetadataConfigurationGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataConfigurationGet200Response from a JSON string
metadata_configuration_get200_response_instance = MetadataConfigurationGet200Response.from_json(json)
# print the JSON string representation of the object
print(MetadataConfigurationGet200Response.to_json())

# convert the object into a dict
metadata_configuration_get200_response_dict = metadata_configuration_get200_response_instance.to_dict()
# create an instance of MetadataConfigurationGet200Response from a dict
metadata_configuration_get200_response_from_dict = MetadataConfigurationGet200Response.from_dict(metadata_configuration_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


