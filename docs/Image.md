# Image

Image represents an image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[ImageAlias]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post7/docs/ImageAlias.md) | List of aliases | [optional] 
**architecture** | **str** | Architecture | [optional] 
**auto_update** | **bool** | Whether the image should auto-update when a new build is available | [optional] 
**cached** | **bool** | Whether the image is an automatically cached remote image | [optional] 
**created_at** | **datetime** | When the image was originally created | [optional] 
**expires_at** | **datetime** | When the image becomes obsolete | [optional] 
**filename** | **str** | Original filename | [optional] 
**fingerprint** | **str** | Full SHA-256 fingerprint | [optional] 
**last_used_at** | **datetime** | Last time the image was used | [optional] 
**profiles** | **List[str]** | List of profiles to use when creating from this image (if none provided by user) | [optional] 
**project** | **str** | Project name | [optional] 
**properties** | **Dict[str, str]** | Descriptive properties | [optional] 
**public** | **bool** | Whether the image is available to unauthenticated users | [optional] 
**size** | **int** | Size of the image in bytes | [optional] 
**type** | **str** | Type of image (container or virtual-machine) | [optional] 
**update_source** | [**ImageSource**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post7/docs/ImageSource.md) |  | [optional] 
**uploaded_at** | **datetime** | When the image was added to this server | [optional] 

## Example

```python
from pyincusd.models.image import Image

# TODO update the JSON string below
json = "{}"
# create an instance of Image from a JSON string
image_instance = Image.from_json(json)
# print the JSON string representation of the object
print(Image.to_json())

# convert the object into a dict
image_dict = image_instance.to_dict()
# create an instance of Image from a dict
image_from_dict = Image.from_dict(image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


