# ClusterProperties

Properties of a database cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The friendly name of your cluster. | [optional] 
**mariadb_version** | [**MariadbVersion**](MariadbVersion.md) |  | [optional] 
**dns_name** | **str** | The DNS name pointing to your cluster. | [optional] 
**instances** | **int** | The total number of instances in the cluster (one primary and n-1 secondary).  | [optional] 
**ram** | **int** | The amount of memory per instance in gigabytes (GB). | [optional] 
**cores** | **int** | The number of CPU cores per instance. | [optional] 
**storage_size** | **int** | The amount of storage per instance in gigabytes (GB). | [optional] 
**connections** | [**list[Connection]**](Connection.md) |  | [optional] 
**maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional] 
**backup** | [**BackupProperties**](BackupProperties.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.cluster_properties import ClusterProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProperties from a JSON string
cluster_properties_instance = ClusterProperties.from_json(json)
# print the JSON string representation of the object
print(ClusterProperties.to_json())

# convert the object into a dict
cluster_properties_dict = cluster_properties_instance.to_dict()
# create an instance of ClusterProperties from a dict
cluster_properties_from_dict = ClusterProperties.from_dict(cluster_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


