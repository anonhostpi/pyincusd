# ImageSource

ImageSource represents the source of an image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Source alias to download from | [optional] 
**certificate** | **str** | Source server certificate (if not trusted by system CA) | [optional] 
**image_type** | **str** | Type of image (container or virtual-machine) | [optional] 
**protocol** | **str** | Source server protocol | [optional] 
**server** | **str** | URL of the source server | [optional] 

## Example

```python
from pyincusd.models.image_source import ImageSource

# TODO update the JSON string below
json = "{}"
# create an instance of ImageSource from a JSON string
image_source_instance = ImageSource.from_json(json)
# print the JSON string representation of the object
print(ImageSource.to_json())

# convert the object into a dict
image_source_dict = image_source_instance.to_dict()
# create an instance of ImageSource from a dict
image_source_from_dict = ImageSource.from_dict(image_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


