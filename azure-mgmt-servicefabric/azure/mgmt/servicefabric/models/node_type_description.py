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


class NodeTypeDescription(Model):
    """Describes a node type in the cluster, each node type represents sub set of
    nodes in the cluster.

    :param name: The name of the node type.
    :type name: str
    :param placement_properties: The placement tags applied to nodes in the
     node type, which can be used to indicate where certain services (workload)
     should run.
    :type placement_properties: dict[str, str]
    :param capacities: The capacity tags applied to the nodes in the node
     type, the cluster resource manager uses these tags to understand how much
     resource a node has.
    :type capacities: dict[str, str]
    :param client_connection_endpoint_port: The TCP cluster management
     endpoint port.
    :type client_connection_endpoint_port: int
    :param http_gateway_endpoint_port: The HTTP cluster management endpoint
     port.
    :type http_gateway_endpoint_port: int
    :param durability_level: The durability level of the node type. Learn
     about
     [DurabilityLevel](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-cluster-capacity).
     - Bronze - No privileges. This is the default.
     - Silver - The infrastructure jobs can be paused for a duration of 10
     minutes per UD.
     - Gold - The infrastructure jobs can be paused for a duration of 2 hours
     per UD. Gold durability can be enabled only on full node VM skus like
     D15_V2, G5 etc.
     . Possible values include: 'Bronze', 'Silver', 'Gold'
    :type durability_level: str or ~azure.mgmt.servicefabric.models.enum
    :param application_ports: The range of ports from which cluster assigned
     port to Service Fabric applications.
    :type application_ports:
     ~azure.mgmt.servicefabric.models.EndpointRangeDescription
    :param ephemeral_ports: The range of empheral ports that nodes in this
     node type should be configured with.
    :type ephemeral_ports:
     ~azure.mgmt.servicefabric.models.EndpointRangeDescription
    :param is_primary: The node type on which system services will run. Only
     one node type should be marked as primary. Primary node type cannot be
     deleted or changed for existing clusters.
    :type is_primary: bool
    :param vm_instance_count: The number of nodes in the node type. This count
     should match the capacity property in the corresponding
     VirtualMachineScaleSet resource.
    :type vm_instance_count: int
    :param reverse_proxy_endpoint_port: The endpoint used by reverse proxy.
    :type reverse_proxy_endpoint_port: int
    """

    _validation = {
        'name': {'required': True},
        'client_connection_endpoint_port': {'required': True},
        'http_gateway_endpoint_port': {'required': True},
        'is_primary': {'required': True},
        'vm_instance_count': {'required': True, 'maximum': 2147483647, 'minimum': 1},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'placement_properties': {'key': 'placementProperties', 'type': '{str}'},
        'capacities': {'key': 'capacities', 'type': '{str}'},
        'client_connection_endpoint_port': {'key': 'clientConnectionEndpointPort', 'type': 'int'},
        'http_gateway_endpoint_port': {'key': 'httpGatewayEndpointPort', 'type': 'int'},
        'durability_level': {'key': 'durabilityLevel', 'type': 'str'},
        'application_ports': {'key': 'applicationPorts', 'type': 'EndpointRangeDescription'},
        'ephemeral_ports': {'key': 'ephemeralPorts', 'type': 'EndpointRangeDescription'},
        'is_primary': {'key': 'isPrimary', 'type': 'bool'},
        'vm_instance_count': {'key': 'vmInstanceCount', 'type': 'int'},
        'reverse_proxy_endpoint_port': {'key': 'reverseProxyEndpointPort', 'type': 'int'},
    }

    def __init__(self, name, client_connection_endpoint_port, http_gateway_endpoint_port, is_primary, vm_instance_count, placement_properties=None, capacities=None, durability_level=None, application_ports=None, ephemeral_ports=None, reverse_proxy_endpoint_port=None):
        super(NodeTypeDescription, self).__init__()
        self.name = name
        self.placement_properties = placement_properties
        self.capacities = capacities
        self.client_connection_endpoint_port = client_connection_endpoint_port
        self.http_gateway_endpoint_port = http_gateway_endpoint_port
        self.durability_level = durability_level
        self.application_ports = application_ports
        self.ephemeral_ports = ephemeral_ports
        self.is_primary = is_primary
        self.vm_instance_count = vm_instance_count
        self.reverse_proxy_endpoint_port = reverse_proxy_endpoint_port
