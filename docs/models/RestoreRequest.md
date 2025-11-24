# RestoreRequest

Request payload to restore a cluster from a backup. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_id** | **str** | The unique ID of the resource. | 
**recovery_target_time** | **datetime** | The timestamp to which the cluster should be restored. If empty, the backup will be applied to the latest timestamp.  This value must be supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp. If empty, the backup will be applied completely.  Must be within the earliestRecoveryTargetTime and now.  The earliestRecoveryTargetTime can be looked up in the backup object.  | [optional] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.restore_request import RestoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreRequest from a JSON string
restore_request_instance = RestoreRequest.from_json(json)
# print the JSON string representation of the object
print(RestoreRequest.to_json())

# convert the object into a dict
restore_request_dict = restore_request_instance.to_dict()
# create an instance of RestoreRequest from a dict
restore_request_from_dict = RestoreRequest.from_dict(restore_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


