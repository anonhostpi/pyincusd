# InstancesGetRecursion2200Response

Sync response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[InstanceFull]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post19/docs/InstanceFull.md) | List of instances | [optional] 
**status** | **str** | Status description | [optional] 
**status_code** | **int** | Status code | [optional] 
**type** | **str** | Response type | [optional] 

## Example

```python
from pyincusd.models.instances_get_recursion2200_response import InstancesGetRecursion2200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesGetRecursion2200Response from a JSON string
instances_get_recursion2200_response_instance = InstancesGetRecursion2200Response.from_json(json)
# print the JSON string representation of the object
print(InstancesGetRecursion2200Response.to_json())

# convert the object into a dict
instances_get_recursion2200_response_dict = instances_get_recursion2200_response_instance.to_dict()
# create an instance of InstancesGetRecursion2200Response from a dict
instances_get_recursion2200_response_from_dict = InstancesGetRecursion2200Response.from_dict(instances_get_recursion2200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


