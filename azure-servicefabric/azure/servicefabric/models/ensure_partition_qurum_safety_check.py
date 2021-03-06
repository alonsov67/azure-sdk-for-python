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

from .partition_safety_check import PartitionSafetyCheck


class EnsurePartitionQurumSafetyCheck(PartitionSafetyCheck):
    """Safety check that ensures that a quorum of replicas are not lost for a
    partition.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    :param partition_id: Id of the partition which is undergoing the safety
     check.
    :type partition_id: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'Kind', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EnsurePartitionQurumSafetyCheck, self).__init__(**kwargs)
        self.kind = 'EnsurePartitionQuorum'
