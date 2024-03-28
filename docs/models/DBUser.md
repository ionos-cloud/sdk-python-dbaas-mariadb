# DBUser

Credentials for the database user to be created.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **username** | **str** | The username for the initial MariaDB user. Some system usernames are restricted (e.g. \&quot;mariadb\&quot;, \&quot;admin\&quot;, \&quot;standby\&quot;).  The username should be compliant with the following rules: - Must not exceed 16 characters - Must start with a letter - Must contain only letters, numbers, or underscores  |  |
| **password** | **str** | The password for a MariaDB user. |  |


