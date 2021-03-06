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

from .rule_data_source import RuleDataSource


class RuleManagementEventDataSource(RuleDataSource):
    """A rule management event data source. The discriminator fields is always
    RuleManagementEventDataSource in this case.

    All required parameters must be populated in order to send to Azure.

    :param resource_uri: the resource identifier of the resource the rule
     monitors. **NOTE**: this property cannot be updated for an existing rule.
    :type resource_uri: str
    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param event_name: the event name.
    :type event_name: str
    :param event_source: the event source.
    :type event_source: str
    :param level: the level.
    :type level: str
    :param operation_name: The name of the operation that should be checked
     for. If no name is provided, any operation will match.
    :type operation_name: str
    :param resource_group_name: the resource group name.
    :type resource_group_name: str
    :param resource_provider_name: the resource provider name.
    :type resource_provider_name: str
    :param status: The status of the operation that should be checked for. If
     no status is provided, any status will match.
    :type status: str
    :param sub_status: the substatus.
    :type sub_status: str
    :param claims: the claims.
    :type claims:
     ~azure.mgmt.monitor.models.RuleManagementEventClaimsDataSource
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'resource_uri': {'key': 'resourceUri', 'type': 'str'},
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
        'event_name': {'key': 'eventName', 'type': 'str'},
        'event_source': {'key': 'eventSource', 'type': 'str'},
        'level': {'key': 'level', 'type': 'str'},
        'operation_name': {'key': 'operationName', 'type': 'str'},
        'resource_group_name': {'key': 'resourceGroupName', 'type': 'str'},
        'resource_provider_name': {'key': 'resourceProviderName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'sub_status': {'key': 'subStatus', 'type': 'str'},
        'claims': {'key': 'claims', 'type': 'RuleManagementEventClaimsDataSource'},
    }

    def __init__(self, **kwargs):
        super(RuleManagementEventDataSource, self).__init__(**kwargs)
        self.event_name = kwargs.get('event_name', None)
        self.event_source = kwargs.get('event_source', None)
        self.level = kwargs.get('level', None)
        self.operation_name = kwargs.get('operation_name', None)
        self.resource_group_name = kwargs.get('resource_group_name', None)
        self.resource_provider_name = kwargs.get('resource_provider_name', None)
        self.status = kwargs.get('status', None)
        self.sub_status = kwargs.get('sub_status', None)
        self.claims = kwargs.get('claims', None)
        self.odatatype = 'Microsoft.Azure.Management.Insights.Models.RuleManagementEventDataSource'
