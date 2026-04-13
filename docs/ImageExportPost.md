# ImageExportPost

ImageExportPost represents the fields required to export an image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[ImageAlias]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post19/docs/ImageAlias.md) | List of aliases to set on the image | [optional] 
**certificate** | **str** | Remote server certificate | [optional] 
**profiles** | **List[str]** | List of profiles to use | [optional] 
**project** | **str** | Project name | [optional] 
**secret** | **str** | Image receive secret | [optional] 
**target** | **str** | Target server URL | [optional] 

## Example

```python
from pyincusd.models.image_export_post import ImageExportPost

# TODO update the JSON string below
json = "{}"
# create an instance of ImageExportPost from a JSON string
image_export_post_instance = ImageExportPost.from_json(json)
# print the JSON string representation of the object
print(ImageExportPost.to_json())

# convert the object into a dict
image_export_post_dict = image_export_post_instance.to_dict()
# create an instance of ImageExportPost from a dict
image_export_post_from_dict = ImageExportPost.from_dict(image_export_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


