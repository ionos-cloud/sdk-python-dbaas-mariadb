# BaseBackup

A single base backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The ISO 8601 creation timestamp. | [optional] 
**size** | **int** | The size of the backup in MiB. This is the size of the binary backup file that was stored.  | [optional] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.base_backup import BaseBackup

# TODO update the JSON string below
json = "{}"
# create an instance of BaseBackup from a JSON string
base_backup_instance = BaseBackup.from_json(json)
# print the JSON string representation of the object
print(BaseBackup.to_json())

# convert the object into a dict
base_backup_dict = base_backup_instance.to_dict()
# create an instance of BaseBackup from a dict
base_backup_from_dict = BaseBackup.from_dict(base_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


