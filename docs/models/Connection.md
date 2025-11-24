# Connection

Details about the network connection for your cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter_id** | **str** | The datacenter to connect your cluster to. | 
**lan_id** | **str** | The numeric LAN ID to connect your cluster to. | 
**cidr** | **str** | The IP and subnet for your cluster. Note the following unavailable IP ranges: 10.233.64.0/18 10.233.0.0/18 10.233.114.0/24  | 

## Example

```python
from ionoscloud_dbaas_mariadb.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print(Connection.to_json())

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_from_dict = Connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


