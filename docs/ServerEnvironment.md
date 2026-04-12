# ServerEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | List of addresses the server is listening on | [optional] 
**architectures** | **List[str]** | List of architectures supported by the server | [optional] 
**certificate** | **str** | Server certificate as PEM encoded X509 | [optional] 
**certificate_fingerprint** | **str** | Server certificate fingerprint as SHA256 | [optional] 
**driver** | **str** | List of supported instance drivers (separate by \&quot; | \&quot;) | [optional] 
**driver_version** | **str** | List of supported instance driver versions (separate by \&quot; | \&quot;) | [optional] 
**firewall** | **str** | Current firewall driver | [optional] 
**kernel** | **str** | OS kernel name | [optional] 
**kernel_architecture** | **str** | OS kernel architecture | [optional] 
**kernel_features** | **Dict[str, str]** | Map of kernel features that were tested on startup | [optional] 
**kernel_version** | **str** | Kernel version | [optional] 
**lxc_features** | **Dict[str, str]** | Map of LXC features that were tested on startup | [optional] 
**os_name** | **str** | Name of the operating system (Linux distribution) | [optional] 
**os_version** | **str** | Version of the operating system (Linux distribution) | [optional] 
**project** | **str** | Current project name | [optional] 
**server** | **str** | Server implementation name | [optional] 
**server_clustered** | **bool** | Whether the server is part of a cluster | [optional] 
**server_event_mode** | **str** | Mode that the event distribution subsystem is operating in on this server. Either \&quot;full-mesh\&quot;, \&quot;hub-server\&quot; or \&quot;hub-client\&quot;. | [optional] 
**server_name** | **str** | Server hostname | [optional] 
**server_pid** | **int** | PID of the daemon | [optional] 
**server_version** | **str** | Server version | [optional] 
**storage** | **str** | List of active storage drivers (separate by \&quot; | \&quot;) | [optional] 
**storage_supported_drivers** | [**List[ServerStorageDriverInfo]**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerStorageDriverInfo.md) | List of supported storage drivers | [optional] 
**storage_version** | **str** | List of active storage driver versions (separate by \&quot; | \&quot;) | [optional] 

## Example

```python
from pyincusd.models.server_environment import ServerEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of ServerEnvironment from a JSON string
server_environment_instance = ServerEnvironment.from_json(json)
# print the JSON string representation of the object
print(ServerEnvironment.to_json())

# convert the object into a dict
server_environment_dict = server_environment_instance.to_dict()
# create an instance of ServerEnvironment from a dict
server_environment_from_dict = ServerEnvironment.from_dict(server_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


