# ClustersGet403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_status** | **int** | The HTTP status code of the operation. | 
**messages** | [**list[ErrorMessage]**](ErrorMessage.md) |  | 

## Example

```python
from ionoscloud_dbaas_mariadb.models.clusters_get403_response import ClustersGet403Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClustersGet403Response from a JSON string
clusters_get403_response_instance = ClustersGet403Response.from_json(json)
# print the JSON string representation of the object
print(ClustersGet403Response.to_json())

# convert the object into a dict
clusters_get403_response_dict = clusters_get403_response_instance.to_dict()
# create an instance of ClustersGet403Response from a dict
clusters_get403_response_from_dict = ClustersGet403Response.from_dict(clusters_get403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


