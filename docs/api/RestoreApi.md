# ionoscloud_dbaas_mariadb.RestoreApi

All URIs are relative to *https://mariadb.de-txl.ionos.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusters_restore**](RestoreApi.md#clusters_restore) | **POST** /clusters/{clusterId}/restore | In-place restore of a cluster.


# **clusters_restore**
> clusters_restore(cluster_id, restore_request)

In-place restore of a cluster.

Restore a MariaDB cluster from a backup.

Conditions:
 - The backup must belong to the MariaDB cluster to
   be restored.
 - The cluster must be in the state "AVAILABLE".

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mariadb
from ionoscloud_dbaas_mariadb.models.restore_request import RestoreRequest
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
    api_instance = ionoscloud_dbaas_mariadb.RestoreApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    restore_request = ionoscloud_dbaas_mariadb.RestoreRequest() # RestoreRequest | The backup to restore from.

    try:
        # In-place restore of a cluster.
        api_instance.clusters_restore(cluster_id, restore_request)
    except Exception as e:
        print("Exception when calling RestoreApi->clusters_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 
 **restore_request** | [**RestoreRequest**](RestoreRequest.md)| The backup to restore from. | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation. |  -  |
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

