# BackupProperties

Properties configuring the backup of the cluster. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | The S3 location where the backups will be stored. | [optional] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.backup_properties import BackupProperties

# TODO update the JSON string below
json = "{}"
# create an instance of BackupProperties from a JSON string
backup_properties_instance = BackupProperties.from_json(json)
# print the JSON string representation of the object
print(BackupProperties.to_json())

# convert the object into a dict
backup_properties_dict = backup_properties_instance.to_dict()
# create an instance of BackupProperties from a dict
backup_properties_from_dict = BackupProperties.from_dict(backup_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


