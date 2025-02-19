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


class ApiImportSummary(object):
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
        'create_entities': 'bool',
        'create_time': 'str',
        'create_user': 'str',
        'filename': 'str',
        'id': 'int',
        'import_status': 'str',
        'import_time': 'str',
        'invalid_count': 'int',
        'update_user': 'str',
        'valid_count': 'int'
    }

    attribute_map = {
        'create_entities': 'createEntities',
        'create_time': 'createTime',
        'create_user': 'createUser',
        'filename': 'filename',
        'id': 'id',
        'import_status': 'importStatus',
        'import_time': 'importTime',
        'invalid_count': 'invalidCount',
        'update_user': 'updateUser',
        'valid_count': 'validCount'
    }

    def __init__(self, create_entities=None, create_time=None, create_user=None, filename=None, id=None, import_status=None, import_time=None, invalid_count=None, update_user=None, valid_count=None, _configuration=None):  # noqa: E501
        """ApiImportSummary - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_entities = None
        self._create_time = None
        self._create_user = None
        self._filename = None
        self._id = None
        self._import_status = None
        self._import_time = None
        self._invalid_count = None
        self._update_user = None
        self._valid_count = None
        self.discriminator = None

        if create_entities is not None:
            self.create_entities = create_entities
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if filename is not None:
            self.filename = filename
        if id is not None:
            self.id = id
        if import_status is not None:
            self.import_status = import_status
        if import_time is not None:
            self.import_time = import_time
        if invalid_count is not None:
            self.invalid_count = invalid_count
        if update_user is not None:
            self.update_user = update_user
        if valid_count is not None:
            self.valid_count = valid_count

    @property
    def create_entities(self):
        """Gets the create_entities of this ApiImportSummary.  # noqa: E501


        :return: The create_entities of this ApiImportSummary.  # noqa: E501
        :rtype: bool
        """
        return self._create_entities

    @create_entities.setter
    def create_entities(self, create_entities):
        """Sets the create_entities of this ApiImportSummary.


        :param create_entities: The create_entities of this ApiImportSummary.  # noqa: E501
        :type: bool
        """

        self._create_entities = create_entities

    @property
    def create_time(self):
        """Gets the create_time of this ApiImportSummary.  # noqa: E501


        :return: The create_time of this ApiImportSummary.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiImportSummary.


        :param create_time: The create_time of this ApiImportSummary.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this ApiImportSummary.  # noqa: E501


        :return: The create_user of this ApiImportSummary.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ApiImportSummary.


        :param create_user: The create_user of this ApiImportSummary.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def filename(self):
        """Gets the filename of this ApiImportSummary.  # noqa: E501


        :return: The filename of this ApiImportSummary.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this ApiImportSummary.


        :param filename: The filename of this ApiImportSummary.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def id(self):
        """Gets the id of this ApiImportSummary.  # noqa: E501


        :return: The id of this ApiImportSummary.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiImportSummary.


        :param id: The id of this ApiImportSummary.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def import_status(self):
        """Gets the import_status of this ApiImportSummary.  # noqa: E501


        :return: The import_status of this ApiImportSummary.  # noqa: E501
        :rtype: str
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status):
        """Sets the import_status of this ApiImportSummary.


        :param import_status: The import_status of this ApiImportSummary.  # noqa: E501
        :type: str
        """

        self._import_status = import_status

    @property
    def import_time(self):
        """Gets the import_time of this ApiImportSummary.  # noqa: E501


        :return: The import_time of this ApiImportSummary.  # noqa: E501
        :rtype: str
        """
        return self._import_time

    @import_time.setter
    def import_time(self, import_time):
        """Sets the import_time of this ApiImportSummary.


        :param import_time: The import_time of this ApiImportSummary.  # noqa: E501
        :type: str
        """

        self._import_time = import_time

    @property
    def invalid_count(self):
        """Gets the invalid_count of this ApiImportSummary.  # noqa: E501


        :return: The invalid_count of this ApiImportSummary.  # noqa: E501
        :rtype: int
        """
        return self._invalid_count

    @invalid_count.setter
    def invalid_count(self, invalid_count):
        """Sets the invalid_count of this ApiImportSummary.


        :param invalid_count: The invalid_count of this ApiImportSummary.  # noqa: E501
        :type: int
        """

        self._invalid_count = invalid_count

    @property
    def update_user(self):
        """Gets the update_user of this ApiImportSummary.  # noqa: E501


        :return: The update_user of this ApiImportSummary.  # noqa: E501
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this ApiImportSummary.


        :param update_user: The update_user of this ApiImportSummary.  # noqa: E501
        :type: str
        """

        self._update_user = update_user

    @property
    def valid_count(self):
        """Gets the valid_count of this ApiImportSummary.  # noqa: E501


        :return: The valid_count of this ApiImportSummary.  # noqa: E501
        :rtype: int
        """
        return self._valid_count

    @valid_count.setter
    def valid_count(self, valid_count):
        """Sets the valid_count of this ApiImportSummary.


        :param valid_count: The valid_count of this ApiImportSummary.  # noqa: E501
        :type: int
        """

        self._valid_count = valid_count

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
        if issubclass(ApiImportSummary, dict):
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
        if not isinstance(other, ApiImportSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiImportSummary):
            return True

        return self.to_dict() != other.to_dict()
