# BackupList

List of backups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | The offset specified in the request (if none was specified, the default offset is 0).  | [optional] [default to 0]
**limit** | **int** | The limit specified in the request (if none was specified, the default limit is 100).  | [optional] [default to 100]
**total** | **int** | The total number of elements matching the request (without pagination).  | [optional] [default to 0]
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 
**id** | **str** | The unique ID of the resource. | [optional] 
**items** | [**list[BackupResponse]**](BackupResponse.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.backup_list import BackupList

# TODO update the JSON string below
json = "{}"
# create an instance of BackupList from a JSON string
backup_list_instance = BackupList.from_json(json)
# print the JSON string representation of the object
print(BackupList.to_json())

# convert the object into a dict
backup_list_dict = backup_list_instance.to_dict()
# create an instance of BackupList from a dict
backup_list_from_dict = BackupList.from_dict(backup_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


