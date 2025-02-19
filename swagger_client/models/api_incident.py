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


class ApiIncident(object):
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
        'code_snip': 'str',
        'create_time': 'str',
        'create_user': 'str',
        'facts': 'ApiFactMap',
        'file': 'str',
        'id': 'int',
        'line': 'int',
        'message': 'str',
        'update_user': 'str'
    }

    attribute_map = {
        'code_snip': 'codeSnip',
        'create_time': 'createTime',
        'create_user': 'createUser',
        'facts': 'facts',
        'file': 'file',
        'id': 'id',
        'line': 'line',
        'message': 'message',
        'update_user': 'updateUser'
    }

    def __init__(self, code_snip=None, create_time=None, create_user=None, facts=None, file=None, id=None, line=None, message=None, update_user=None, _configuration=None):  # noqa: E501
        """ApiIncident - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code_snip = None
        self._create_time = None
        self._create_user = None
        self._facts = None
        self._file = None
        self._id = None
        self._line = None
        self._message = None
        self._update_user = None
        self.discriminator = None

        if code_snip is not None:
            self.code_snip = code_snip
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if facts is not None:
            self.facts = facts
        if file is not None:
            self.file = file
        if id is not None:
            self.id = id
        if line is not None:
            self.line = line
        if message is not None:
            self.message = message
        if update_user is not None:
            self.update_user = update_user

    @property
    def code_snip(self):
        """Gets the code_snip of this ApiIncident.  # noqa: E501


        :return: The code_snip of this ApiIncident.  # noqa: E501
        :rtype: str
        """
        return self._code_snip

    @code_snip.setter
    def code_snip(self, code_snip):
        """Sets the code_snip of this ApiIncident.


        :param code_snip: The code_snip of this ApiIncident.  # noqa: E501
        :type: str
        """

        self._code_snip = code_snip

    @property
    def create_time(self):
        """Gets the create_time of this ApiIncident.  # noqa: E501


        :return: The create_time of this ApiIncident.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiIncident.


        :param create_time: The create_time of this ApiIncident.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this ApiIncident.  # noqa: E501


        :return: The create_user of this ApiIncident.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ApiIncident.


        :param create_user: The create_user of this ApiIncident.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def facts(self):
        """Gets the facts of this ApiIncident.  # noqa: E501


        :return: The facts of this ApiIncident.  # noqa: E501
        :rtype: ApiFactMap
        """
        return self._facts

    @facts.setter
    def facts(self, facts):
        """Sets the facts of this ApiIncident.


        :param facts: The facts of this ApiIncident.  # noqa: E501
        :type: ApiFactMap
        """

        self._facts = facts

    @property
    def file(self):
        """Gets the file of this ApiIncident.  # noqa: E501


        :return: The file of this ApiIncident.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ApiIncident.


        :param file: The file of this ApiIncident.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def id(self):
        """Gets the id of this ApiIncident.  # noqa: E501


        :return: The id of this ApiIncident.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiIncident.


        :param id: The id of this ApiIncident.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def line(self):
        """Gets the line of this ApiIncident.  # noqa: E501


        :return: The line of this ApiIncident.  # noqa: E501
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this ApiIncident.


        :param line: The line of this ApiIncident.  # noqa: E501
        :type: int
        """

        self._line = line

    @property
    def message(self):
        """Gets the message of this ApiIncident.  # noqa: E501


        :return: The message of this ApiIncident.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ApiIncident.


        :param message: The message of this ApiIncident.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def update_user(self):
        """Gets the update_user of this ApiIncident.  # noqa: E501


        :return: The update_user of this ApiIncident.  # noqa: E501
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this ApiIncident.


        :param update_user: The update_user of this ApiIncident.  # noqa: E501
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
        if issubclass(ApiIncident, dict):
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
        if not isinstance(other, ApiIncident):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiIncident):
            return True

        return self.to_dict() != other.to_dict()
