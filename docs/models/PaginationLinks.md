# PaginationLinks

URLs to navigate the different pages. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | **str** | URL (with offset and limit parameters) of the previous page; only present if offset is greater than 0.  | [optional] [readonly] 
**var_self** | **str** | URL (with offset and limit parameters) of the current page.  | [optional] [readonly] 
**next** | **str** | URL (with offset and limit parameters) of the next page; only present if offset + limit is less than the total number of elements.  | [optional] [readonly] 

## Example

```python
from ionoscloud_dbaas_mariadb.models.pagination_links import PaginationLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationLinks from a JSON string
pagination_links_instance = PaginationLinks.from_json(json)
# print the JSON string representation of the object
print(PaginationLinks.to_json())

# convert the object into a dict
pagination_links_dict = pagination_links_instance.to_dict()
# create an instance of PaginationLinks from a dict
pagination_links_from_dict = PaginationLinks.from_dict(pagination_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


