# ClustersGet503Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_status** | **int** | The HTTP status code of the operation. | 
**messages** | [**list[ErrorMessage]**](ErrorMessage.md) |  | 

## Example

```python
from ionoscloud_dbaas_mariadb.models.clusters_get503_response import ClustersGet503Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClustersGet503Response from a JSON string
clusters_get503_response_instance = ClustersGet503Response.from_json(json)
# print the JSON string representation of the object
print(ClustersGet503Response.to_json())

# convert the object into a dict
clusters_get503_response_dict = clusters_get503_response_instance.to_dict()
# create an instance of ClustersGet503Response from a dict
clusters_get503_response_from_dict = ClustersGet503Response.from_dict(clusters_get503_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


