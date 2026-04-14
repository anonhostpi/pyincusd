# InstancesGetRecursion1200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[Instance]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post21/docs/Instance.md) | List of instances | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.instances_get_recursion1200_response import InstancesGetRecursion1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesGetRecursion1200Response from a JSON string
instances_get_recursion1200_response_instance = InstancesGetRecursion1200Response.from_json(json)
# print the JSON string representation of the object
print(InstancesGetRecursion1200Response.to_json())

# convert the object into a dict
instances_get_recursion1200_response_dict = instances_get_recursion1200_response_instance.to_dict()
# create an instance of InstancesGetRecursion1200Response from a dict
instances_get_recursion1200_response_from_dict = InstancesGetRecursion1200Response.from_dict(instances_get_recursion1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


