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


class DataSourceFilter(Model):
    """DataSource filter. Right now, only filter by kind is supported.

    :param kind: Possible values include: 'AzureActivityLog',
     'ChangeTrackingPath', 'ChangeTrackingDefaultPath',
     'ChangeTrackingDefaultRegistry', 'ChangeTrackingCustomRegistry',
     'CustomLog', 'CustomLogCollection', 'GenericDataSource', 'IISLogs',
     'LinuxPerformanceObject', 'LinuxPerformanceCollection', 'LinuxSyslog',
     'LinuxSyslogCollection', 'WindowsEvent', 'WindowsPerformanceCounter'
    :type kind: str or :class:`DataSourceKind
     <azure.mgmt.loganalytics.models.DataSourceKind>`
    """

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, kind=None):
        self.kind = kind