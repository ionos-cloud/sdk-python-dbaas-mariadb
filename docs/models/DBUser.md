# DBUser

Credentials for the database user to be created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The username for the initial MariaDB user. Some system usernames are restricted (e.g. \&quot;mariadb\&quot;, \&quot;admin\&quot;, \&quot;standby\&quot;).  The username should be compliant with the following rules: - Must not exceed 16 characters - Must start with a letter - Must contain only letters, numbers, or underscores  | 
**password** | **str** | The password for a MariaDB user. | 

## Example

```python
from ionoscloud_dbaas_mariadb.models.db_user import DBUser

# TODO update the JSON string below
json = "{}"
# create an instance of DBUser from a JSON string
db_user_instance = DBUser.from_json(json)
# print the JSON string representation of the object
print(DBUser.to_json())

# convert the object into a dict
db_user_dict = db_user_instance.to_dict()
# create an instance of DBUser from a dict
db_user_from_dict = DBUser.from_dict(db_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


