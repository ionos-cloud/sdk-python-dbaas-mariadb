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


class ClusterListAllOf(object):
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

        'id': 'str',

        'items': 'list[ClusterResponse]',
    }

    attribute_map = {

        'id': 'id',

        'items': 'items',
    }

    def __init__(self, id=None, items=None, local_vars_configuration=None):  # noqa: E501
        """ClusterListAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._items = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if items is not None:
            self.items = items


    @property
    def id(self):
        """Gets the id of this ClusterListAllOf.  # noqa: E501

        The unique ID of the resource.  # noqa: E501

        :return: The id of this ClusterListAllOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterListAllOf.

        The unique ID of the resource.  # noqa: E501

        :param id: The id of this ClusterListAllOf.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def items(self):
        """Gets the items of this ClusterListAllOf.  # noqa: E501


        :return: The items of this ClusterListAllOf.  # noqa: E501
        :rtype: list[ClusterResponse]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ClusterListAllOf.


        :param items: The items of this ClusterListAllOf.  # noqa: E501
        :type items: list[ClusterResponse]
        """

        self._items = items
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
        if not isinstance(other, ClusterListAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterListAllOf):
            return True

        return self.to_dict() != other.to_dict()
