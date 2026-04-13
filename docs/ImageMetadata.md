# ImageMetadata

ImageMetadata represents image metadata (used in image tarball)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | Architecture name | [optional] 
**creation_date** | **int** | Image creation data (as UNIX epoch) | [optional] 
**expiry_date** | **int** | Image expiry data (as UNIX epoch) | [optional] 
**properties** | **Dict[str, str]** | Descriptive properties | [optional] 
**templates** | [**Dict[str, ImageMetadataTemplate]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post17/docs/ImageMetadataTemplate.md) | Template for files in the image | [optional] 

## Example

```python
from pyincusd.models.image_metadata import ImageMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ImageMetadata from a JSON string
image_metadata_instance = ImageMetadata.from_json(json)
# print the JSON string representation of the object
print(ImageMetadata.to_json())

# convert the object into a dict
image_metadata_dict = image_metadata_instance.to_dict()
# create an instance of ImageMetadata from a dict
image_metadata_from_dict = ImageMetadata.from_dict(image_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


