# ImagesPostSource

ImagesPostSource represents the source of a new image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Source alias to download from | [optional] 
**certificate** | **str** | Source server certificate (if not trusted by system CA) | [optional] 
**fingerprint** | **str** | Source image fingerprint (for type \&quot;image\&quot;) | [optional] 
**image_type** | **str** | Type of image (container or virtual-machine) | [optional] 
**mode** | **str** | Transfer mode (push or pull) | [optional] 
**name** | **str** | Instance name (for type \&quot;instance\&quot; or \&quot;snapshot\&quot;) | [optional] 
**project** | **str** | Source project name | [optional] 
**protocol** | **str** | Source server protocol | [optional] 
**secret** | **str** | Source image server secret token (when downloading private images) | [optional] 
**server** | **str** | URL of the source server | [optional] 
**type** | **str** | Type of image source (instance, snapshot, image or url) | [optional] 
**url** | **str** | Source URL (for type \&quot;url\&quot;) | [optional] 

## Example

```python
from pyincusd.models.images_post_source import ImagesPostSource

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesPostSource from a JSON string
images_post_source_instance = ImagesPostSource.from_json(json)
# print the JSON string representation of the object
print(ImagesPostSource.to_json())

# convert the object into a dict
images_post_source_dict = images_post_source_instance.to_dict()
# create an instance of ImagesPostSource from a dict
images_post_source_from_dict = ImagesPostSource.from_dict(images_post_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


