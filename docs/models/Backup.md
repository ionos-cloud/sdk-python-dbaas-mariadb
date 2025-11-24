# Backup

A backup object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The unique ID of the cluster that was backed up. | [optional] 
**location** | **str** | The S3 location where the backups will be stored. | [optional] 
**earliest_recovery_target_time** | **datetime** | The oldest available timestamp to which you can restore. | [optional] 
**size** | **int** | Size of all base backups in MiB. This is at least the sum of all base backup sizes.  | [optional] 
**base_backups** | [**list[BaseBackup]**](BaseBackup.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.backup import Backup

# TODO update the JSON string below
json = "{}"
# create an instance of Backup from a JSON string
backup_instance = Backup.from_json(json)
# print the JSON string representation of the object
print(Backup.to_json())

# convert the object into a dict
backup_dict = backup_instance.to_dict()
# create an instance of Backup from a dict
backup_from_dict = Backup.from_dict(backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


