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


class ApiTaskReport(object):
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
        'activity': 'list[str]',
        'completed': 'int',
        'create_time': 'str',
        'create_user': 'str',
        'error': 'str',
        'id': 'int',
        'result': 'object',
        'status': 'str',
        'task': 'int',
        'total': 'int',
        'update_user': 'str'
    }

    attribute_map = {
        'activity': 'activity',
        'completed': 'completed',
        'create_time': 'createTime',
        'create_user': 'createUser',
        'error': 'error',
        'id': 'id',
        'result': 'result',
        'status': 'status',
        'task': 'task',
        'total': 'total',
        'update_user': 'updateUser'
    }

    def __init__(self, activity=None, completed=None, create_time=None, create_user=None, error=None, id=None, result=None, status=None, task=None, total=None, update_user=None, _configuration=None):  # noqa: E501
        """ApiTaskReport - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._activity = None
        self._completed = None
        self._create_time = None
        self._create_user = None
        self._error = None
        self._id = None
        self._result = None
        self._status = None
        self._task = None
        self._total = None
        self._update_user = None
        self.discriminator = None

        if activity is not None:
            self.activity = activity
        if completed is not None:
            self.completed = completed
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if result is not None:
            self.result = result
        if status is not None:
            self.status = status
        if task is not None:
            self.task = task
        if total is not None:
            self.total = total
        if update_user is not None:
            self.update_user = update_user

    @property
    def activity(self):
        """Gets the activity of this ApiTaskReport.  # noqa: E501


        :return: The activity of this ApiTaskReport.  # noqa: E501
        :rtype: list[str]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this ApiTaskReport.


        :param activity: The activity of this ApiTaskReport.  # noqa: E501
        :type: list[str]
        """

        self._activity = activity

    @property
    def completed(self):
        """Gets the completed of this ApiTaskReport.  # noqa: E501


        :return: The completed of this ApiTaskReport.  # noqa: E501
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this ApiTaskReport.


        :param completed: The completed of this ApiTaskReport.  # noqa: E501
        :type: int
        """

        self._completed = completed

    @property
    def create_time(self):
        """Gets the create_time of this ApiTaskReport.  # noqa: E501


        :return: The create_time of this ApiTaskReport.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiTaskReport.


        :param create_time: The create_time of this ApiTaskReport.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this ApiTaskReport.  # noqa: E501


        :return: The create_user of this ApiTaskReport.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ApiTaskReport.


        :param create_user: The create_user of this ApiTaskReport.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def error(self):
        """Gets the error of this ApiTaskReport.  # noqa: E501


        :return: The error of this ApiTaskReport.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ApiTaskReport.


        :param error: The error of this ApiTaskReport.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def id(self):
        """Gets the id of this ApiTaskReport.  # noqa: E501


        :return: The id of this ApiTaskReport.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiTaskReport.


        :param id: The id of this ApiTaskReport.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def result(self):
        """Gets the result of this ApiTaskReport.  # noqa: E501


        :return: The result of this ApiTaskReport.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ApiTaskReport.


        :param result: The result of this ApiTaskReport.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def status(self):
        """Gets the status of this ApiTaskReport.  # noqa: E501


        :return: The status of this ApiTaskReport.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiTaskReport.


        :param status: The status of this ApiTaskReport.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def task(self):
        """Gets the task of this ApiTaskReport.  # noqa: E501


        :return: The task of this ApiTaskReport.  # noqa: E501
        :rtype: int
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this ApiTaskReport.


        :param task: The task of this ApiTaskReport.  # noqa: E501
        :type: int
        """

        self._task = task

    @property
    def total(self):
        """Gets the total of this ApiTaskReport.  # noqa: E501


        :return: The total of this ApiTaskReport.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ApiTaskReport.


        :param total: The total of this ApiTaskReport.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def update_user(self):
        """Gets the update_user of this ApiTaskReport.  # noqa: E501


        :return: The update_user of this ApiTaskReport.  # noqa: E501
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this ApiTaskReport.


        :param update_user: The update_user of this ApiTaskReport.  # noqa: E501
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
        if issubclass(ApiTaskReport, dict):
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
        if not isinstance(other, ApiTaskReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiTaskReport):
            return True

        return self.to_dict() != other.to_dict()
