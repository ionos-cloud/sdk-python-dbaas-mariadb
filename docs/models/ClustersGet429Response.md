# ClustersGet429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_status** | **int** | The HTTP status code of the operation. | 
**messages** | [**list[ErrorMessage]**](ErrorMessage.md) |  | 

## Example

```python
from ionoscloud_dbaas_mariadb.models.clusters_get429_response import ClustersGet429Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClustersGet429Response from a JSON string
clusters_get429_response_instance = ClustersGet429Response.from_json(json)
# print the JSON string representation of the object
print(ClustersGet429Response.to_json())

# convert the object into a dict
clusters_get429_response_dict = clusters_get429_response_instance.to_dict()
# create an instance of ClustersGet429Response from a dict
clusters_get429_response_from_dict = ClustersGet429Response.from_dict(clusters_get429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


