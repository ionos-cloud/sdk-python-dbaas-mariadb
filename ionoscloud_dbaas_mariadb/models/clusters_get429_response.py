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


class ClustersGet429Response(object):
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

        'http_status': 'int',

        'messages': 'list[ErrorMessage]',
    }

    attribute_map = {

        'http_status': 'httpStatus',

        'messages': 'messages',
    }

    def __init__(self, http_status=None, messages=None, local_vars_configuration=None):  # noqa: E501
        """ClustersGet429Response - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._http_status = None
        self._messages = None
        self.discriminator = None

        self.http_status = http_status
        self.messages = messages


    @property
    def http_status(self):
        """Gets the http_status of this ClustersGet429Response.  # noqa: E501

        The HTTP status code of the operation.  # noqa: E501

        :return: The http_status of this ClustersGet429Response.  # noqa: E501
        :rtype: int
        """
        return self._http_status

    @http_status.setter
    def http_status(self, http_status):
        """Sets the http_status of this ClustersGet429Response.

        The HTTP status code of the operation.  # noqa: E501

        :param http_status: The http_status of this ClustersGet429Response.  # noqa: E501
        :type http_status: int
        """
        if self.local_vars_configuration.client_side_validation and http_status is None:  # noqa: E501
            raise ValueError("Invalid value for `http_status`, must not be `None`")  # noqa: E501

        self._http_status = http_status

    @property
    def messages(self):
        """Gets the messages of this ClustersGet429Response.  # noqa: E501


        :return: The messages of this ClustersGet429Response.  # noqa: E501
        :rtype: list[ErrorMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this ClustersGet429Response.


        :param messages: The messages of this ClustersGet429Response.  # noqa: E501
        :type messages: list[ErrorMessage]
        """
        if self.local_vars_configuration.client_side_validation and messages is None:  # noqa: E501
            raise ValueError("Invalid value for `messages`, must not be `None`")  # noqa: E501

        self._messages = messages
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
        if not isinstance(other, ClustersGet429Response):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClustersGet429Response):
            return True

        return self.to_dict() != other.to_dict()
