# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QueryBody(Model):
    """The Analytics query. Learn more about the [Analytics query
    syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/).

    All required parameters must be populated in order to send to Azure.

    :param query: Required. The query to execute.
    :type query: str
    :param timespan: Optional. The timespan over which to query data. This is
     an ISO8601 time period value.  This timespan is applied in addition to any
     that are specified in the query expression.
    :type timespan: str
    :param workspaces: A list of workspaces that are included in the query.
    :type workspaces: list[str]
    """

    _validation = {
        'query': {'required': True},
    }

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'timespan': {'key': 'timespan', 'type': 'str'},
        'workspaces': {'key': 'workspaces', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(QueryBody, self).__init__(**kwargs)
        self.query = kwargs.get('query', None)
        self.timespan = kwargs.get('timespan', None)
        self.workspaces = kwargs.get('workspaces', None)
