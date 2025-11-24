# ClustersGet422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_status** | **int** | The HTTP status code of the operation. | 
**messages** | [**list[ErrorMessage]**](ErrorMessage.md) |  | 

## Example

```python
from ionoscloud_dbaas_mariadb.models.clusters_get422_response import ClustersGet422Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClustersGet422Response from a JSON string
clusters_get422_response_instance = ClustersGet422Response.from_json(json)
# print the JSON string representation of the object
print(ClustersGet422Response.to_json())

# convert the object into a dict
clusters_get422_response_dict = clusters_get422_response_instance.to_dict()
# create an instance of ClustersGet422Response from a dict
clusters_get422_response_from_dict = ClustersGet422Response.from_dict(clusters_get422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


