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


class MigrationReportResult(Model):
    """Migration validation report result, contains the url for downloading the
    generated report.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Migration validation result identifier
    :vartype id: str
    :ivar report_url: The url of the report.
    :vartype report_url: str
    """

    _validation = {
        'id': {'readonly': True},
        'report_url': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'report_url': {'key': 'reportUrl', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MigrationReportResult, self).__init__(**kwargs)
        self.id = None
        self.report_url = None