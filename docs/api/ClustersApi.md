# ClustersApi

All URIs are relative to *https://mariadb.de-txl.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**clusters_delete**](ClustersApi.md#clusters_delete) | **DELETE** /clusters/{clusterId} | Delete a cluster |
| [**clusters_find_by_id**](ClustersApi.md#clusters_find_by_id) | **GET** /clusters/{clusterId} | Fetch a cluster |
| [**clusters_get**](ClustersApi.md#clusters_get) | **GET** /clusters | List clusters |
| [**clusters_post**](ClustersApi.md#clusters_post) | **POST** /clusters | Create a cluster |


# **clusters_delete**
> ClusterResponse clusters_delete(cluster_id)

Delete a cluster

Delete a MariaDB cluster.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |

### Return type

[**ClusterResponse**](../models/ClusterResponse.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_find_by_id**
> ClusterResponse clusters_find_by_id(cluster_id)

Fetch a cluster

You can retrieve a MariaDB cluster by using its ID. This value can be found in the response body when a MariaDB cluster is created or when you GET a list of MariaDB clusters. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |

### Return type

[**ClusterResponse**](../models/ClusterResponse.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_get**
> ClusterList clusters_get(limit=limit, offset=offset, filter_name=filter_name)

List clusters

Retrieves a list of MariaDB clusters.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100] |
| **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0] |
| **filter_name** | **str**| Response filter to list only the MariaDB clusters that contain the specified name. The value is case insensitive and matched on the &#39;displayName&#39; field.  | [optional]  |

### Return type

[**ClusterList**](../models/ClusterList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_post**
> ClusterResponse clusters_post(create_cluster_request)

Create a cluster

Creates a new MariaDB cluster. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **create_cluster_request** | [**CreateClusterRequest**](../models/CreateClusterRequest.md)| The cluster to be created. |  |

### Return type

[**ClusterResponse**](../models/ClusterResponse.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

