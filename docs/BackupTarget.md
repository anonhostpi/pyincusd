# BackupTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | AccessKey is the S3 API access key | [optional] 
**bucket_name** | **str** | BucketName is the name of the S3 bucket. | [optional] 
**path** | **str** | Path is the target path. | [optional] 
**protocol** | **str** | Protocol is the upload protocol. | [optional] 
**secret_key** | **str** | SecretKey is the S3 API access key | [optional] 
**url** | **str** | URL is the HTTPS URL for the backup | [optional] 

## Example

```python
from pyincusd.models.backup_target import BackupTarget

# TODO update the JSON string below
json = "{}"
# create an instance of BackupTarget from a JSON string
backup_target_instance = BackupTarget.from_json(json)
# print the JSON string representation of the object
print(BackupTarget.to_json())

# convert the object into a dict
backup_target_dict = backup_target_instance.to_dict()
# create an instance of BackupTarget from a dict
backup_target_from_dict = BackupTarget.from_dict(backup_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


