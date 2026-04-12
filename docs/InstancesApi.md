# pyincusd.InstancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_access**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_access) | **GET** /1.0/instances/{name}/access | Get who has access to an instance
[**instance_backup_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_backup_delete) | **DELETE** /1.0/instances/{name}/backups/{backup} | Delete a backup
[**instance_backup_export**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_backup_export) | **GET** /1.0/instances/{name}/backups/{backup}/export | Get the raw backup file(s)
[**instance_backup_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_backup_get) | **GET** /1.0/instances/{name}/backups/{backup} | Get the backup
[**instance_backup_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_backup_post) | **POST** /1.0/instances/{name}/backups/{backup} | Rename a backup
[**instance_backups_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_backups_get) | **GET** /1.0/instances/{name}/backups | Get the backups
[**instance_backups_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_backups_get_recursion1) | **GET** /1.0/instances/{name}/backups?recursion&#x3D;1 | Get the backups
[**instance_backups_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_backups_post) | **POST** /1.0/instances/{name}/backups | Create a backup
[**instance_console_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_console_delete) | **DELETE** /1.0/instances/{name}/console | Clear the console log
[**instance_console_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_console_get) | **GET** /1.0/instances/{name}/console | Get console output
[**instance_console_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_console_post) | **POST** /1.0/instances/{name}/console | Connect to console
[**instance_debug_memory_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_debug_memory_get) | **GET** /1.0/instances/{name}/debug/memory | Get memory debug information of an instance
[**instance_debug_repair_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_debug_repair_post) | **GET** /1.0/instances/{name}/debug/repair | Trigger a repair action on the instance.
[**instance_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_delete) | **DELETE** /1.0/instances/{name} | Delete an instance
[**instance_exec_output_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_exec_output_delete) | **DELETE** /1.0/instances/{name}/logs/exec-output/{filename} | Delete the exec record-output file
[**instance_exec_output_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_exec_output_get) | **GET** /1.0/instances/{name}/logs/exec-output/{filename} | Get the exec-output log file
[**instance_exec_outputs_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_exec_outputs_get) | **GET** /1.0/instances/{name}/logs/exec-output | Get the exec record-output files
[**instance_exec_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_exec_post) | **POST** /1.0/instances/{name}/exec | Run a command
[**instance_files_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_files_delete) | **DELETE** /1.0/instances/{name}/files | Delete a file
[**instance_files_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_files_get) | **GET** /1.0/instances/{name}/files | Get a file
[**instance_files_head**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_files_head) | **HEAD** /1.0/instances/{name}/files | Get metadata for a file
[**instance_files_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_files_post) | **POST** /1.0/instances/{name}/files | Create or replace a file
[**instance_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_get) | **GET** /1.0/instances/{name} | Get the instance
[**instance_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_get_recursion1) | **GET** /1.0/instances/{name}?recursion&#x3D;1 | Get the instance
[**instance_log_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_log_delete) | **DELETE** /1.0/instances/{name}/logs/{filename} | Delete the log file
[**instance_log_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_log_get) | **GET** /1.0/instances/{name}/logs/{filename} | Get the log file
[**instance_logs_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_logs_get) | **GET** /1.0/instances/{name}/logs | Get the log files
[**instance_metadata_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_metadata_get) | **GET** /1.0/instances/{name}/metadata | Get the instance image metadata
[**instance_metadata_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_metadata_patch) | **PATCH** /1.0/instances/{name}/metadata | Partially update the image metadata
[**instance_metadata_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_metadata_put) | **PUT** /1.0/instances/{name}/metadata | Update the image metadata
[**instance_metadata_templates_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_metadata_templates_delete) | **DELETE** /1.0/instances/{name}/metadata/templates | Delete a template file
[**instance_metadata_templates_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_metadata_templates_get) | **GET** /1.0/instances/{name}/metadata/templates | Get the template file names or a specific
[**instance_metadata_templates_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_metadata_templates_post) | **POST** /1.0/instances/{name}/metadata/templates | Create or replace a template file
[**instance_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_patch) | **PATCH** /1.0/instances/{name} | Partially update the instance
[**instance_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_post) | **POST** /1.0/instances/{name} | Rename or move/migrate an instance
[**instance_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_put) | **PUT** /1.0/instances/{name} | Update the instance
[**instance_rebuild_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_rebuild_post) | **POST** /1.0/instances/{name}/rebuild | Rebuild an instance
[**instance_sftp**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_sftp) | **GET** /1.0/instances/{name}/sftp | Get the instance SFTP connection
[**instance_snapshot_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_snapshot_delete) | **DELETE** /1.0/instances/{name}/snapshots/{snapshot} | Delete a snapshot
[**instance_snapshot_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_snapshot_get) | **GET** /1.0/instances/{name}/snapshots/{snapshot} | Get the snapshot
[**instance_snapshot_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_snapshot_patch) | **PATCH** /1.0/instances/{name}/snapshots/{snapshot} | Partially update snapshot
[**instance_snapshot_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_snapshot_post) | **POST** /1.0/instances/{name}/snapshots/{snapshot} | Rename or move/migrate a snapshot
[**instance_snapshot_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_snapshot_put) | **PUT** /1.0/instances/{name}/snapshots/{snapshot} | Update snapshot
[**instance_snapshots_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_snapshots_get) | **GET** /1.0/instances/{name}/snapshots | Get the snapshots
[**instance_snapshots_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_snapshots_get_recursion1) | **GET** /1.0/instances/{name}/snapshots?recursion&#x3D;1 | Get the snapshots
[**instance_snapshots_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_snapshots_post) | **POST** /1.0/instances/{name}/snapshots | Create a snapshot
[**instance_state_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_state_get) | **GET** /1.0/instances/{name}/state | Get the runtime state
[**instance_state_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instance_state_put) | **PUT** /1.0/instances/{name}/state | Change the state
[**instances_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instances_get) | **GET** /1.0/instances | Get the instances
[**instances_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instances_get_recursion1) | **GET** /1.0/instances?recursion&#x3D;1 | Get the instances
[**instances_get_recursion2**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instances_get_recursion2) | **GET** /1.0/instances?recursion&#x3D;2 | Get the instances
[**instances_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instances_post) | **POST** /1.0/instances | Create a new instance
[**instances_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesApi.md#instances_put) | **PUT** /1.0/instances | Bulk instance state update


# **instance_access**
> InstanceAccess200Response instance_access(project=project)

Get who has access to an instance

Gets the access information for the instance.

### Example


```python
import pyincusd
from pyincusd.models.instance_access200_response import InstanceAccess200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get who has access to an instance
        api_response = api_instance.instance_access(project=project)
        print("The response of InstancesApi->instance_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceAccess200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceAccess200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_backup_delete**
> ClusterMembersPost202Response instance_backup_delete(project=project)

Delete a backup

Deletes the instance backup.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete a backup
        api_response = api_instance.instance_backup_delete(project=project)
        print("The response of InstancesApi->instance_backup_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_backup_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_backup_export**
> instance_backup_export(project=project)

Get the raw backup file(s)

Download the raw backup file(s) from the server.

### Example


```python
import pyincusd
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the raw backup file(s)
        api_instance.instance_backup_export(project=project)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_backup_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw image data |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_backup_get**
> InstanceBackupGet200Response instance_backup_get(project=project)

Get the backup

Gets a specific instance backup.

### Example


```python
import pyincusd
from pyincusd.models.instance_backup_get200_response import InstanceBackupGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the backup
        api_response = api_instance.instance_backup_get(project=project)
        print("The response of InstancesApi->instance_backup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_backup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceBackupGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceBackupGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instance backup |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_backup_post**
> ClusterMembersPost202Response instance_backup_post(project=project, backup=backup)

Rename a backup

Renames an instance backup.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instance_backup_post import InstanceBackupPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    backup = pyincusd.InstanceBackupPost() # InstanceBackupPost | Backup rename (optional)

    try:
        # Rename a backup
        api_response = api_instance.instance_backup_post(project=project, backup=backup)
        print("The response of InstancesApi->instance_backup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_backup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **backup** | [**InstanceBackupPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceBackupPost.md)| Backup rename | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_backups_get**
> InstanceBackupsGet200Response instance_backups_get(project=project)

Get the backups

Returns a list of instance backups (URLs).

### Example


```python
import pyincusd
from pyincusd.models.instance_backups_get200_response import InstanceBackupsGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the backups
        api_response = api_instance.instance_backups_get(project=project)
        print("The response of InstancesApi->instance_backups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_backups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceBackupsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceBackupsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_backups_get_recursion1**
> InstanceBackupsGetRecursion1200Response instance_backups_get_recursion1(project=project)

Get the backups

Returns a list of instance backups (structs).

### Example


```python
import pyincusd
from pyincusd.models.instance_backups_get_recursion1200_response import InstanceBackupsGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the backups
        api_response = api_instance.instance_backups_get_recursion1(project=project)
        print("The response of InstancesApi->instance_backups_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_backups_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceBackupsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceBackupsGetRecursion1200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_backups_post**
> ClusterMembersPost202Response instance_backups_post(project=project, backup=backup)

Create a backup

Creates a new backup.

If the `Accept` header is set to `application/octet-stream`, this directly streams the backup
tarball to the client without any intermediate operation.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instance_backups_post import InstanceBackupsPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    backup = pyincusd.InstanceBackupsPost() # InstanceBackupsPost | Backup request (optional)

    try:
        # Create a backup
        api_response = api_instance.instance_backups_post(project=project, backup=backup)
        print("The response of InstancesApi->instance_backups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_backups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **backup** | [**InstanceBackupsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceBackupsPost.md)| Backup request | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_console_delete**
> ServerPut200Response instance_console_delete(project=project)

Clear the console log

Clears the console log buffer.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Clear the console log
        api_response = api_instance.instance_console_delete(project=project)
        print("The response of InstancesApi->instance_console_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_console_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_console_get**
> instance_console_get(project=project, type=type)

Get console output

Gets the console output for the instance either as text log or as vga
screendump.

### Example


```python
import pyincusd
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    type = log # str | Console type (optional) (default to log)

    try:
        # Get console output
        api_instance.instance_console_get(project=project, type=type)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_console_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **type** | **str**| Console type | [optional] [default to log]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Console output either as raw console log or as vga screendump in PNG format depending on the &#x60;type&#x60; parameter provided with the request.  |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_console_post**
> ClusterMembersPost202Response instance_console_post(project=project, console=console)

Connect to console

Connects to the console of an instance.

The returned operation metadata will contain two websockets, one for data and one for control.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instance_console_post import InstanceConsolePost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    console = pyincusd.InstanceConsolePost() # InstanceConsolePost | Console request (optional)

    try:
        # Connect to console
        api_response = api_instance.instance_console_post(project=project, console=console)
        print("The response of InstancesApi->instance_console_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_console_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **console** | [**InstanceConsolePost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceConsolePost.md)| Console request | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_debug_memory_get**
> instance_debug_memory_get(project=project, format=format)

Get memory debug information of an instance

Returns memory debug information of a running instance.
Only supported for VMs.

### Example


```python
import pyincusd
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    format = 'format_example' # str | Memory dump format (optional)

    try:
        # Get memory debug information of an instance
        api_instance.instance_debug_memory_get(project=project, format=format)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_debug_memory_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **format** | **str**| Memory dump format | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_debug_repair_post**
> ServerPut200Response instance_debug_repair_post(project=project, state=state)

Trigger a repair action on the instance.

Runs an internal repair action on the instance.

### Example


```python
import pyincusd
from pyincusd.models.instance_debug_repair_post import InstanceDebugRepairPost
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    state = pyincusd.InstanceDebugRepairPost() # InstanceDebugRepairPost | State (optional)

    try:
        # Trigger a repair action on the instance.
        api_response = api_instance.instance_debug_repair_post(project=project, state=state)
        print("The response of InstancesApi->instance_debug_repair_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_debug_repair_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **state** | [**InstanceDebugRepairPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceDebugRepairPost.md)| State | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_delete**
> ClusterMembersPost202Response instance_delete(project=project)

Delete an instance

Deletes a specific instance.

This also deletes anything owned by the instance such as snapshots and backups.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete an instance
        api_response = api_instance.instance_delete(project=project)
        print("The response of InstancesApi->instance_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_exec_output_delete**
> ServerPut200Response instance_exec_output_delete(project=project)

Delete the exec record-output file

Removes the exec record-output file.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the exec record-output file
        api_response = api_instance.instance_exec_output_delete(project=project)
        print("The response of InstancesApi->instance_exec_output_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_exec_output_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_exec_output_get**
> instance_exec_output_get(project=project)

Get the exec-output log file

Gets the exec-output file.

### Example


```python
import pyincusd
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the exec-output log file
        api_instance.instance_exec_output_get(project=project)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_exec_output_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw file |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_exec_outputs_get**
> InstanceExecOutputsGet200Response instance_exec_outputs_get(project=project)

Get the exec record-output files

Returns a list of exec record-output files (URLs).

### Example


```python
import pyincusd
from pyincusd.models.instance_exec_outputs_get200_response import InstanceExecOutputsGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the exec record-output files
        api_response = api_instance.instance_exec_outputs_get(project=project)
        print("The response of InstancesApi->instance_exec_outputs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_exec_outputs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceExecOutputsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceExecOutputsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_exec_post**
> ClusterMembersPost202Response instance_exec_post(project=project, var_exec=var_exec)

Run a command

Executes a command inside an instance.

The returned operation metadata will contain either 2 or 4 websockets.
In non-interactive mode, you'll get one websocket for each of stdin, stdout and stderr.
In interactive mode, a single bi-directional websocket is used for stdin and stdout/stderr.

An additional "control" socket is always added on top which can be used for out of band communications.
This allows sending signals and window sizing information through.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instance_exec_post import InstanceExecPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    var_exec = pyincusd.InstanceExecPost() # InstanceExecPost | Exec request (optional)

    try:
        # Run a command
        api_response = api_instance.instance_exec_post(project=project, var_exec=var_exec)
        print("The response of InstancesApi->instance_exec_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_exec_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **var_exec** | [**InstanceExecPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceExecPost.md)| Exec request | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_files_delete**
> ServerPut200Response instance_files_delete(path=path, project=project, x_incus_force=x_incus_force)

Delete a file

Removes the file.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    path = 'path_example' # str | Path to the file (optional)
    project = 'project_example' # str | Project name (optional)
    x_incus_force = None # object | Perform recursive deletion (optional)

    try:
        # Delete a file
        api_response = api_instance.instance_files_delete(path=path, project=project, x_incus_force=x_incus_force)
        print("The response of InstancesApi->instance_files_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_files_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the file | [optional] 
 **project** | **str**| Project name | [optional] 
 **x_incus_force** | [**object**](.md)| Perform recursive deletion | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_files_get**
> instance_files_get(path=path, project=project)

Get a file

Gets the file content. If it's a directory, a json list of files will be returned instead.

### Example


```python
import pyincusd
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    path = 'path_example' # str | Path to the file (optional)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get a file
        api_instance.instance_files_get(path=path, project=project)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_files_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the file | [optional] 
 **project** | **str**| Project name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw file or directory listing |  * X-Incus-modified - Last modified date <br>  * X-Incus-type - Type of file (file, symlink or directory) <br>  * X-Incus-gid - File owner GID <br>  * X-Incus-mode - Mode mask <br>  * X-Incus-uid - File owner UID <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_files_head**
> instance_files_head(path=path, project=project)

Get metadata for a file

Gets the file or directory metadata.

### Example


```python
import pyincusd
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    path = 'path_example' # str | Path to the file (optional)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get metadata for a file
        api_instance.instance_files_head(path=path, project=project)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_files_head: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the file | [optional] 
 **project** | **str**| Project name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw file or directory listing |  * X-Incus-modified - Last modified date <br>  * X-Incus-type - Type of file (file, symlink or directory) <br>  * X-Incus-gid - File owner GID <br>  * X-Incus-mode - Mode mask <br>  * X-Incus-uid - File owner UID <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_files_post**
> ServerPut200Response instance_files_post(path=path, project=project, x_incus_uid=x_incus_uid, x_incus_gid=x_incus_gid, x_incus_mode=x_incus_mode, x_incus_type=x_incus_type, x_incus_write=x_incus_write)

Create or replace a file

Creates a new file in the instance.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    path = 'path_example' # str | Path to the file (optional)
    project = 'project_example' # str | Project name (optional)
    x_incus_uid = None # object | File owner UID (optional)
    x_incus_gid = None # object | File owner GID (optional)
    x_incus_mode = None # object | File mode (optional)
    x_incus_type = None # object | Type of file (file, symlink or directory) (optional)
    x_incus_write = None # object | Write mode (overwrite or append) (optional)

    try:
        # Create or replace a file
        api_response = api_instance.instance_files_post(path=path, project=project, x_incus_uid=x_incus_uid, x_incus_gid=x_incus_gid, x_incus_mode=x_incus_mode, x_incus_type=x_incus_type, x_incus_write=x_incus_write)
        print("The response of InstancesApi->instance_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the file | [optional] 
 **project** | **str**| Project name | [optional] 
 **x_incus_uid** | [**object**](.md)| File owner UID | [optional] 
 **x_incus_gid** | [**object**](.md)| File owner GID | [optional] 
 **x_incus_mode** | [**object**](.md)| File mode | [optional] 
 **x_incus_type** | [**object**](.md)| Type of file (file, symlink or directory) | [optional] 
 **x_incus_write** | [**object**](.md)| Write mode (overwrite or append) | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_get**
> InstanceGet200Response instance_get(project=project)

Get the instance

Gets a specific instance (basic struct).

### Example


```python
import pyincusd
from pyincusd.models.instance_get200_response import InstanceGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the instance
        api_response = api_instance.instance_get(project=project)
        print("The response of InstancesApi->instance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instance |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_get_recursion1**
> InstanceGetRecursion1200Response instance_get_recursion1(project=project)

Get the instance

Gets a specific instance (full struct).

recursion=1 also includes information about state, snapshots and backups.

### Example


```python
import pyincusd
from pyincusd.models.instance_get_recursion1200_response import InstanceGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the instance
        api_response = api_instance.instance_get_recursion1(project=project)
        print("The response of InstancesApi->instance_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceGetRecursion1200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instance |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_log_delete**
> ServerPut200Response instance_log_delete(project=project)

Delete the log file

Removes the log file.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the log file
        api_response = api_instance.instance_log_delete(project=project)
        print("The response of InstancesApi->instance_log_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_log_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_log_get**
> instance_log_get(project=project)

Get the log file

Gets the log file.

### Example


```python
import pyincusd
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the log file
        api_instance.instance_log_get(project=project)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_log_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw file |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_logs_get**
> InstanceLogsGet200Response instance_logs_get(project=project)

Get the log files

Returns a list of log files (URLs).

### Example


```python
import pyincusd
from pyincusd.models.instance_logs_get200_response import InstanceLogsGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the log files
        api_response = api_instance.instance_logs_get(project=project)
        print("The response of InstancesApi->instance_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceLogsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceLogsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_metadata_get**
> InstanceMetadataGet200Response instance_metadata_get(project=project)

Get the instance image metadata

Gets the image metadata for the instance.

### Example


```python
import pyincusd
from pyincusd.models.instance_metadata_get200_response import InstanceMetadataGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the instance image metadata
        api_response = api_instance.instance_metadata_get(project=project)
        print("The response of InstancesApi->instance_metadata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_metadata_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceMetadataGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceMetadataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image metadata |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_metadata_patch**
> ServerPut200Response instance_metadata_patch(metadata, project=project)

Partially update the image metadata

Updates a subset of the instance image metadata.

### Example


```python
import pyincusd
from pyincusd.models.image_metadata import ImageMetadata
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    metadata = pyincusd.ImageMetadata() # ImageMetadata | Image metadata
    project = 'project_example' # str | Project name (optional)

    try:
        # Partially update the image metadata
        api_response = api_instance.instance_metadata_patch(metadata, project=project)
        print("The response of InstancesApi->instance_metadata_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_metadata_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**ImageMetadata**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ImageMetadata.md)| Image metadata | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_metadata_put**
> ServerPut200Response instance_metadata_put(metadata, project=project)

Update the image metadata

Updates the instance image metadata.

### Example


```python
import pyincusd
from pyincusd.models.image_metadata import ImageMetadata
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    metadata = pyincusd.ImageMetadata() # ImageMetadata | Image metadata
    project = 'project_example' # str | Project name (optional)

    try:
        # Update the image metadata
        api_response = api_instance.instance_metadata_put(metadata, project=project)
        print("The response of InstancesApi->instance_metadata_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_metadata_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**ImageMetadata**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ImageMetadata.md)| Image metadata | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_metadata_templates_delete**
> ServerPut200Response instance_metadata_templates_delete(path=path, project=project)

Delete a template file

Removes the template file.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    path = 'path_example' # str | Template name (optional)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete a template file
        api_response = api_instance.instance_metadata_templates_delete(path=path, project=project)
        print("The response of InstancesApi->instance_metadata_templates_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_metadata_templates_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Template name | [optional] 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_metadata_templates_get**
> instance_metadata_templates_get(project=project, path=path)

Get the template file names or a specific

If no path specified, returns a list of template file names.
If a path is specified, returns the file content.

### Example


```python
import pyincusd
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    path = 'path_example' # str | Template name (optional)

    try:
        # Get the template file names or a specific
        api_instance.instance_metadata_templates_get(project=project, path=path)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_metadata_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **path** | **str**| Template name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw template file or file listing |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_metadata_templates_post**
> ServerPut200Response instance_metadata_templates_post(path=path, project=project)

Create or replace a template file

Creates a new image template file for the instance.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    path = 'path_example' # str | Template name (optional)
    project = 'project_example' # str | Project name (optional)

    try:
        # Create or replace a template file
        api_response = api_instance.instance_metadata_templates_post(path=path, project=project)
        print("The response of InstancesApi->instance_metadata_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_metadata_templates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Template name | [optional] 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_patch**
> ServerPut200Response instance_patch(project=project, instance=instance)

Partially update the instance

Updates a subset of the instance configuration

### Example


```python
import pyincusd
from pyincusd.models.instance_put import InstancePut
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    instance = pyincusd.InstancePut() # InstancePut | Update request (optional)

    try:
        # Partially update the instance
        api_response = api_instance.instance_patch(project=project, instance=instance)
        print("The response of InstancesApi->instance_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **instance** | [**InstancePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancePut.md)| Update request | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_post**
> ClusterMembersPost202Response instance_post(project=project, migration=migration)

Rename or move/migrate an instance

Renames, moves an instance between pools or migrates an instance to another server.

The returned operation metadata will vary based on what's requested.
For rename or move within the same server, this is a simple background operation with progress data.
For migration, in the push case, this will similarly be a background
operation with progress data, for the pull case, it will be a websocket
operation with a number of secrets to be passed to the target server.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instance_post import InstancePost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    migration = pyincusd.InstancePost() # InstancePost | Migration request (optional)

    try:
        # Rename or move/migrate an instance
        api_response = api_instance.instance_post(project=project, migration=migration)
        print("The response of InstancesApi->instance_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **migration** | [**InstancePost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancePost.md)| Migration request | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_put**
> ClusterMembersPost202Response instance_put(project=project, instance=instance)

Update the instance

Updates the instance configuration or trigger a snapshot restore.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instance_put import InstancePut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    instance = pyincusd.InstancePut() # InstancePut | Update request (optional)

    try:
        # Update the instance
        api_response = api_instance.instance_put(project=project, instance=instance)
        print("The response of InstancesApi->instance_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **instance** | [**InstancePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancePut.md)| Update request | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_rebuild_post**
> ServerPut200Response instance_rebuild_post(instance, project=project)

Rebuild an instance

Rebuild an instance using an alternate image or as empty.

### Example


```python
import pyincusd
from pyincusd.models.instance_rebuild_post import InstanceRebuildPost
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    instance = pyincusd.InstanceRebuildPost() # InstanceRebuildPost | InstanceRebuild request
    project = 'project_example' # str | Project name (optional)

    try:
        # Rebuild an instance
        api_response = api_instance.instance_rebuild_post(instance, project=project)
        print("The response of InstancesApi->instance_rebuild_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_rebuild_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**InstanceRebuildPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceRebuildPost.md)| InstanceRebuild request | 
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_sftp**
> instance_sftp()

Get the instance SFTP connection

Upgrades the request to an SFTP connection of the instance's filesystem.

### Example


```python
import pyincusd
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)

    try:
        # Get the instance SFTP connection
        api_instance.instance_sftp()
    except Exception as e:
        print("Exception when calling InstancesApi->instance_sftp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**101** | Switching protocols to SFTP |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_snapshot_delete**
> ClusterMembersPost202Response instance_snapshot_delete(project=project)

Delete a snapshot

Deletes the instance snapshot.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete a snapshot
        api_response = api_instance.instance_snapshot_delete(project=project)
        print("The response of InstancesApi->instance_snapshot_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_snapshot_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_snapshot_get**
> InstanceSnapshotGet200Response instance_snapshot_get(project=project)

Get the snapshot

Gets a specific instance snapshot.

### Example


```python
import pyincusd
from pyincusd.models.instance_snapshot_get200_response import InstanceSnapshotGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the snapshot
        api_response = api_instance.instance_snapshot_get(project=project)
        print("The response of InstancesApi->instance_snapshot_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_snapshot_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceSnapshotGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceSnapshotGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instance snapshot |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_snapshot_patch**
> ClusterMembersPost202Response instance_snapshot_patch(project=project, snapshot=snapshot)

Partially update snapshot

Updates a subset of the snapshot config.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instance_snapshot_put import InstanceSnapshotPut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    snapshot = pyincusd.InstanceSnapshotPut() # InstanceSnapshotPut | Snapshot update (optional)

    try:
        # Partially update snapshot
        api_response = api_instance.instance_snapshot_patch(project=project, snapshot=snapshot)
        print("The response of InstancesApi->instance_snapshot_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_snapshot_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **snapshot** | [**InstanceSnapshotPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceSnapshotPut.md)| Snapshot update | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_snapshot_post**
> ClusterMembersPost202Response instance_snapshot_post(project=project, snapshot=snapshot)

Rename or move/migrate a snapshot

Renames or migrates an instance snapshot to another server.

The returned operation metadata will vary based on what's requested.
For rename or move within the same server, this is a simple background operation with progress data.
For migration, in the push case, this will similarly be a background
operation with progress data, for the pull case, it will be a websocket
operation with a number of secrets to be passed to the target server.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instance_snapshot_post import InstanceSnapshotPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    snapshot = pyincusd.InstanceSnapshotPost() # InstanceSnapshotPost | Snapshot migration (optional)

    try:
        # Rename or move/migrate a snapshot
        api_response = api_instance.instance_snapshot_post(project=project, snapshot=snapshot)
        print("The response of InstancesApi->instance_snapshot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_snapshot_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **snapshot** | [**InstanceSnapshotPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceSnapshotPost.md)| Snapshot migration | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_snapshot_put**
> ClusterMembersPost202Response instance_snapshot_put(project=project, snapshot=snapshot)

Update snapshot

Updates the snapshot config.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instance_snapshot_put import InstanceSnapshotPut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    snapshot = pyincusd.InstanceSnapshotPut() # InstanceSnapshotPut | Snapshot update (optional)

    try:
        # Update snapshot
        api_response = api_instance.instance_snapshot_put(project=project, snapshot=snapshot)
        print("The response of InstancesApi->instance_snapshot_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_snapshot_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **snapshot** | [**InstanceSnapshotPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceSnapshotPut.md)| Snapshot update | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_snapshots_get**
> InstanceSnapshotsGet200Response instance_snapshots_get(project=project)

Get the snapshots

Returns a list of instance snapshots (URLs).

### Example


```python
import pyincusd
from pyincusd.models.instance_snapshots_get200_response import InstanceSnapshotsGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the snapshots
        api_response = api_instance.instance_snapshots_get(project=project)
        print("The response of InstancesApi->instance_snapshots_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_snapshots_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceSnapshotsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceSnapshotsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_snapshots_get_recursion1**
> InstanceSnapshotsGetRecursion1200Response instance_snapshots_get_recursion1(project=project)

Get the snapshots

Returns a list of instance snapshots (structs).

### Example


```python
import pyincusd
from pyincusd.models.instance_snapshots_get_recursion1200_response import InstanceSnapshotsGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the snapshots
        api_response = api_instance.instance_snapshots_get_recursion1(project=project)
        print("The response of InstancesApi->instance_snapshots_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_snapshots_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceSnapshotsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceSnapshotsGetRecursion1200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_snapshots_post**
> ClusterMembersPost202Response instance_snapshots_post(project=project, snapshot=snapshot)

Create a snapshot

Creates a new snapshot.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instance_snapshots_post import InstanceSnapshotsPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    snapshot = pyincusd.InstanceSnapshotsPost() # InstanceSnapshotsPost | Snapshot request (optional)

    try:
        # Create a snapshot
        api_response = api_instance.instance_snapshots_post(project=project, snapshot=snapshot)
        print("The response of InstancesApi->instance_snapshots_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_snapshots_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **snapshot** | [**InstanceSnapshotsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceSnapshotsPost.md)| Snapshot request | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_state_get**
> InstanceStateGet200Response instance_state_get(project=project)

Get the runtime state

Gets the runtime state of the instance.

This is a reasonably expensive call as it causes code to be run
inside of the instance to retrieve the resource usage and network
information.

### Example


```python
import pyincusd
from pyincusd.models.instance_state_get200_response import InstanceStateGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the runtime state
        api_response = api_instance.instance_state_get(project=project)
        print("The response of InstancesApi->instance_state_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_state_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**InstanceStateGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceStateGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | State |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_state_put**
> ClusterMembersPost202Response instance_state_put(project=project, state=state)

Change the state

Changes the running state of the instance.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instance_state_put import InstanceStatePut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    state = pyincusd.InstanceStatePut() # InstanceStatePut | State (optional)

    try:
        # Change the state
        api_response = api_instance.instance_state_put(project=project, state=state)
        print("The response of InstancesApi->instance_state_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instance_state_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **state** | [**InstanceStatePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstanceStatePut.md)| State | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get**
> InstancesGet200Response instances_get(project=project, filter=filter, all_projects=all_projects)

Get the instances

Returns a list of instances (URLs).

### Example


```python
import pyincusd
from pyincusd.models.instances_get200_response import InstancesGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)
    all_projects = True # bool | Retrieve instances from all projects (optional)

    try:
        # Get the instances
        api_response = api_instance.instances_get(project=project, filter=filter, all_projects=all_projects)
        print("The response of InstancesApi->instances_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instances_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 
 **all_projects** | **bool**| Retrieve instances from all projects | [optional] 

### Return type

[**InstancesGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_recursion1**
> InstancesGetRecursion1200Response instances_get_recursion1(project=project, filter=filter, all_projects=all_projects)

Get the instances

Returns a list of instances (basic structs).

### Example


```python
import pyincusd
from pyincusd.models.instances_get_recursion1200_response import InstancesGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)
    all_projects = True # bool | Retrieve instances from all projects (optional)

    try:
        # Get the instances
        api_response = api_instance.instances_get_recursion1(project=project, filter=filter, all_projects=all_projects)
        print("The response of InstancesApi->instances_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instances_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 
 **all_projects** | **bool**| Retrieve instances from all projects | [optional] 

### Return type

[**InstancesGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesGetRecursion1200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_recursion2**
> InstancesGetRecursion2200Response instances_get_recursion2(project=project, filter=filter, all_projects=all_projects)

Get the instances

Returns a list of instances (full structs).

The main difference between recursion=1 and recursion=2 is that the
latter also includes state and snapshot information allowing for a
single API call to return everything needed by most clients.

### Example


```python
import pyincusd
from pyincusd.models.instances_get_recursion2200_response import InstancesGetRecursion2200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)
    all_projects = True # bool | Retrieve instances from all projects (optional)

    try:
        # Get the instances
        api_response = api_instance.instances_get_recursion2(project=project, filter=filter, all_projects=all_projects)
        print("The response of InstancesApi->instances_get_recursion2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instances_get_recursion2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 
 **all_projects** | **bool**| Retrieve instances from all projects | [optional] 

### Return type

[**InstancesGetRecursion2200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesGetRecursion2200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API endpoints |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_post**
> ClusterMembersPost202Response instances_post(project=project, target=target)

Create a new instance

Creates a new instance.
Depending on the source, this can create an instance from an existing
local image, remote image, existing local instance or snapshot, remote
migration stream or backup file.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member (optional)

    try:
        # Create a new instance
        api_response = api_instance.instances_post(project=project, target=target)
        print("The response of InstancesApi->instances_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instances_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_put**
> ClusterMembersPost202Response instances_put(project=project, state=state)

Bulk instance state update

Changes the running state of all instances.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.instances_put import InstancesPut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.InstancesApi(api_client)
    project = 'project_example' # str | Project name (optional)
    state = pyincusd.InstancesPut() # InstancesPut | State (optional)

    try:
        # Bulk instance state update
        api_response = api_instance.instances_put(project=project, state=state)
        print("The response of InstancesApi->instances_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->instances_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **state** | [**InstancesPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/InstancesPut.md)| State | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post1/docs/ClusterMembersPost202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

