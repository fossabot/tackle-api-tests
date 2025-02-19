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


class ApiStakeholders(object):
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
        'contributors': 'list[ApiRef]',
        'owner': 'ApiRef'
    }

    attribute_map = {
        'contributors': 'contributors',
        'owner': 'owner'
    }

    def __init__(self, contributors=None, owner=None, _configuration=None):  # noqa: E501
        """ApiStakeholders - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._contributors = None
        self._owner = None
        self.discriminator = None

        if contributors is not None:
            self.contributors = contributors
        if owner is not None:
            self.owner = owner

    @property
    def contributors(self):
        """Gets the contributors of this ApiStakeholders.  # noqa: E501


        :return: The contributors of this ApiStakeholders.  # noqa: E501
        :rtype: list[ApiRef]
        """
        return self._contributors

    @contributors.setter
    def contributors(self, contributors):
        """Sets the contributors of this ApiStakeholders.


        :param contributors: The contributors of this ApiStakeholders.  # noqa: E501
        :type: list[ApiRef]
        """

        self._contributors = contributors

    @property
    def owner(self):
        """Gets the owner of this ApiStakeholders.  # noqa: E501


        :return: The owner of this ApiStakeholders.  # noqa: E501
        :rtype: ApiRef
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ApiStakeholders.


        :param owner: The owner of this ApiStakeholders.  # noqa: E501
        :type: ApiRef
        """

        self._owner = owner

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
        if issubclass(ApiStakeholders, dict):
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
        if not isinstance(other, ApiStakeholders):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiStakeholders):
            return True

        return self.to_dict() != other.to_dict()
