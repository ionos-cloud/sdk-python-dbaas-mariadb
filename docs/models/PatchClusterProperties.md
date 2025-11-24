# PatchClusterProperties

Properties of the payload to change a cluster: - instances can only be increased (3, 5, 7), - mariadbVersion can only be increased (no downgrade) - storageSize can only be increased, - ram and cores can be both increased and decreased. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mariadb_version** | [**MariadbVersion**](MariadbVersion.md) |  | [optional] 
**instances** | **int** | The total number of instances in the cluster (one primary and n-1 secondary).  | [optional] 
**cores** | **int** | The number of CPU cores per instance. | [optional] 
**ram** | **int** | The amount of memory per instance in gigabytes (GB). | [optional] 
**storage_size** | **int** | The amount of storage per instance in gigabytes (GB). | [optional] 
**display_name** | **str** | The friendly name of your cluster. | [optional] 
**maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.patch_cluster_properties import PatchClusterProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PatchClusterProperties from a JSON string
patch_cluster_properties_instance = PatchClusterProperties.from_json(json)
# print the JSON string representation of the object
print(PatchClusterProperties.to_json())

# convert the object into a dict
patch_cluster_properties_dict = patch_cluster_properties_instance.to_dict()
# create an instance of PatchClusterProperties from a dict
patch_cluster_properties_from_dict = PatchClusterProperties.from_dict(patch_cluster_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


