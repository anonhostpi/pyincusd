# ImagePut

ImagePut represents the modifiable fields of an image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_update** | **bool** | Whether the image should auto-update when a new build is available | [optional] 
**expires_at** | **datetime** | When the image becomes obsolete | [optional] 
**profiles** | **List[str]** | List of profiles to use when creating from this image (if none provided by user) | [optional] 
**properties** | **Dict[str, str]** | Descriptive properties | [optional] 
**public** | **bool** | Whether the image is available to unauthenticated users | [optional] 

## Example

```python
from pyincusd.models.image_put import ImagePut

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePut from a JSON string
image_put_instance = ImagePut.from_json(json)
# print the JSON string representation of the object
print(ImagePut.to_json())

# convert the object into a dict
image_put_dict = image_put_instance.to_dict()
# create an instance of ImagePut from a dict
image_put_from_dict = ImagePut.from_dict(image_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


