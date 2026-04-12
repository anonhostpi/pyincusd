# ImagesPost

ImagesPost represents the fields available for a new image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[ImageAlias]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post4/docs/ImageAlias.md) | Aliases to add to the image | [optional] 
**auto_update** | **bool** | Whether the image should auto-update when a new build is available | [optional] 
**compression_algorithm** | **str** | Compression algorithm to use when turning an instance into an image | [optional] 
**expires_at** | **datetime** | When the image becomes obsolete | [optional] 
**filename** | **str** | Original filename of the image | [optional] 
**format** | **str** | Type of image format | [optional] 
**profiles** | **List[str]** | List of profiles to use when creating from this image (if none provided by user) | [optional] 
**properties** | **Dict[str, str]** | Descriptive properties | [optional] 
**public** | **bool** | Whether the image is available to unauthenticated users | [optional] 
**source** | [**ImagesPostSource**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post4/docs/ImagesPostSource.md) |  | [optional] 

## Example

```python
from pyincusd.models.images_post import ImagesPost

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesPost from a JSON string
images_post_instance = ImagesPost.from_json(json)
# print the JSON string representation of the object
print(ImagesPost.to_json())

# convert the object into a dict
images_post_dict = images_post_instance.to_dict()
# create an instance of ImagesPost from a dict
images_post_from_dict = ImagesPost.from_dict(images_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


