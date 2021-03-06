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


class UploadChunkRange(Model):
    """Information about which portion of the file to upload.

    :param start_position: The start position of the portion of the file. It's
     represented by the number of bytes.
    :type start_position: str
    :param end_position: The end position of the portion of the file. It's
     represented by the number of bytes.
    :type end_position: str
    """

    _attribute_map = {
        'start_position': {'key': 'StartPosition', 'type': 'str'},
        'end_position': {'key': 'EndPosition', 'type': 'str'},
    }

    def __init__(self, *, start_position: str=None, end_position: str=None, **kwargs) -> None:
        super(UploadChunkRange, self).__init__(**kwargs)
        self.start_position = start_position
        self.end_position = end_position
