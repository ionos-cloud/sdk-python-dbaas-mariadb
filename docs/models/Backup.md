# Backup

A backup object.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **cluster_id** | **str** | The unique ID of the cluster that was backed up. | [optional]  |
| **earliest_recovery_target_time** | **datetime** | The oldest available timestamp to which you can restore. | [optional]  |
| **size** | **int** | Size of all base backups in MiB. This is at least the sum of all base backup sizes.  | [optional]  |
| **base_backups** | [**list[BaseBackup]**](BaseBackup.md) |  | [optional]  |


