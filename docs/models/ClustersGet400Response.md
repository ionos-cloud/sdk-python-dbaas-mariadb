# ClustersGet400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_status** | **int** | The HTTP status code of the operation. | 
**messages** | [**list[ErrorMessage]**](ErrorMessage.md) |  | 

## Example

```python
from ionoscloud_dbaas_mariadb.models.clusters_get400_response import ClustersGet400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClustersGet400Response from a JSON string
clusters_get400_response_instance = ClustersGet400Response.from_json(json)
# print the JSON string representation of the object
print(ClustersGet400Response.to_json())

# convert the object into a dict
clusters_get400_response_dict = clusters_get400_response_instance.to_dict()
# create an instance of ClustersGet400Response from a dict
clusters_get400_response_from_dict = ClustersGet400Response.from_dict(clusters_get400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


