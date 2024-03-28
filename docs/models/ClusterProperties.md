# ClusterProperties

Properties of a database cluster.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **display_name** | **str** | The friendly name of your cluster. | [optional]  |
| **mariadb_version** | [**MariadbVersion**](MariadbVersion.md) |  | [optional]  |
| **dns_name** | **str** | The DNS name pointing to your cluster. | [optional]  |
| **instances** | **int** | The total number of instances in the cluster (one primary and n-1 secondary).  | [optional]  |
| **ram** | **int** | The amount of memory per instance in gigabytes (GB). | [optional]  |
| **cores** | **int** | The number of CPU cores per instance. | [optional]  |
| **storage_size** | **int** | The amount of storage per instance in gigabytes (GB). | [optional]  |
| **connections** | [**list[Connection]**](Connection.md) |  | [optional]  |
| **maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional]  |


