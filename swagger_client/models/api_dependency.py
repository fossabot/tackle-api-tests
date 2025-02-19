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


class ApiDependency(object):
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
        'create_time': 'str',
        'create_user': 'str',
        '_from': 'ApiRef',
        'id': 'int',
        'to': 'ApiRef',
        'update_user': 'str'
    }

    attribute_map = {
        'create_time': 'createTime',
        'create_user': 'createUser',
        '_from': 'from',
        'id': 'id',
        'to': 'to',
        'update_user': 'updateUser'
    }

    def __init__(self, create_time=None, create_user=None, _from=None, id=None, to=None, update_user=None, _configuration=None):  # noqa: E501
        """ApiDependency - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._create_user = None
        self.__from = None
        self._id = None
        self._to = None
        self._update_user = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if _from is not None:
            self._from = _from
        if id is not None:
            self.id = id
        if to is not None:
            self.to = to
        if update_user is not None:
            self.update_user = update_user

    @property
    def create_time(self):
        """Gets the create_time of this ApiDependency.  # noqa: E501


        :return: The create_time of this ApiDependency.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiDependency.


        :param create_time: The create_time of this ApiDependency.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this ApiDependency.  # noqa: E501


        :return: The create_user of this ApiDependency.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ApiDependency.


        :param create_user: The create_user of this ApiDependency.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def _from(self):
        """Gets the _from of this ApiDependency.  # noqa: E501


        :return: The _from of this ApiDependency.  # noqa: E501
        :rtype: ApiRef
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ApiDependency.


        :param _from: The _from of this ApiDependency.  # noqa: E501
        :type: ApiRef
        """

        self.__from = _from

    @property
    def id(self):
        """Gets the id of this ApiDependency.  # noqa: E501


        :return: The id of this ApiDependency.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiDependency.


        :param id: The id of this ApiDependency.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def to(self):
        """Gets the to of this ApiDependency.  # noqa: E501


        :return: The to of this ApiDependency.  # noqa: E501
        :rtype: ApiRef
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ApiDependency.


        :param to: The to of this ApiDependency.  # noqa: E501
        :type: ApiRef
        """

        self._to = to

    @property
    def update_user(self):
        """Gets the update_user of this ApiDependency.  # noqa: E501


        :return: The update_user of this ApiDependency.  # noqa: E501
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this ApiDependency.


        :param update_user: The update_user of this ApiDependency.  # noqa: E501
        :type: str
        """

        self._update_user = update_user

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
        if issubclass(ApiDependency, dict):
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
        if not isinstance(other, ApiDependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiDependency):
            return True

        return self.to_dict() != other.to_dict()
