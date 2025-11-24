# ClusterMetadata

Metadata of the resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | The ISO 8601 creation timestamp. | [optional] 
**created_by** | **str** |  | [optional] 
**created_by_user_id** | **str** |  | [optional] 
**last_modified_date** | **datetime** | The ISO 8601 modified timestamp. | [optional] 
**last_modified_by** | **str** |  | [optional] 
**last_modified_by_user_id** | **str** |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.cluster_metadata import ClusterMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMetadata from a JSON string
cluster_metadata_instance = ClusterMetadata.from_json(json)
# print the JSON string representation of the object
print(ClusterMetadata.to_json())

# convert the object into a dict
cluster_metadata_dict = cluster_metadata_instance.to_dict()
# create an instance of ClusterMetadata from a dict
cluster_metadata_from_dict = ClusterMetadata.from_dict(cluster_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


