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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.autoscale_settings_operations import AutoscaleSettingsOperations
from .operations.operations import Operations
from .operations.alert_rule_incidents_operations import AlertRuleIncidentsOperations
from .operations.alert_rules_operations import AlertRulesOperations
from .operations.log_profiles_operations import LogProfilesOperations
from .operations.diagnostic_settings_operations import DiagnosticSettingsOperations
from .operations.diagnostic_settings_category_operations import DiagnosticSettingsCategoryOperations
from .operations.action_groups_operations import ActionGroupsOperations
from .operations.activity_log_alerts_operations import ActivityLogAlertsOperations
from .operations.activity_logs_operations import ActivityLogsOperations
from .operations.event_categories_operations import EventCategoriesOperations
from .operations.tenant_activity_logs_operations import TenantActivityLogsOperations
from .operations.metric_definitions_operations import MetricDefinitionsOperations
from .operations.metrics_operations import MetricsOperations
from .operations.metric_baseline_operations import MetricBaselineOperations
from .operations.metric_alerts_operations import MetricAlertsOperations
from .operations.metric_alerts_status_operations import MetricAlertsStatusOperations
from .operations.scheduled_query_rules_operations import ScheduledQueryRulesOperations
from . import models


class MonitorManagementClientConfiguration(AzureConfiguration):
    """Configuration for MonitorManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(MonitorManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-monitor/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class MonitorManagementClient(SDKClient):
    """Monitor Management Client

    :ivar config: Configuration for client.
    :vartype config: MonitorManagementClientConfiguration

    :ivar autoscale_settings: AutoscaleSettings operations
    :vartype autoscale_settings: azure.mgmt.monitor.operations.AutoscaleSettingsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.monitor.operations.Operations
    :ivar alert_rule_incidents: AlertRuleIncidents operations
    :vartype alert_rule_incidents: azure.mgmt.monitor.operations.AlertRuleIncidentsOperations
    :ivar alert_rules: AlertRules operations
    :vartype alert_rules: azure.mgmt.monitor.operations.AlertRulesOperations
    :ivar log_profiles: LogProfiles operations
    :vartype log_profiles: azure.mgmt.monitor.operations.LogProfilesOperations
    :ivar diagnostic_settings: DiagnosticSettings operations
    :vartype diagnostic_settings: azure.mgmt.monitor.operations.DiagnosticSettingsOperations
    :ivar diagnostic_settings_category: DiagnosticSettingsCategory operations
    :vartype diagnostic_settings_category: azure.mgmt.monitor.operations.DiagnosticSettingsCategoryOperations
    :ivar action_groups: ActionGroups operations
    :vartype action_groups: azure.mgmt.monitor.operations.ActionGroupsOperations
    :ivar activity_log_alerts: ActivityLogAlerts operations
    :vartype activity_log_alerts: azure.mgmt.monitor.operations.ActivityLogAlertsOperations
    :ivar activity_logs: ActivityLogs operations
    :vartype activity_logs: azure.mgmt.monitor.operations.ActivityLogsOperations
    :ivar event_categories: EventCategories operations
    :vartype event_categories: azure.mgmt.monitor.operations.EventCategoriesOperations
    :ivar tenant_activity_logs: TenantActivityLogs operations
    :vartype tenant_activity_logs: azure.mgmt.monitor.operations.TenantActivityLogsOperations
    :ivar metric_definitions: MetricDefinitions operations
    :vartype metric_definitions: azure.mgmt.monitor.operations.MetricDefinitionsOperations
    :ivar metrics: Metrics operations
    :vartype metrics: azure.mgmt.monitor.operations.MetricsOperations
    :ivar metric_baseline: MetricBaseline operations
    :vartype metric_baseline: azure.mgmt.monitor.operations.MetricBaselineOperations
    :ivar metric_alerts: MetricAlerts operations
    :vartype metric_alerts: azure.mgmt.monitor.operations.MetricAlertsOperations
    :ivar metric_alerts_status: MetricAlertsStatus operations
    :vartype metric_alerts_status: azure.mgmt.monitor.operations.MetricAlertsStatusOperations
    :ivar scheduled_query_rules: ScheduledQueryRules operations
    :vartype scheduled_query_rules: azure.mgmt.monitor.operations.ScheduledQueryRulesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = MonitorManagementClientConfiguration(credentials, subscription_id, base_url)
        super(MonitorManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.autoscale_settings = AutoscaleSettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.alert_rule_incidents = AlertRuleIncidentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.alert_rules = AlertRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.log_profiles = LogProfilesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.diagnostic_settings = DiagnosticSettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.diagnostic_settings_category = DiagnosticSettingsCategoryOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.action_groups = ActionGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.activity_log_alerts = ActivityLogAlertsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.activity_logs = ActivityLogsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.event_categories = EventCategoriesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tenant_activity_logs = TenantActivityLogsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.metric_definitions = MetricDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.metrics = MetricsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.metric_baseline = MetricBaselineOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.metric_alerts = MetricAlertsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.metric_alerts_status = MetricAlertsStatusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.scheduled_query_rules = ScheduledQueryRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
