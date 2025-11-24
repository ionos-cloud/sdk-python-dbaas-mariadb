# ionoscloud_dbaas_mariadb.ClustersApi

All URIs are relative to *https://mariadb.de-txl.ionos.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusters_delete**](ClustersApi.md#clusters_delete) | **DELETE** /clusters/{clusterId} | Delete a cluster
[**clusters_find_by_id**](ClustersApi.md#clusters_find_by_id) | **GET** /clusters/{clusterId} | Fetch a cluster
[**clusters_get**](ClustersApi.md#clusters_get) | **GET** /clusters | List clusters
[**clusters_patch**](ClustersApi.md#clusters_patch) | **PATCH** /clusters/{clusterId} | Update a cluster
[**clusters_post**](ClustersApi.md#clusters_post) | **POST** /clusters | Create a cluster


# **clusters_delete**
> ClusterResponse clusters_delete(cluster_id)

Delete a cluster

Delete a MariaDB cluster.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mariadb
from ionoscloud_dbaas_mariadb.models.cluster_response import ClusterResponse
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
    api_instance = ionoscloud_dbaas_mariadb.ClustersApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.

    try:
        # Delete a cluster
        api_response = api_instance.clusters_delete(cluster_id)
        print("The response of ClustersApi->clusters_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->clusters_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted cluster with &#x60;metadata.state&#x60; set to \&quot;DESTROYING\&quot;.  |  -  |
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

# **clusters_find_by_id**
> ClusterResponse clusters_find_by_id(cluster_id)

Fetch a cluster

You can retrieve a MariaDB cluster by using its ID. This value can be
found in the response body when a MariaDB cluster is created or when
you GET a list of MariaDB clusters.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mariadb
from ionoscloud_dbaas_mariadb.models.cluster_response import ClusterResponse
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
    api_instance = ionoscloud_dbaas_mariadb.ClustersApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.

    try:
        # Fetch a cluster
        api_response = api_instance.clusters_find_by_id(cluster_id)
        print("The response of ClustersApi->clusters_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->clusters_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

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

# **clusters_get**
> ClusterList clusters_get(limit=limit, offset=offset, filter_name=filter_name)

List clusters

Retrieves a list of MariaDB clusters.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mariadb
from ionoscloud_dbaas_mariadb.models.cluster_list import ClusterList
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
    api_instance = ionoscloud_dbaas_mariadb.ClustersApi(api_client)
    limit = 100 # int | The maximum number of elements to return. Use together with 'offset' for pagination. (optional) (default to 100)
    offset = 0 # int | The first element to return. Use together with 'limit' for pagination. (optional) (default to 0)
    filter_name = 'filter_name_example' # str | Response filter to list only the MariaDB clusters that contain the specified name. The value is case insensitive and matched on the 'displayName' field.  (optional)

    try:
        # List clusters
        api_response = api_instance.clusters_get(limit=limit, offset=offset, filter_name=filter_name)
        print("The response of ClustersApi->clusters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->clusters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100]
 **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0]
 **filter_name** | **str**| Response filter to list only the MariaDB clusters that contain the specified name. The value is case insensitive and matched on the &#39;displayName&#39; field.  | [optional] 

### Return type

[**ClusterList**](ClusterList.md)

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

# **clusters_patch**
> ClusterResponse clusters_patch(cluster_id, patch_cluster_request)

Update a cluster

Updates mutable attributes on a MariaDB cluster.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mariadb
from ionoscloud_dbaas_mariadb.models.cluster_response import ClusterResponse
from ionoscloud_dbaas_mariadb.models.patch_cluster_request import PatchClusterRequest
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
    api_instance = ionoscloud_dbaas_mariadb.ClustersApi(api_client)
    cluster_id = '498ae72f-411f-11eb-9d07-046c59cc737e' # str | The unique ID of the cluster.
    patch_cluster_request = ionoscloud_dbaas_mariadb.PatchClusterRequest() # PatchClusterRequest | Attributes of the cluster which should be modified.

    try:
        # Update a cluster
        api_response = api_instance.clusters_patch(cluster_id, patch_cluster_request)
        print("The response of ClustersApi->clusters_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->clusters_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 
 **patch_cluster_request** | [**PatchClusterRequest**](PatchClusterRequest.md)| Attributes of the cluster which should be modified. | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **clusters_post**
> ClusterResponse clusters_post(create_cluster_request)

Create a cluster

Creates a new MariaDB cluster.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mariadb
from ionoscloud_dbaas_mariadb.models.cluster_response import ClusterResponse
from ionoscloud_dbaas_mariadb.models.create_cluster_request import CreateClusterRequest
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
    api_instance = ionoscloud_dbaas_mariadb.ClustersApi(api_client)
    create_cluster_request = ionoscloud_dbaas_mariadb.CreateClusterRequest() # CreateClusterRequest | The cluster to be created.

    try:
        # Create a cluster
        api_response = api_instance.clusters_post(create_cluster_request)
        print("The response of ClustersApi->clusters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->clusters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cluster_request** | [**CreateClusterRequest**](CreateClusterRequest.md)| The cluster to be created. | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created cluster is returned with &#x60;metadata.state&#x60; set to \&quot;BUSY\&quot;.  |  -  |
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

