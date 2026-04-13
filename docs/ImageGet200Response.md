# ImageGet200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Image**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post16/docs/Image.md) |  | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.image_get200_response import ImageGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImageGet200Response from a JSON string
image_get200_response_instance = ImageGet200Response.from_json(json)
# print the JSON string representation of the object
print(ImageGet200Response.to_json())

# convert the object into a dict
image_get200_response_dict = image_get200_response_instance.to_dict()
# create an instance of ImageGet200Response from a dict
image_get200_response_from_dict = ImageGet200Response.from_dict(image_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


