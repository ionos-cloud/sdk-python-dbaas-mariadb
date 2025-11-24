# ionoscloud_dbaas_mariadb.BackupsApi

All URIs are relative to *https://mariadb.de-txl.ionos.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backups_find_by_id**](BackupsApi.md#backups_find_by_id) | **GET** /backups/{backupId} | Fetch backups
[**backups_get**](BackupsApi.md#backups_get) | **GET** /backups | List of backups.
[**cluster_backups_get**](BackupsApi.md#cluster_backups_get) | **GET** /clusters/{clusterId}/backups | List backups of cluster


# **backups_find_by_id**
> BackupResponse backups_find_by_id(backup_id)

Fetch backups

Retrieve a MariaDB backup by ID. This value can be
found when you GET the list of MariaDB backups.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mariadb
from ionoscloud_dbaas_mariadb.models.backup_response import BackupResponse
from ionoscloud_dbaas_mariadb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mariadb.de-txl.ionos.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_dbaas_mariadb.Configuration(
    host = "https://mariadb.de-txl.ionos.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_dbaas_mariadb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_mariadb.BackupsApi(api_client)
    backup_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the backup.

    try:
        # Fetch backups
        api_response = api_instance.backups_find_by_id(backup_id)
        print("The response of BackupsApi->backups_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->backups_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_id** | **str**| The unique ID of the backup. | 

### Return type

[**BackupResponse**](BackupResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Parse error. |  -  |
**401** | Authentication error. |  -  |
**403** | Unauthorized. |  -  |
**404** | Not Found. |  -  |
**405** | Unsupported HTTP method. |  -  |
**415** | Unsupported content type. |  -  |
**422** | Validation error. |  -  |
**429** | Request rate limit exceeded. |  -  |
**500** | Server error. |  -  |
**503** | Maintenance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backups_get**
> BackupList backups_get(limit=limit, offset=offset)

List of backups.

Retrieves all lists of backups for all MariaDB clusters in this contract.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mariadb
from ionoscloud_dbaas_mariadb.models.backup_list import BackupList
from ionoscloud_dbaas_mariadb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mariadb.de-txl.ionos.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_dbaas_mariadb.Configuration(
    host = "https://mariadb.de-txl.ionos.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_dbaas_mariadb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_mariadb.BackupsApi(api_client)
    limit = 100 # int | The maximum number of elements to return. Use together with 'offset' for pagination. (optional) (default to 100)
    offset = 0 # int | The first element to return. Use together with 'limit' for pagination. (optional) (default to 0)

    try:
        # List of backups.
        api_response = api_instance.backups_get(limit=limit, offset=offset)
        print("The response of BackupsApi->backups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->backups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100]
 **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0]

### Return type

[**BackupList**](BackupList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Parse error. |  -  |
**401** | Authentication error. |  -  |
**403** | Unauthorized. |  -  |
**404** | Not Found. |  -  |
**405** | Unsupported HTTP method. |  -  |
**415** | Unsupported content type. |  -  |
**422** | Validation error. |  -  |
**429** | Request rate limit exceeded. |  -  |
**500** | Server error. |  -  |
**503** | Maintenance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_backups_get**
> BackupList cluster_backups_get(cluster_id, limit=limit, offset=offset)

List backups of cluster

Retrieves a list of all backups of the given MariaDB cluster.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mariadb
from ionoscloud_dbaas_mariadb.models.backup_list import BackupList
from ionoscloud_dbaas_mariadb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mariadb.de-txl.ionos.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_dbaas_mariadb.Configuration(
    host = "https://mariadb.de-txl.ionos.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_dbaas_mariadb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_mariadb.BackupsApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    limit = 100 # int | The maximum number of elements to return. Use together with 'offset' for pagination. (optional) (default to 100)
    offset = 0 # int | The first element to return. Use together with 'limit' for pagination. (optional) (default to 0)

    try:
        # List backups of cluster
        api_response = api_instance.cluster_backups_get(cluster_id, limit=limit, offset=offset)
        print("The response of BackupsApi->cluster_backups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->cluster_backups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 
 **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100]
 **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0]

### Return type

[**BackupList**](BackupList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Parse error. |  -  |
**401** | Authentication error. |  -  |
**403** | Unauthorized. |  -  |
**404** | Not Found. |  -  |
**405** | Unsupported HTTP method. |  -  |
**415** | Unsupported content type. |  -  |
**422** | Validation error. |  -  |
**429** | Request rate limit exceeded. |  -  |
**500** | Server error. |  -  |
**503** | Maintenance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

