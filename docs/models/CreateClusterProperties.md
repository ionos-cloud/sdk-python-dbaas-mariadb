# CreateClusterProperties

Properties with all data needed to create a new MariaDB cluster. 
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **mariadb_version** | [**MariadbVersion**](MariadbVersion.md) |  |  |
| **instances** | **int** | The total number of instances in the cluster (one primary and n-1 secondary).  |  |
| **cores** | **int** | The number of CPU cores per instance. |  |
| **ram** | **int** | The amount of memory per instance in gigabytes (GB). |  |
| **storage_size** | **int** | The amount of storage per instance in gigabytes (GB). |  |
| **connections** | [**list[Connection]**](Connection.md) | The network connection for your cluster. Only one connection is allowed.  |  |
| **display_name** | **str** | The friendly name of your cluster. |  |
| **maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional]  |
| **credentials** | [**DBUser**](DBUser.md) |  |  |


