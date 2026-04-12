# NetworkACLPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name for the ACL | [optional] 

## Example

```python
from pyincusd.models.network_acl_post import NetworkACLPost

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkACLPost from a JSON string
network_acl_post_instance = NetworkACLPost.from_json(json)
# print the JSON string representation of the object
print(NetworkACLPost.to_json())

# convert the object into a dict
network_acl_post_dict = network_acl_post_instance.to_dict()
# create an instance of NetworkACLPost from a dict
network_acl_post_from_dict = NetworkACLPost.from_dict(network_acl_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


