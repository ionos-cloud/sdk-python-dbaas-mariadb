# BackupsApi

All URIs are relative to *https://mariadb.de-txl.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**backups_find_by_id**](BackupsApi.md#backups_find_by_id) | **GET** /backups/{backupId} | Fetch a cluster&#39;s backups |
| [**backups_get**](BackupsApi.md#backups_get) | **GET** /backups | List of cluster&#39;s backups. |
| [**cluster_backups_get**](BackupsApi.md#cluster_backups_get) | **GET** /clusters/{clusterId}/backups | List backups of cluster |


# **backups_find_by_id**
> BackupResponse backups_find_by_id(backup_id)

Fetch a cluster's backups

Retrieve a MariaDB cluster's backups by using its ID. This value can be found when you GET the list of MariaDB cluster backups. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **backup_id** | **str**| The unique ID of the backup. |  |

### Return type

[**BackupResponse**](../models/BackupResponse.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **backups_get**
> BackupList backups_get(limit=limit, offset=offset)

List of cluster's backups.

Retrieves all lists of backups for all MariaDB clusters in this contract. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100] |
| **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0] |

### Return type

[**BackupList**](../models/BackupList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **cluster_backups_get**
> BackupList cluster_backups_get(cluster_id, limit=limit, offset=offset)

List backups of cluster

Retrieves a list of all backups of the given MariaDB cluster. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100] |
| **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0] |

### Return type

[**BackupList**](../models/BackupList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

