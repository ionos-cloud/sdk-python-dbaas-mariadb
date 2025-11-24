# CreateClusterRequest

Request payload with all data needed to create a new MariaDB cluster. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**CreateClusterProperties**](CreateClusterProperties.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.create_cluster_request import CreateClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterRequest from a JSON string
create_cluster_request_instance = CreateClusterRequest.from_json(json)
# print the JSON string representation of the object
print(CreateClusterRequest.to_json())

# convert the object into a dict
create_cluster_request_dict = create_cluster_request_instance.to_dict()
# create an instance of CreateClusterRequest from a dict
create_cluster_request_from_dict = CreateClusterRequest.from_dict(create_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


