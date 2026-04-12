# pyincusd.StorageApi

All URIs are relative to the incusd API (unix socket or https). See [Incus REST API docs](https://linuxcontainers.org/incus/docs/main/rest-api/).

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_pool_bucket_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_delete) | **DELETE** /1.0/storage-pools/{name}/buckets/{bucketName} | Delete the storage bucket
[**storage_pool_bucket_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_get) | **GET** /1.0/storage-pools/{poolName}/buckets/{bucketName} | Get the storage pool bucket
[**storage_pool_bucket_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_get_recursion1) | **GET** /1.0/storage-pools/{poolName}/buckets/{bucketName}?recursion&#x3D;1 | Get the full storage pool bucket details
[**storage_pool_bucket_key_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_key_delete) | **DELETE** /1.0/storage-pools/{name}/buckets/{bucketName}/keys/{keyName} | Delete the storage bucket key
[**storage_pool_bucket_key_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_key_get) | **GET** /1.0/storage-pools/{poolName}/buckets/{bucketName}/keys/{keyName} | Get the storage pool bucket key
[**storage_pool_bucket_key_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_key_post) | **POST** /1.0/storage-pools/{poolName}/buckets/{bucketName}/keys | Add a storage pool bucket key.
[**storage_pool_bucket_key_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_key_put) | **PUT** /1.0/storage-pools/{name}/buckets/{bucketName}/keys/{keyName} | Update the storage bucket key
[**storage_pool_bucket_keys_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_keys_get) | **GET** /1.0/storage-pools/{poolName}/buckets/{bucketName}/keys | Get the storage pool bucket keys
[**storage_pool_bucket_keys_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_keys_get_recursion1) | **GET** /1.0/storage-pools/{poolName}/buckets/{bucketName}/keys?recursion&#x3D;1 | Get the storage pool bucket keys
[**storage_pool_bucket_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_patch) | **PATCH** /1.0/storage-pools/{name}/buckets/{bucketName} | Partially update the storage bucket.
[**storage_pool_bucket_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_post) | **POST** /1.0/storage-pools/{poolName}/buckets | Add a storage pool bucket.
[**storage_pool_bucket_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_bucket_put) | **PUT** /1.0/storage-pools/{name}/buckets/{bucketName} | Update the storage bucket
[**storage_pool_buckets_backup_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_buckets_backup_delete) | **DELETE** /1.0/storage-pools/{poolName}/buckets/{bucketName}/backups/{backupName} | Delete a storage bucket backup
[**storage_pool_buckets_backup_export_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_buckets_backup_export_get) | **GET** /1.0/storage-pools/{poolName}/buckets/{bucketName}/backups/{backupName}/export | Get the raw backup file
[**storage_pool_buckets_backup_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_buckets_backup_get) | **GET** /1.0/storage-pools/{poolName}/buckets/{bucketName}/backups/{backupName} | Get the storage bucket backup
[**storage_pool_buckets_backup_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_buckets_backup_post) | **POST** /1.0/storage-pools/{poolName}/buckets/{bucketName}/backups/{backupName} | Rename a storage bucket backup
[**storage_pool_buckets_backups_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_buckets_backups_get) | **GET** /1.0/storage-pools/{poolName}/buckets/{bucketName}/backups | Get the storage bucket backups
[**storage_pool_buckets_backups_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_buckets_backups_get_recursion1) | **GET** /1.0/storage-pools/{poolName}/buckets/{bucketName}/backups?recursion&#x3D;1 | Get the storage bucket backups
[**storage_pool_buckets_backups_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_buckets_backups_post) | **POST** /1.0/storage-pools/{poolName}/buckets/{bucketName}/backups | Create a storage bucket backup
[**storage_pool_buckets_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_buckets_get) | **GET** /1.0/storage-pools/{poolName}/buckets | Get the storage pool buckets
[**storage_pool_buckets_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_buckets_get_recursion1) | **GET** /1.0/storage-pools/{poolName}/buckets?recursion&#x3D;1 | Get the storage pool buckets
[**storage_pool_buckets_get_recursion2**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_buckets_get_recursion2) | **GET** /1.0/storage-pools/{poolName}/buckets?recursion&#x3D;2 | Get the storage pool bucket details
[**storage_pool_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_get) | **GET** /1.0/storage-pools/{poolName} | Get the storage pool
[**storage_pool_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_patch) | **PATCH** /1.0/storage-pools/{poolName} | Partially update the storage pool
[**storage_pool_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_put) | **PUT** /1.0/storage-pools/{poolName} | Update the storage pool
[**storage_pool_resources**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_resources) | **GET** /1.0/storage-pools/{name}/resources | Get storage pool resources information
[**storage_pool_volume_type_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_delete) | **DELETE** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName} | Delete the storage volume
[**storage_pool_volume_type_files_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_files_delete) | **DELETE** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/files | Delete a file
[**storage_pool_volume_type_files_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_files_get) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/files | Get a file
[**storage_pool_volume_type_files_head**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_files_head) | **HEAD** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/files | Get metadata for a file
[**storage_pool_volume_type_files_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_files_post) | **POST** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/files | Create or replace a file
[**storage_pool_volume_type_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_get) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName} | Get the storage volume
[**storage_pool_volume_type_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_get_recursion1) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}?recursion&#x3D;1 | Get the full storage volume details
[**storage_pool_volume_type_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_patch) | **PATCH** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName} | Partially update the storage volume
[**storage_pool_volume_type_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_post) | **POST** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName} | Rename or move/migrate a storage volume
[**storage_pool_volume_type_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_put) | **PUT** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName} | Update the storage volume
[**storage_pool_volume_type_sftp_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_sftp_get) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/sftp | Get the storage volume SFTP connection
[**storage_pool_volume_type_state_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volume_type_state_get) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/state | Get the storage volume state
[**storage_pool_volumes_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_get) | **GET** /1.0/storage-pools/{poolName}/volumes | Get the storage volumes
[**storage_pool_volumes_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_get_recursion1) | **GET** /1.0/storage-pools/{poolName}/volumes?recursion&#x3D;1 | Get the storage volumes
[**storage_pool_volumes_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_post) | **POST** /1.0/storage-pools/{poolName}/volumes | Add a storage volume
[**storage_pool_volumes_type_backup_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_backup_delete) | **DELETE** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/backups/{backupName} | Delete a storage volume backup
[**storage_pool_volumes_type_backup_export_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_backup_export_get) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/backups/{backupName}/export | Get the raw backup file
[**storage_pool_volumes_type_backup_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_backup_get) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/backups/{backupName} | Get the storage volume backup
[**storage_pool_volumes_type_backup_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_backup_post) | **POST** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/backups/{backupName} | Rename a storage volume backup
[**storage_pool_volumes_type_backups_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_backups_get) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/backups | Get the storage volume backups
[**storage_pool_volumes_type_backups_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_backups_get_recursion1) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/backups?recursion&#x3D;1 | Get the storage volume backups
[**storage_pool_volumes_type_backups_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_backups_post) | **POST** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/backups | Create a storage volume backup
[**storage_pool_volumes_type_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_get) | **GET** /1.0/storage-pools/{poolName}/volumes/{type} | Get the storage volumes
[**storage_pool_volumes_type_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_get_recursion1) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}?recursion&#x3D;1 | Get the storage volumes
[**storage_pool_volumes_type_get_recursion2**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_get_recursion2) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}?recursion&#x3D;2 | Get the storage volumes with all details
[**storage_pool_volumes_type_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_post) | **POST** /1.0/storage-pools/{poolName}/volumes/{type} | Add a storage volume
[**storage_pool_volumes_type_snapshot_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_snapshot_delete) | **DELETE** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/snapshots/{snapshotName} | Delete a storage volume snapshot
[**storage_pool_volumes_type_snapshot_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_snapshot_get) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/snapshots/{snapshotName} | Get the storage volume snapshot
[**storage_pool_volumes_type_snapshot_patch**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_snapshot_patch) | **PATCH** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/snapshots/{snapshotName} | Partially update the storage volume snapshot
[**storage_pool_volumes_type_snapshot_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_snapshot_post) | **POST** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/snapshots/{snapshotName} | Rename a storage volume snapshot
[**storage_pool_volumes_type_snapshot_put**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_snapshot_put) | **PUT** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/snapshots/{snapshotName} | Update the storage volume snapshot
[**storage_pool_volumes_type_snapshots_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_snapshots_get) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/snapshots | Get the storage volume snapshots
[**storage_pool_volumes_type_snapshots_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_snapshots_get_recursion1) | **GET** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/snapshots?recursion&#x3D;1 | Get the storage volume snapshots
[**storage_pool_volumes_type_snapshots_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pool_volumes_type_snapshots_post) | **POST** /1.0/storage-pools/{poolName}/volumes/{type}/{volumeName}/snapshots | Create a storage volume snapshot
[**storage_pools_delete**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pools_delete) | **DELETE** /1.0/storage-pools/{poolName} | Delete the storage pool
[**storage_pools_get**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pools_get) | **GET** /1.0/storage-pools | Get the storage pools
[**storage_pools_get_recursion1**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pools_get_recursion1) | **GET** /1.0/storage-pools?recursion&#x3D;1 | Get the storage pools
[**storage_pools_post**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageApi.md#storage_pools_post) | **POST** /1.0/storage-pools | Add a storage pool


# **storage_pool_bucket_delete**
> ServerPut200Response storage_pool_bucket_delete(project=project, target=target)

Delete the storage bucket

Removes the storage bucket.

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Delete the storage bucket
        api_response = await api_instance.storage_pool_bucket_delete(project=project, target=target)
        print("The response of StorageApi->storage_pool_bucket_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_bucket_get**
> StoragePoolBucketGet200Response storage_pool_bucket_get(project=project)

Get the storage pool bucket

Gets a specific storage pool bucket.

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_bucket_get200_response import StoragePoolBucketGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the storage pool bucket
        api_response = await api_instance.storage_pool_bucket_get(project=project)
        print("The response of StorageApi->storage_pool_bucket_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**StoragePoolBucketGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolBucketGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage pool bucket |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_bucket_get_recursion1**
> StoragePoolBucketGetRecursion1200Response storage_pool_bucket_get_recursion1(project=project)

Get the full storage pool bucket details

Gets a specific storage pool bucket with all details (backups and keys).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_bucket_get_recursion1200_response import StoragePoolBucketGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the full storage pool bucket details
        api_response = await api_instance.storage_pool_bucket_get_recursion1(project=project)
        print("The response of StorageApi->storage_pool_bucket_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**StoragePoolBucketGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolBucketGetRecursion1200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage pool bucket |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_bucket_key_delete**
> ServerPut200Response storage_pool_bucket_key_delete(project=project, target=target)

Delete the storage bucket key

Removes the storage bucket key.

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Delete the storage bucket key
        api_response = await api_instance.storage_pool_bucket_key_delete(project=project, target=target)
        print("The response of StorageApi->storage_pool_bucket_key_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_key_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_bucket_key_get**
> StoragePoolBucketKeyGet200Response storage_pool_bucket_key_get(project=project)

Get the storage pool bucket key

Gets a specific storage pool bucket key.

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_bucket_key_get200_response import StoragePoolBucketKeyGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the storage pool bucket key
        api_response = await api_instance.storage_pool_bucket_key_get(project=project)
        print("The response of StorageApi->storage_pool_bucket_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**StoragePoolBucketKeyGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolBucketKeyGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage pool bucket key |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_bucket_key_post**
> storage_pool_bucket_key_post(bucket, project=project)

Add a storage pool bucket key.

Creates a new storage pool bucket key.

### Example


```python
import pyincusd
from pyincusd.models.storage_bucket_keys_post import StorageBucketKeysPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    bucket = pyincusd.StorageBucketKeysPost() # StorageBucketKeysPost | Bucket
    project = 'project_example' # str | Project name (optional)

    try:
        # Add a storage pool bucket key.
        await api_instance.storage_pool_bucket_key_post(bucket, project=project)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | [**StorageBucketKeysPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageBucketKeysPost.md)| Bucket | 
 **project** | **str**| Project name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_bucket_key_put**
> ServerPut200Response storage_pool_bucket_key_put(storage_bucket, project=project, target=target)

Update the storage bucket key

Updates the entire storage bucket key configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_bucket_key_put import StorageBucketKeyPut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    storage_bucket = pyincusd.StorageBucketKeyPut() # StorageBucketKeyPut | Storage bucket key configuration
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Update the storage bucket key
        api_response = await api_instance.storage_pool_bucket_key_put(storage_bucket, project=project, target=target)
        print("The response of StorageApi->storage_pool_bucket_key_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_key_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_bucket** | [**StorageBucketKeyPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageBucketKeyPut.md)| Storage bucket key configuration | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

# **storage_pool_bucket_keys_get**
> StoragePoolBucketKeysGet200Response storage_pool_bucket_keys_get(project=project)

Get the storage pool bucket keys

Returns a list of storage pool bucket keys (URLs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_bucket_keys_get200_response import StoragePoolBucketKeysGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the storage pool bucket keys
        api_response = await api_instance.storage_pool_bucket_keys_get(project=project)
        print("The response of StorageApi->storage_pool_bucket_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_keys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**StoragePoolBucketKeysGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolBucketKeysGet200Response.md)

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

# **storage_pool_bucket_keys_get_recursion1**
> StoragePoolBucketKeysGetRecursion1200Response storage_pool_bucket_keys_get_recursion1(project=project)

Get the storage pool bucket keys

Returns a list of storage pool bucket keys (structs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_bucket_keys_get_recursion1200_response import StoragePoolBucketKeysGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get the storage pool bucket keys
        api_response = await api_instance.storage_pool_bucket_keys_get_recursion1(project=project)
        print("The response of StorageApi->storage_pool_bucket_keys_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_keys_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**StoragePoolBucketKeysGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolBucketKeysGetRecursion1200Response.md)

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

# **storage_pool_bucket_patch**
> ServerPut200Response storage_pool_bucket_patch(storage_bucket, project=project, target=target)

Partially update the storage bucket.

Updates a subset of the storage bucket configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_bucket_put import StorageBucketPut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    storage_bucket = pyincusd.StorageBucketPut() # StorageBucketPut | Storage bucket configuration
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Partially update the storage bucket.
        api_response = await api_instance.storage_pool_bucket_patch(storage_bucket, project=project, target=target)
        print("The response of StorageApi->storage_pool_bucket_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_bucket** | [**StorageBucketPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageBucketPut.md)| Storage bucket configuration | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

# **storage_pool_bucket_post**
> storage_pool_bucket_post(bucket, project=project)

Add a storage pool bucket.

Creates a new storage pool bucket.

### Example


```python
import pyincusd
from pyincusd.models.storage_buckets_post import StorageBucketsPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    bucket = pyincusd.StorageBucketsPost() # StorageBucketsPost | Bucket
    project = 'project_example' # str | Project name (optional)

    try:
        # Add a storage pool bucket.
        await api_instance.storage_pool_bucket_post(bucket, project=project)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | [**StorageBucketsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageBucketsPost.md)| Bucket | 
 **project** | **str**| Project name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_bucket_put**
> ServerPut200Response storage_pool_bucket_put(storage_bucket, project=project, target=target)

Update the storage bucket

Updates the entire storage bucket configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_bucket_put import StorageBucketPut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    storage_bucket = pyincusd.StorageBucketPut() # StorageBucketPut | Storage bucket configuration
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Update the storage bucket
        api_response = await api_instance.storage_pool_bucket_put(storage_bucket, project=project, target=target)
        print("The response of StorageApi->storage_pool_bucket_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_bucket_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_bucket** | [**StorageBucketPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageBucketPut.md)| Storage bucket configuration | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

# **storage_pool_buckets_backup_delete**
> ClusterMembersPost202Response storage_pool_buckets_backup_delete(project=project, target=target)

Delete a storage bucket backup

Deletes a new storage bucket backup.

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Delete a storage bucket backup
        api_response = await api_instance.storage_pool_buckets_backup_delete(project=project, target=target)
        print("The response of StorageApi->storage_pool_buckets_backup_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_buckets_backup_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ClusterMembersPost202Response.md)

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

# **storage_pool_buckets_backup_export_get**
> storage_pool_buckets_backup_export_get(project=project, target=target)

Get the raw backup file

Download the raw backup file from the server.

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the raw backup file
        await api_instance.storage_pool_buckets_backup_export_get(project=project, target=target)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_buckets_backup_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

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
**200** | Raw backup data |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_buckets_backup_get**
> StoragePoolBucketsBackupGet200Response storage_pool_buckets_backup_get(project=project, target=target)

Get the storage bucket backup

Gets a specific storage bucket backup.

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_buckets_backup_get200_response import StoragePoolBucketsBackupGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage bucket backup
        api_response = await api_instance.storage_pool_buckets_backup_get(project=project, target=target)
        print("The response of StorageApi->storage_pool_buckets_backup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_buckets_backup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolBucketsBackupGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolBucketsBackupGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage bucket backup |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_buckets_backup_post**
> ClusterMembersPost202Response storage_pool_buckets_backup_post(bucket_rename, project=project, target=target)

Rename a storage bucket backup

Renames a storage bucket backup.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.storage_bucket_backup_post import StorageBucketBackupPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    bucket_rename = pyincusd.StorageBucketBackupPost() # StorageBucketBackupPost | Storage bucket backup
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Rename a storage bucket backup
        api_response = await api_instance.storage_pool_buckets_backup_post(bucket_rename, project=project, target=target)
        print("The response of StorageApi->storage_pool_buckets_backup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_buckets_backup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_rename** | [**StorageBucketBackupPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageBucketBackupPost.md)| Storage bucket backup | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ClusterMembersPost202Response.md)

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

# **storage_pool_buckets_backups_get**
> StoragePoolBucketsBackupsGet200Response storage_pool_buckets_backups_get(project=project, target=target)

Get the storage bucket backups

Returns a list of storage bucket backups (URLs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_buckets_backups_get200_response import StoragePoolBucketsBackupsGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage bucket backups
        api_response = await api_instance.storage_pool_buckets_backups_get(project=project, target=target)
        print("The response of StorageApi->storage_pool_buckets_backups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_buckets_backups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolBucketsBackupsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolBucketsBackupsGet200Response.md)

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

# **storage_pool_buckets_backups_get_recursion1**
> StoragePoolBucketsBackupsGetRecursion1200Response storage_pool_buckets_backups_get_recursion1(project=project, target=target)

Get the storage bucket backups

Returns a list of storage bucket backups (structs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_buckets_backups_get_recursion1200_response import StoragePoolBucketsBackupsGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage bucket backups
        api_response = await api_instance.storage_pool_buckets_backups_get_recursion1(project=project, target=target)
        print("The response of StorageApi->storage_pool_buckets_backups_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_buckets_backups_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolBucketsBackupsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolBucketsBackupsGetRecursion1200Response.md)

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

# **storage_pool_buckets_backups_post**
> ClusterMembersPost202Response storage_pool_buckets_backups_post(bucket, project=project, target=target)

Create a storage bucket backup

Creates a new storage bucket backup.

If the `Accept` header is set to `application/octet-stream`, this directly streams the backup
tarball to the client without any intermediate operation.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.storage_bucket_backups_post import StorageBucketBackupsPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    bucket = pyincusd.StorageBucketBackupsPost() # StorageBucketBackupsPost | Storage bucket backup
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Create a storage bucket backup
        api_response = await api_instance.storage_pool_buckets_backups_post(bucket, project=project, target=target)
        print("The response of StorageApi->storage_pool_buckets_backups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_buckets_backups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | [**StorageBucketBackupsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageBucketBackupsPost.md)| Storage bucket backup | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ClusterMembersPost202Response.md)

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

# **storage_pool_buckets_get**
> StoragePoolBucketsGet200Response storage_pool_buckets_get(project=project, all_projects=all_projects, filter=filter)

Get the storage pool buckets

Returns a list of storage pool buckets (URLs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_buckets_get200_response import StoragePoolBucketsGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve storage pool buckets from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the storage pool buckets
        api_response = await api_instance.storage_pool_buckets_get(project=project, all_projects=all_projects, filter=filter)
        print("The response of StorageApi->storage_pool_buckets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_buckets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve storage pool buckets from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**StoragePoolBucketsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolBucketsGet200Response.md)

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

# **storage_pool_buckets_get_recursion1**
> StoragePoolBucketsGetRecursion1200Response storage_pool_buckets_get_recursion1(project=project, all_projects=all_projects, filter=filter)

Get the storage pool buckets

Returns a list of storage pool buckets (structs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_buckets_get_recursion1200_response import StoragePoolBucketsGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve storage pool buckets from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the storage pool buckets
        api_response = await api_instance.storage_pool_buckets_get_recursion1(project=project, all_projects=all_projects, filter=filter)
        print("The response of StorageApi->storage_pool_buckets_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_buckets_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve storage pool buckets from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**StoragePoolBucketsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolBucketsGetRecursion1200Response.md)

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

# **storage_pool_buckets_get_recursion2**
> StoragePoolBucketsGetRecursion2200Response storage_pool_buckets_get_recursion2(project=project, all_projects=all_projects, filter=filter)

Get the storage pool bucket details

Returns a list of storage pool buckets with all details (structs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_buckets_get_recursion2200_response import StoragePoolBucketsGetRecursion2200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    all_projects = True # bool | Retrieve storage pool buckets from all projects (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the storage pool bucket details
        api_response = await api_instance.storage_pool_buckets_get_recursion2(project=project, all_projects=all_projects, filter=filter)
        print("The response of StorageApi->storage_pool_buckets_get_recursion2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_buckets_get_recursion2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **all_projects** | **bool**| Retrieve storage pool buckets from all projects | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**StoragePoolBucketsGetRecursion2200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolBucketsGetRecursion2200Response.md)

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

# **storage_pool_get**
> StoragePoolGet200Response storage_pool_get(project=project, target=target)

Get the storage pool

Gets a specific storage pool.

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_get200_response import StoragePoolGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage pool
        api_response = await api_instance.storage_pool_get(project=project, target=target)
        print("The response of StorageApi->storage_pool_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage pool |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_patch**
> ServerPut200Response storage_pool_patch(storage_pool, project=project, target=target)

Partially update the storage pool

Updates a subset of the storage pool configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_pool_put import StoragePoolPut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    storage_pool = pyincusd.StoragePoolPut() # StoragePoolPut | Storage pool configuration
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Partially update the storage pool
        api_response = await api_instance.storage_pool_patch(storage_pool, project=project, target=target)
        print("The response of StorageApi->storage_pool_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_pool** | [**StoragePoolPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolPut.md)| Storage pool configuration | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

# **storage_pool_put**
> ServerPut200Response storage_pool_put(storage_pool, project=project, target=target)

Update the storage pool

Updates the entire storage pool configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_pool_put import StoragePoolPut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    storage_pool = pyincusd.StoragePoolPut() # StoragePoolPut | Storage pool configuration
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Update the storage pool
        api_response = await api_instance.storage_pool_put(storage_pool, project=project, target=target)
        print("The response of StorageApi->storage_pool_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_pool** | [**StoragePoolPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolPut.md)| Storage pool configuration | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

# **storage_pool_resources**
> StoragePoolResources200Response storage_pool_resources(target=target)

Get storage pool resources information

Gets the usage information for the storage pool.

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_resources200_response import StoragePoolResources200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get storage pool resources information
        api_response = await api_instance.storage_pool_resources(target=target)
        print("The response of StorageApi->storage_pool_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolResources200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolResources200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hardware resources |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volume_type_delete**
> ServerPut200Response storage_pool_volume_type_delete(project=project, target=target)

Delete the storage volume

Removes the storage volume.

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Delete the storage volume
        api_response = await api_instance.storage_pool_volume_type_delete(project=project, target=target)
        print("The response of StorageApi->storage_pool_volume_type_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volume_type_files_delete**
> ServerPut200Response storage_pool_volume_type_files_delete(path=path, project=project, x_incus_force=x_incus_force)

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    path = 'path_example' # str | Path to the file (optional)
    project = 'project_example' # str | Project name (optional)
    x_incus_force = None # object | Perform recursive deletion (optional)

    try:
        # Delete a file
        api_response = await api_instance.storage_pool_volume_type_files_delete(path=path, project=project, x_incus_force=x_incus_force)
        print("The response of StorageApi->storage_pool_volume_type_files_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_files_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the file | [optional] 
 **project** | **str**| Project name | [optional] 
 **x_incus_force** | [**object**](.md)| Perform recursive deletion | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

# **storage_pool_volume_type_files_get**
> storage_pool_volume_type_files_get(path=path, project=project)

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    path = 'path_example' # str | Path to the file (optional)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get a file
        await api_instance.storage_pool_volume_type_files_get(path=path, project=project)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_files_get: %s\n" % e)
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

# **storage_pool_volume_type_files_head**
> storage_pool_volume_type_files_head(path=path, project=project)

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    path = 'path_example' # str | Path to the file (optional)
    project = 'project_example' # str | Project name (optional)

    try:
        # Get metadata for a file
        await api_instance.storage_pool_volume_type_files_head(path=path, project=project)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_files_head: %s\n" % e)
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

# **storage_pool_volume_type_files_post**
> ServerPut200Response storage_pool_volume_type_files_post(path=path, project=project, x_incus_uid=x_incus_uid, x_incus_gid=x_incus_gid, x_incus_mode=x_incus_mode, x_incus_type=x_incus_type, x_incus_write=x_incus_write)

Create or replace a file

Creates a new file in the storage volume.

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    path = 'path_example' # str | Path to the file (optional)
    project = 'project_example' # str | Project name (optional)
    x_incus_uid = None # object | File owner UID (optional)
    x_incus_gid = None # object | File owner GID (optional)
    x_incus_mode = None # object | File mode (optional)
    x_incus_type = None # object | Type of file (file, symlink or directory) (optional)
    x_incus_write = None # object | Write mode (overwrite or append) (optional)

    try:
        # Create or replace a file
        api_response = await api_instance.storage_pool_volume_type_files_post(path=path, project=project, x_incus_uid=x_incus_uid, x_incus_gid=x_incus_gid, x_incus_mode=x_incus_mode, x_incus_type=x_incus_type, x_incus_write=x_incus_write)
        print("The response of StorageApi->storage_pool_volume_type_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_files_post: %s\n" % e)
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

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

# **storage_pool_volume_type_get**
> StoragePoolVolumeTypeGet200Response storage_pool_volume_type_get(project=project, target=target)

Get the storage volume

Gets a specific storage volume.

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volume_type_get200_response import StoragePoolVolumeTypeGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage volume
        api_response = await api_instance.storage_pool_volume_type_get(project=project, target=target)
        print("The response of StorageApi->storage_pool_volume_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumeTypeGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumeTypeGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage volume |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volume_type_get_recursion1**
> StoragePoolVolumeTypeGetRecursion1200Response storage_pool_volume_type_get_recursion1(project=project, target=target)

Get the full storage volume details

Gets a specific storage volume with all details (backups, snapshots and state0..

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volume_type_get_recursion1200_response import StoragePoolVolumeTypeGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the full storage volume details
        api_response = await api_instance.storage_pool_volume_type_get_recursion1(project=project, target=target)
        print("The response of StorageApi->storage_pool_volume_type_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumeTypeGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumeTypeGetRecursion1200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage volume |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volume_type_patch**
> ServerPut200Response storage_pool_volume_type_patch(storage_volume, project=project, target=target)

Partially update the storage volume

Updates a subset of the storage volume configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_volume_put import StorageVolumePut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    storage_volume = pyincusd.StorageVolumePut() # StorageVolumePut | Storage volume configuration
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Partially update the storage volume
        api_response = await api_instance.storage_pool_volume_type_patch(storage_volume, project=project, target=target)
        print("The response of StorageApi->storage_pool_volume_type_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_volume** | [**StorageVolumePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageVolumePut.md)| Storage volume configuration | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

# **storage_pool_volume_type_post**
> ClusterMembersPost202Response storage_pool_volume_type_post(project=project, target=target, migration=migration)

Rename or move/migrate a storage volume

Renames, moves a storage volume between pools or migrates an instance to another server.

The returned operation metadata will vary based on what's requested.
For rename or move within the same server, this is a simple background operation with progress data.
For migration, in the push case, this will similarly be a background
operation with progress data, for the pull case, it will be a websocket
operation with a number of secrets to be passed to the target server.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.storage_volume_post import StorageVolumePost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)
    migration = pyincusd.StorageVolumePost() # StorageVolumePost | Migration request (optional)

    try:
        # Rename or move/migrate a storage volume
        api_response = await api_instance.storage_pool_volume_type_post(project=project, target=target, migration=migration)
        print("The response of StorageApi->storage_pool_volume_type_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 
 **migration** | [**StorageVolumePost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageVolumePost.md)| Migration request | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ClusterMembersPost202Response.md)

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

# **storage_pool_volume_type_put**
> ServerPut200Response storage_pool_volume_type_put(storage_volume, project=project, target=target)

Update the storage volume

Updates the entire storage volume configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_volume_put import StorageVolumePut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    storage_volume = pyincusd.StorageVolumePut() # StorageVolumePut | Storage volume configuration
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Update the storage volume
        api_response = await api_instance.storage_pool_volume_type_put(storage_volume, project=project, target=target)
        print("The response of StorageApi->storage_pool_volume_type_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_volume** | [**StorageVolumePut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageVolumePut.md)| Storage volume configuration | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

# **storage_pool_volume_type_sftp_get**
> storage_pool_volume_type_sftp_get()

Get the storage volume SFTP connection

Upgrades the request to an SFTP connection of the storage volume's filesystem.

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)

    try:
        # Get the storage volume SFTP connection
        await api_instance.storage_pool_volume_type_sftp_get()
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_sftp_get: %s\n" % e)
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

# **storage_pool_volume_type_state_get**
> StoragePoolVolumeTypeStateGet200Response storage_pool_volume_type_state_get(project=project, target=target)

Get the storage volume state

Gets a specific storage volume state (usage data).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volume_type_state_get200_response import StoragePoolVolumeTypeStateGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage volume state
        api_response = await api_instance.storage_pool_volume_type_state_get(project=project, target=target)
        print("The response of StorageApi->storage_pool_volume_type_state_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volume_type_state_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumeTypeStateGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumeTypeStateGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage pool |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volumes_get**
> StoragePoolVolumesGet200Response storage_pool_volumes_get(project=project, target=target, filter=filter)

Get the storage volumes

Returns a list of storage volumes (URLs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volumes_get200_response import StoragePoolVolumesGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the storage volumes
        api_response = await api_instance.storage_pool_volumes_get(project=project, target=target, filter=filter)
        print("The response of StorageApi->storage_pool_volumes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**StoragePoolVolumesGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumesGet200Response.md)

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

# **storage_pool_volumes_get_recursion1**
> StoragePoolVolumesTypeGetRecursion1200Response storage_pool_volumes_get_recursion1(project=project, target=target, filter=filter)

Get the storage volumes

Returns a list of storage volumes (structs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volumes_type_get_recursion1200_response import StoragePoolVolumesTypeGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the storage volumes
        api_response = await api_instance.storage_pool_volumes_get_recursion1(project=project, target=target, filter=filter)
        print("The response of StorageApi->storage_pool_volumes_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**StoragePoolVolumesTypeGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumesTypeGetRecursion1200Response.md)

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

# **storage_pool_volumes_post**
> ServerPut200Response storage_pool_volumes_post(volume, project=project, target=target)

Add a storage volume

Creates a new storage volume.
Will return an empty sync response on simple volume creation but an operation on copy or migration.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_volumes_post import StorageVolumesPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    volume = pyincusd.StorageVolumesPost() # StorageVolumesPost | Storage volume
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Add a storage volume
        api_response = await api_instance.storage_pool_volumes_post(volume, project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume** | [**StorageVolumesPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageVolumesPost.md)| Storage volume | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volumes_type_backup_delete**
> ClusterMembersPost202Response storage_pool_volumes_type_backup_delete(project=project, target=target)

Delete a storage volume backup

Deletes a new storage volume backup.

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Delete a storage volume backup
        api_response = await api_instance.storage_pool_volumes_type_backup_delete(project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_backup_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_backup_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ClusterMembersPost202Response.md)

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

# **storage_pool_volumes_type_backup_export_get**
> storage_pool_volumes_type_backup_export_get(project=project, target=target)

Get the raw backup file

Download the raw backup file from the server.

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the raw backup file
        await api_instance.storage_pool_volumes_type_backup_export_get(project=project, target=target)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_backup_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

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
**200** | Raw backup data |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volumes_type_backup_get**
> StoragePoolVolumesTypeBackupGet200Response storage_pool_volumes_type_backup_get(project=project, target=target)

Get the storage volume backup

Gets a specific storage volume backup.

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volumes_type_backup_get200_response import StoragePoolVolumesTypeBackupGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage volume backup
        api_response = await api_instance.storage_pool_volumes_type_backup_get(project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_backup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_backup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumesTypeBackupGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumesTypeBackupGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage volume backup |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volumes_type_backup_post**
> ClusterMembersPost202Response storage_pool_volumes_type_backup_post(volume_rename, project=project, target=target)

Rename a storage volume backup

Renames a storage volume backup.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.storage_volume_snapshot_post import StorageVolumeSnapshotPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    volume_rename = pyincusd.StorageVolumeSnapshotPost() # StorageVolumeSnapshotPost | Storage volume backup
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Rename a storage volume backup
        api_response = await api_instance.storage_pool_volumes_type_backup_post(volume_rename, project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_backup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_backup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_rename** | [**StorageVolumeSnapshotPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageVolumeSnapshotPost.md)| Storage volume backup | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ClusterMembersPost202Response.md)

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

# **storage_pool_volumes_type_backups_get**
> StoragePoolVolumesTypeBackupsGet200Response storage_pool_volumes_type_backups_get(project=project, target=target)

Get the storage volume backups

Returns a list of storage volume backups (URLs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volumes_type_backups_get200_response import StoragePoolVolumesTypeBackupsGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage volume backups
        api_response = await api_instance.storage_pool_volumes_type_backups_get(project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_backups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_backups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumesTypeBackupsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumesTypeBackupsGet200Response.md)

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

# **storage_pool_volumes_type_backups_get_recursion1**
> StoragePoolVolumesTypeBackupsGetRecursion1200Response storage_pool_volumes_type_backups_get_recursion1(project=project, target=target)

Get the storage volume backups

Returns a list of storage volume backups (structs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volumes_type_backups_get_recursion1200_response import StoragePoolVolumesTypeBackupsGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage volume backups
        api_response = await api_instance.storage_pool_volumes_type_backups_get_recursion1(project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_backups_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_backups_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumesTypeBackupsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumesTypeBackupsGetRecursion1200Response.md)

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

# **storage_pool_volumes_type_backups_post**
> ClusterMembersPost202Response storage_pool_volumes_type_backups_post(volume, project=project, target=target)

Create a storage volume backup

Creates a new storage volume backup.

If the `Accept` header is set to `application/octet-stream`, this directly streams the backup
tarball to the client without any intermediate operation.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.storage_volume_backups_post import StorageVolumeBackupsPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    volume = pyincusd.StorageVolumeBackupsPost() # StorageVolumeBackupsPost | Storage volume backup
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Create a storage volume backup
        api_response = await api_instance.storage_pool_volumes_type_backups_post(volume, project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_backups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_backups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume** | [**StorageVolumeBackupsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageVolumeBackupsPost.md)| Storage volume backup | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ClusterMembersPost202Response.md)

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

# **storage_pool_volumes_type_get**
> StoragePoolVolumesTypeGet200Response storage_pool_volumes_type_get(project=project, target=target)

Get the storage volumes

Returns a list of storage volumes (URLs) (type specific endpoint).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volumes_type_get200_response import StoragePoolVolumesTypeGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage volumes
        api_response = await api_instance.storage_pool_volumes_type_get(project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumesTypeGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumesTypeGet200Response.md)

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

# **storage_pool_volumes_type_get_recursion1**
> StoragePoolVolumesTypeGetRecursion1200Response storage_pool_volumes_type_get_recursion1(project=project, target=target)

Get the storage volumes

Returns a list of storage volumes (structs) (type specific endpoint).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volumes_type_get_recursion1200_response import StoragePoolVolumesTypeGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage volumes
        api_response = await api_instance.storage_pool_volumes_type_get_recursion1(project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumesTypeGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumesTypeGetRecursion1200Response.md)

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

# **storage_pool_volumes_type_get_recursion2**
> StoragePoolVolumesTypeGetRecursion2200Response storage_pool_volumes_type_get_recursion2(project=project, target=target)

Get the storage volumes with all details

Returns a list of storage volumes (structs) including all details (type specific endpoint).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volumes_type_get_recursion2200_response import StoragePoolVolumesTypeGetRecursion2200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage volumes with all details
        api_response = await api_instance.storage_pool_volumes_type_get_recursion2(project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_get_recursion2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_get_recursion2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumesTypeGetRecursion2200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumesTypeGetRecursion2200Response.md)

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

# **storage_pool_volumes_type_post**
> ServerPut200Response storage_pool_volumes_type_post(volume, project=project, target=target)

Add a storage volume

Creates a new storage volume (type specific endpoint).
Will return an empty sync response on simple volume creation but an operation on copy or migration.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_volumes_post import StorageVolumesPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    volume = pyincusd.StorageVolumesPost() # StorageVolumesPost | Storage volume
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Add a storage volume
        api_response = await api_instance.storage_pool_volumes_type_post(volume, project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume** | [**StorageVolumesPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageVolumesPost.md)| Storage volume | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty sync response |  -  |
**202** | Operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volumes_type_snapshot_delete**
> ClusterMembersPost202Response storage_pool_volumes_type_snapshot_delete(project=project, target=target)

Delete a storage volume snapshot

Deletes a new storage volume snapshot.

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Delete a storage volume snapshot
        api_response = await api_instance.storage_pool_volumes_type_snapshot_delete(project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_snapshot_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_snapshot_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ClusterMembersPost202Response.md)

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

# **storage_pool_volumes_type_snapshot_get**
> StoragePoolVolumesTypeSnapshotGet200Response storage_pool_volumes_type_snapshot_get(project=project, target=target)

Get the storage volume snapshot

Gets a specific storage volume snapshot.

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volumes_type_snapshot_get200_response import StoragePoolVolumesTypeSnapshotGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage volume snapshot
        api_response = await api_instance.storage_pool_volumes_type_snapshot_get(project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_snapshot_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_snapshot_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumesTypeSnapshotGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumesTypeSnapshotGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage volume snapshot |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volumes_type_snapshot_patch**
> ServerPut200Response storage_pool_volumes_type_snapshot_patch(storage_volume_snapshot, project=project, target=target)

Partially update the storage volume snapshot

Updates a subset of the storage volume snapshot configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_volume_snapshot_put import StorageVolumeSnapshotPut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    storage_volume_snapshot = pyincusd.StorageVolumeSnapshotPut() # StorageVolumeSnapshotPut | Storage volume snapshot configuration
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Partially update the storage volume snapshot
        api_response = await api_instance.storage_pool_volumes_type_snapshot_patch(storage_volume_snapshot, project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_snapshot_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_snapshot_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_volume_snapshot** | [**StorageVolumeSnapshotPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageVolumeSnapshotPut.md)| Storage volume snapshot configuration | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

# **storage_pool_volumes_type_snapshot_post**
> ClusterMembersPost202Response storage_pool_volumes_type_snapshot_post(volume_rename, project=project, target=target)

Rename a storage volume snapshot

Renames a storage volume snapshot.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.storage_volume_snapshot_post import StorageVolumeSnapshotPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    volume_rename = pyincusd.StorageVolumeSnapshotPost() # StorageVolumeSnapshotPost | Storage volume snapshot
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Rename a storage volume snapshot
        api_response = await api_instance.storage_pool_volumes_type_snapshot_post(volume_rename, project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_snapshot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_snapshot_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_rename** | [**StorageVolumeSnapshotPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageVolumeSnapshotPost.md)| Storage volume snapshot | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ClusterMembersPost202Response.md)

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

# **storage_pool_volumes_type_snapshot_put**
> ServerPut200Response storage_pool_volumes_type_snapshot_put(storage_volume_snapshot, project=project, target=target)

Update the storage volume snapshot

Updates the entire storage volume snapshot configuration.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_volume_snapshot_put import StorageVolumeSnapshotPut
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    storage_volume_snapshot = pyincusd.StorageVolumeSnapshotPut() # StorageVolumeSnapshotPut | Storage volume snapshot configuration
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Update the storage volume snapshot
        api_response = await api_instance.storage_pool_volumes_type_snapshot_put(storage_volume_snapshot, project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_snapshot_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_snapshot_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_volume_snapshot** | [**StorageVolumeSnapshotPut**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageVolumeSnapshotPut.md)| Storage volume snapshot configuration | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

# **storage_pool_volumes_type_snapshots_get**
> StoragePoolVolumesTypeSnapshotsGet200Response storage_pool_volumes_type_snapshots_get(project=project, target=target)

Get the storage volume snapshots

Returns a list of storage volume snapshots (URLs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volumes_type_snapshots_get200_response import StoragePoolVolumesTypeSnapshotsGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage volume snapshots
        api_response = await api_instance.storage_pool_volumes_type_snapshots_get(project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_snapshots_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_snapshots_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumesTypeSnapshotsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumesTypeSnapshotsGet200Response.md)

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

# **storage_pool_volumes_type_snapshots_get_recursion1**
> StoragePoolVolumesTypeSnapshotsGetRecursion1200Response storage_pool_volumes_type_snapshots_get_recursion1(project=project, target=target)

Get the storage volume snapshots

Returns a list of storage volume snapshots (structs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pool_volumes_type_snapshots_get_recursion1200_response import StoragePoolVolumesTypeSnapshotsGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Get the storage volume snapshots
        api_response = await api_instance.storage_pool_volumes_type_snapshots_get_recursion1(project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_snapshots_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_snapshots_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**StoragePoolVolumesTypeSnapshotsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolVolumesTypeSnapshotsGetRecursion1200Response.md)

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

# **storage_pool_volumes_type_snapshots_post**
> ClusterMembersPost202Response storage_pool_volumes_type_snapshots_post(volume, project=project, target=target)

Create a storage volume snapshot

Creates a new storage volume snapshot.

### Example


```python
import pyincusd
from pyincusd.models.cluster_members_post202_response import ClusterMembersPost202Response
from pyincusd.models.storage_volume_snapshots_post import StorageVolumeSnapshotsPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    volume = pyincusd.StorageVolumeSnapshotsPost() # StorageVolumeSnapshotsPost | Storage volume snapshot
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Create a storage volume snapshot
        api_response = await api_instance.storage_pool_volumes_type_snapshots_post(volume, project=project, target=target)
        print("The response of StorageApi->storage_pool_volumes_type_snapshots_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pool_volumes_type_snapshots_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume** | [**StorageVolumeSnapshotsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StorageVolumeSnapshotsPost.md)| Storage volume snapshot | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ClusterMembersPost202Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ClusterMembersPost202Response.md)

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

# **storage_pools_delete**
> ServerPut200Response storage_pools_delete(project=project)

Delete the storage pool

Removes the storage pool.

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
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)

    try:
        # Delete the storage pool
        api_response = await api_instance.storage_pools_delete(project=project)
        print("The response of StorageApi->storage_pools_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pools_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pools_get**
> StoragePoolsGet200Response storage_pools_get(project=project, filter=filter)

Get the storage pools

Returns a list of storage pools (URLs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pools_get200_response import StoragePoolsGet200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the storage pools
        api_response = await api_instance.storage_pools_get(project=project, filter=filter)
        print("The response of StorageApi->storage_pools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**StoragePoolsGet200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolsGet200Response.md)

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

# **storage_pools_get_recursion1**
> StoragePoolsGetRecursion1200Response storage_pools_get_recursion1(project=project, filter=filter)

Get the storage pools

Returns a list of storage pools (structs).

### Example


```python
import pyincusd
from pyincusd.models.storage_pools_get_recursion1200_response import StoragePoolsGetRecursion1200Response
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    project = 'project_example' # str | Project name (optional)
    filter = 'filter_example' # str | Collection filter (optional)

    try:
        # Get the storage pools
        api_response = await api_instance.storage_pools_get_recursion1(project=project, filter=filter)
        print("The response of StorageApi->storage_pools_get_recursion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pools_get_recursion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project name | [optional] 
 **filter** | **str**| Collection filter | [optional] 

### Return type

[**StoragePoolsGetRecursion1200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolsGetRecursion1200Response.md)

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

# **storage_pools_post**
> ServerPut200Response storage_pools_post(storage, project=project, target=target)

Add a storage pool

Creates a new storage pool.
When clustered, storage pools require individual POST for each cluster member prior to a global POST.

### Example


```python
import pyincusd
from pyincusd.models.server_put200_response import ServerPut200Response
from pyincusd.models.storage_pools_post import StoragePoolsPost
from pyincusd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyincusd.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyincusd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyincusd.StorageApi(api_client)
    storage = pyincusd.StoragePoolsPost() # StoragePoolsPost | Storage pool
    project = 'project_example' # str | Project name (optional)
    target = 'target_example' # str | Cluster member name (optional)

    try:
        # Add a storage pool
        api_response = await api_instance.storage_pools_post(storage, project=project, target=target)
        print("The response of StorageApi->storage_pools_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_pools_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage** | [**StoragePoolsPost**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/StoragePoolsPost.md)| Storage pool | 
 **project** | **str**| Project name | [optional] 
 **target** | **str**| Cluster member name | [optional] 

### Return type

[**ServerPut200Response**](https://github.com/anonhostpi/pyincusd/blob/v6.23.0.post8/docs/ServerPut200Response.md)

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

