# ClustersGet405Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_status** | **int** | The HTTP status code of the operation. | 
**messages** | [**list[ErrorMessage]**](ErrorMessage.md) |  | 

## Example

```python
from ionoscloud_dbaas_mariadb.models.clusters_get405_response import ClustersGet405Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClustersGet405Response from a JSON string
clusters_get405_response_instance = ClustersGet405Response.from_json(json)
# print the JSON string representation of the object
print(ClustersGet405Response.to_json())

# convert the object into a dict
clusters_get405_response_dict = clusters_get405_response_instance.to_dict()
# create an instance of ClustersGet405Response from a dict
clusters_get405_response_from_dict = ClustersGet405Response.from_dict(clusters_get405_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


