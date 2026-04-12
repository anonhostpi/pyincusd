# InitNetworksProjectPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** | Project in which the network will reside | [optional] 
**config** | **object** | Network configuration map (refer to doc/networks.md) | [optional] 
**description** | **str** | Description of the profile | [optional] 
**name** | **str** | The name of the new network | [optional] 
**type** | **str** | The network type (refer to doc/networks.md) | [optional] 

## Example

```python
from pyincusd.models.init_networks_project_post import InitNetworksProjectPost

# TODO update the JSON string below
json = "{}"
# create an instance of InitNetworksProjectPost from a JSON string
init_networks_project_post_instance = InitNetworksProjectPost.from_json(json)
# print the JSON string representation of the object
print(InitNetworksProjectPost.to_json())

# convert the object into a dict
init_networks_project_post_dict = init_networks_project_post_instance.to_dict()
# create an instance of InitNetworksProjectPost from a dict
init_networks_project_post_from_dict = InitNetworksProjectPost.from_dict(init_networks_project_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


