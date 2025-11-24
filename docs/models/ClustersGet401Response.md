# ClustersGet401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_status** | **int** | The HTTP status code of the operation. | 
**messages** | [**list[ErrorMessage]**](ErrorMessage.md) |  | 

## Example

```python
from ionoscloud_dbaas_mariadb.models.clusters_get401_response import ClustersGet401Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClustersGet401Response from a JSON string
clusters_get401_response_instance = ClustersGet401Response.from_json(json)
# print the JSON string representation of the object
print(ClustersGet401Response.to_json())

# convert the object into a dict
clusters_get401_response_dict = clusters_get401_response_instance.to_dict()
# create an instance of ClustersGet401Response from a dict
clusters_get401_response_from_dict = ClustersGet401Response.from_dict(clusters_get401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


