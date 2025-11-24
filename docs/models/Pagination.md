# Pagination

Pagination information in list responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | The offset specified in the request (if none was specified, the default offset is 0).  | [optional] [default to 0]
**limit** | **int** | The limit specified in the request (if none was specified, the default limit is 100).  | [optional] [default to 100]
**total** | **int** | The total number of elements matching the request (without pagination).  | [optional] [default to 0]
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print(Pagination.to_json())

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_from_dict = Pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


