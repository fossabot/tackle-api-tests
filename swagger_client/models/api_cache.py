# coding: utf-8

"""
    MTA 6.1 api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ApiCache(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'capacity': 'str',
        'exists': 'bool',
        'path': 'str',
        'used': 'str'
    }

    attribute_map = {
        'capacity': 'capacity',
        'exists': 'exists',
        'path': 'path',
        'used': 'used'
    }

    def __init__(self, capacity=None, exists=None, path=None, used=None, _configuration=None):  # noqa: E501
        """ApiCache - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._capacity = None
        self._exists = None
        self._path = None
        self._used = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity
        if exists is not None:
            self.exists = exists
        if path is not None:
            self.path = path
        if used is not None:
            self.used = used

    @property
    def capacity(self):
        """Gets the capacity of this ApiCache.  # noqa: E501


        :return: The capacity of this ApiCache.  # noqa: E501
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this ApiCache.


        :param capacity: The capacity of this ApiCache.  # noqa: E501
        :type: str
        """

        self._capacity = capacity

    @property
    def exists(self):
        """Gets the exists of this ApiCache.  # noqa: E501


        :return: The exists of this ApiCache.  # noqa: E501
        :rtype: bool
        """
        return self._exists

    @exists.setter
    def exists(self, exists):
        """Sets the exists of this ApiCache.


        :param exists: The exists of this ApiCache.  # noqa: E501
        :type: bool
        """

        self._exists = exists

    @property
    def path(self):
        """Gets the path of this ApiCache.  # noqa: E501


        :return: The path of this ApiCache.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ApiCache.


        :param path: The path of this ApiCache.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def used(self):
        """Gets the used of this ApiCache.  # noqa: E501


        :return: The used of this ApiCache.  # noqa: E501
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ApiCache.


        :param used: The used of this ApiCache.  # noqa: E501
        :type: str
        """

        self._used = used

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ApiCache, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiCache):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiCache):
            return True

        return self.to_dict() != other.to_dict()
