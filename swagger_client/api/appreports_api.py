# coding: utf-8

"""
    MTA 6.1 api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AppreportsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def analyses_report_applications_get(self, **kwargs):  # noqa: E501
        """List application reports.  # noqa: E501

        List application reports. filters: - id - name - description - businessService - effort - incidents - files - issue.id - issue.name - issue.ruleset - issue.rule - issue.category - issue.effort - issue.labels - application.id - application.name - businessService.name sort: - id - name - description - businessService - effort - incidents - files  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.analyses_report_applications_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ApiAppReport]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.analyses_report_applications_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.analyses_report_applications_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def analyses_report_applications_get_with_http_info(self, **kwargs):  # noqa: E501
        """List application reports.  # noqa: E501

        List application reports. filters: - id - name - description - businessService - effort - incidents - files - issue.id - issue.name - issue.ruleset - issue.rule - issue.category - issue.effort - issue.labels - application.id - application.name - businessService.name sort: - id - name - description - businessService - effort - incidents - files  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.analyses_report_applications_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ApiAppReport]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method analyses_report_applications_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/analyses/report/applications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ApiAppReport]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
