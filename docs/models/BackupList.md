# BackupList

List of backups.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **str** | The unique ID of the resource. | [optional]  |
| **items** | [**list[BackupResponse]**](BackupResponse.md) |  | [optional]  |
| **offset** | **int** | The offset specified in the request (if none was specified, the default offset is 0).  | [optional] [default to 0] |
| **limit** | **int** | The limit specified in the request (if none was specified, the default limit is 100).  | [optional] [default to 100] |
| **total** | **int** | The total number of elements matching the request (without pagination).  | [optional] [default to 0] |
| **links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional]  |


