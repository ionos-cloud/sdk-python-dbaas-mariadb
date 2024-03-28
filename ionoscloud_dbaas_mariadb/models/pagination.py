# coding: utf-8

"""
    IONOS DBaaS MariaDB REST API

    An enterprise-grade Database is provided as a Service (DBaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.  The API allows you to create additional MariaDB database clusters or modify existing ones. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_dbaas_mariadb.configuration import Configuration


class Pagination(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {

        'offset': 'int',

        'limit': 'int',

        'total': 'int',

        'links': 'PaginationLinks',
    }

    attribute_map = {

        'offset': 'offset',

        'limit': 'limit',

        'total': 'total',

        'links': '_links',
    }

    def __init__(self, offset=0, limit=100, total=0, links=None, local_vars_configuration=None):  # noqa: E501
        """Pagination - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._offset = None
        self._limit = None
        self._total = None
        self._links = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if links is not None:
            self.links = links


    @property
    def offset(self):
        """Gets the offset of this Pagination.  # noqa: E501

        The offset specified in the request (if none was specified, the default offset is 0).   # noqa: E501

        :return: The offset of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Pagination.

        The offset specified in the request (if none was specified, the default offset is 0).   # noqa: E501

        :param offset: The offset of this Pagination.  # noqa: E501
        :type offset: int
        """
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this Pagination.  # noqa: E501

        The limit specified in the request (if none was specified, the default limit is 100).   # noqa: E501

        :return: The limit of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Pagination.

        The limit specified in the request (if none was specified, the default limit is 100).   # noqa: E501

        :param limit: The limit of this Pagination.  # noqa: E501
        :type limit: int
        """
        if (self.local_vars_configuration.client_side_validation and
                limit is not None and limit > 1000):  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                limit is not None and limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._limit = limit

    @property
    def total(self):
        """Gets the total of this Pagination.  # noqa: E501

        The total number of elements matching the request (without pagination).   # noqa: E501

        :return: The total of this Pagination.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Pagination.

        The total number of elements matching the request (without pagination).   # noqa: E501

        :param total: The total of this Pagination.  # noqa: E501
        :type total: int
        """
        if (self.local_vars_configuration.client_side_validation and
                total is not None and total < 0):  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total = total

    @property
    def links(self):
        """Gets the links of this Pagination.  # noqa: E501


        :return: The links of this Pagination.  # noqa: E501
        :rtype: PaginationLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Pagination.


        :param links: The links of this Pagination.  # noqa: E501
        :type links: PaginationLinks
        """

        self._links = links
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Pagination):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Pagination):
            return True

        return self.to_dict() != other.to_dict()
