# CreateClusterProperties

Properties with all data needed to create a new MariaDB cluster. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mariadb_version** | [**MariadbVersion**](MariadbVersion.md) |  | 
**instances** | **int** | The total number of instances in the cluster (one primary and n-1 secondary).  | 
**cores** | **int** | The number of CPU cores per instance. | 
**ram** | **int** | The amount of memory per instance in gigabytes (GB). | 
**storage_size** | **int** | The amount of storage per instance in gigabytes (GB). | 
**connections** | [**list[Connection]**](Connection.md) | The network connection for your cluster. Only one connection is allowed.  | 
**display_name** | **str** | The friendly name of your cluster. | 
**maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional] 
**backup** | [**BackupProperties**](BackupProperties.md) |  | [optional] 
**credentials** | [**DBUser**](DBUser.md) |  | 
**from_backup** | [**RestoreRequest**](RestoreRequest.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.create_cluster_properties import CreateClusterProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterProperties from a JSON string
create_cluster_properties_instance = CreateClusterProperties.from_json(json)
# print the JSON string representation of the object
print(CreateClusterProperties.to_json())

# convert the object into a dict
create_cluster_properties_dict = create_cluster_properties_instance.to_dict()
# create an instance of CreateClusterProperties from a dict
create_cluster_properties_from_dict = CreateClusterProperties.from_dict(create_cluster_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


