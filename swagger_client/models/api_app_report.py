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


class ApiAppReport(object):
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
        'business_service': 'str',
        'description': 'str',
        'effort': 'int',
        'files': 'int',
        'id': 'int',
        'incidents': 'int',
        'issue': 'ApiAppReportIssue',
        'name': 'str'
    }

    attribute_map = {
        'business_service': 'businessService',
        'description': 'description',
        'effort': 'effort',
        'files': 'files',
        'id': 'id',
        'incidents': 'incidents',
        'issue': 'issue',
        'name': 'name'
    }

    def __init__(self, business_service=None, description=None, effort=None, files=None, id=None, incidents=None, issue=None, name=None, _configuration=None):  # noqa: E501
        """ApiAppReport - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._business_service = None
        self._description = None
        self._effort = None
        self._files = None
        self._id = None
        self._incidents = None
        self._issue = None
        self._name = None
        self.discriminator = None

        if business_service is not None:
            self.business_service = business_service
        if description is not None:
            self.description = description
        if effort is not None:
            self.effort = effort
        if files is not None:
            self.files = files
        if id is not None:
            self.id = id
        if incidents is not None:
            self.incidents = incidents
        if issue is not None:
            self.issue = issue
        if name is not None:
            self.name = name

    @property
    def business_service(self):
        """Gets the business_service of this ApiAppReport.  # noqa: E501


        :return: The business_service of this ApiAppReport.  # noqa: E501
        :rtype: str
        """
        return self._business_service

    @business_service.setter
    def business_service(self, business_service):
        """Sets the business_service of this ApiAppReport.


        :param business_service: The business_service of this ApiAppReport.  # noqa: E501
        :type: str
        """

        self._business_service = business_service

    @property
    def description(self):
        """Gets the description of this ApiAppReport.  # noqa: E501


        :return: The description of this ApiAppReport.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiAppReport.


        :param description: The description of this ApiAppReport.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def effort(self):
        """Gets the effort of this ApiAppReport.  # noqa: E501


        :return: The effort of this ApiAppReport.  # noqa: E501
        :rtype: int
        """
        return self._effort

    @effort.setter
    def effort(self, effort):
        """Sets the effort of this ApiAppReport.


        :param effort: The effort of this ApiAppReport.  # noqa: E501
        :type: int
        """

        self._effort = effort

    @property
    def files(self):
        """Gets the files of this ApiAppReport.  # noqa: E501


        :return: The files of this ApiAppReport.  # noqa: E501
        :rtype: int
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ApiAppReport.


        :param files: The files of this ApiAppReport.  # noqa: E501
        :type: int
        """

        self._files = files

    @property
    def id(self):
        """Gets the id of this ApiAppReport.  # noqa: E501


        :return: The id of this ApiAppReport.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiAppReport.


        :param id: The id of this ApiAppReport.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def incidents(self):
        """Gets the incidents of this ApiAppReport.  # noqa: E501


        :return: The incidents of this ApiAppReport.  # noqa: E501
        :rtype: int
        """
        return self._incidents

    @incidents.setter
    def incidents(self, incidents):
        """Sets the incidents of this ApiAppReport.


        :param incidents: The incidents of this ApiAppReport.  # noqa: E501
        :type: int
        """

        self._incidents = incidents

    @property
    def issue(self):
        """Gets the issue of this ApiAppReport.  # noqa: E501


        :return: The issue of this ApiAppReport.  # noqa: E501
        :rtype: ApiAppReportIssue
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """Sets the issue of this ApiAppReport.


        :param issue: The issue of this ApiAppReport.  # noqa: E501
        :type: ApiAppReportIssue
        """

        self._issue = issue

    @property
    def name(self):
        """Gets the name of this ApiAppReport.  # noqa: E501


        :return: The name of this ApiAppReport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiAppReport.


        :param name: The name of this ApiAppReport.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(ApiAppReport, dict):
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
        if not isinstance(other, ApiAppReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiAppReport):
            return True

        return self.to_dict() != other.to_dict()
