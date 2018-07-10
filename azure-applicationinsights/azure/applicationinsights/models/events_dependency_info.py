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


class EventsDependencyInfo(Model):
    """The dependency info.

    :param target: The target of the dependency
    :type target: str
    :param data: The data of the dependency
    :type data: str
    :param success: Indicates if the dependency was successful
    :type success: str
    :param duration: The duration of the dependency
    :type duration: long
    :param performance_bucket: The performance bucket of the dependency
    :type performance_bucket: str
    :param result_code: The result code of the dependency
    :type result_code: str
    :param type: The type of the dependency
    :type type: str
    :param name: The name of the dependency
    :type name: str
    :param id: The ID of the dependency
    :type id: str
    """

    _attribute_map = {
        'target': {'key': 'target', 'type': 'str'},
        'data': {'key': 'data', 'type': 'str'},
        'success': {'key': 'success', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'long'},
        'performance_bucket': {'key': 'performanceBucket', 'type': 'str'},
        'result_code': {'key': 'resultCode', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EventsDependencyInfo, self).__init__(**kwargs)
        self.target = kwargs.get('target', None)
        self.data = kwargs.get('data', None)
        self.success = kwargs.get('success', None)
        self.duration = kwargs.get('duration', None)
        self.performance_bucket = kwargs.get('performance_bucket', None)
        self.result_code = kwargs.get('result_code', None)
        self.type = kwargs.get('type', None)
        self.name = kwargs.get('name', None)
        self.id = kwargs.get('id', None)
