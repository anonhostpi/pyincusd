# InstanceExecPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **List[str]** | Command and its arguments | [optional] 
**cwd** | **str** | Current working directory for the command | [optional] 
**environment** | **Dict[str, str]** | Additional environment to pass to the command | [optional] 
**group** | **int** | GID of the user to spawn the command as | [optional] 
**height** | **int** | Terminal height in rows (for interactive) | [optional] 
**interactive** | **bool** | Whether the command is to be spawned in interactive mode (singled PTY instead of 3 PIPEs) | [optional] 
**record_output** | **bool** | Whether to capture the output for later download (requires non-interactive) | [optional] 
**user** | **int** | UID of the user to spawn the command as | [optional] 
**wait_for_websocket** | **bool** | Whether to wait for all websockets to be connected before spawning the command | [optional] 
**width** | **int** | Terminal width in characters (for interactive) | [optional] 

## Example

```python
from pyincusd.models.instance_exec_post import InstanceExecPost

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceExecPost from a JSON string
instance_exec_post_instance = InstanceExecPost.from_json(json)
# print the JSON string representation of the object
print(InstanceExecPost.to_json())

# convert the object into a dict
instance_exec_post_dict = instance_exec_post_instance.to_dict()
# create an instance of InstanceExecPost from a dict
instance_exec_post_from_dict = InstanceExecPost.from_dict(instance_exec_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


