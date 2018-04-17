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


class CaffeSettings(Model):
    """Specifies the settings for Caffe job.

    :param config_file_path: Specifies the path of the config file. This
     property cannot be specified if pythonScriptFilePath is specified.
    :type config_file_path: str
    :param python_script_file_path: The path and file name of the python
     script to execute the job. This property cannot be specified if
     configFilePath is specified.
    :type python_script_file_path: str
    :param python_interpreter_path: The path to python interpreter. This
     property can be specified only if the pythonScriptFilePath is specified.
    :type python_interpreter_path: str
    :param command_line_args: Command line arguments that needs to be passed
     to the Caffe job.
    :type command_line_args: str
    :param process_count: Number of processes parameter that is passed to MPI
     runtime. The default value for this property is equal to nodeCount
     property
    :type process_count: int
    """

    _attribute_map = {
        'config_file_path': {'key': 'configFilePath', 'type': 'str'},
        'python_script_file_path': {'key': 'pythonScriptFilePath', 'type': 'str'},
        'python_interpreter_path': {'key': 'pythonInterpreterPath', 'type': 'str'},
        'command_line_args': {'key': 'commandLineArgs', 'type': 'str'},
        'process_count': {'key': 'processCount', 'type': 'int'},
    }

    def __init__(self, *, config_file_path: str=None, python_script_file_path: str=None, python_interpreter_path: str=None, command_line_args: str=None, process_count: int=None, **kwargs) -> None:
        super(CaffeSettings, self).__init__(**kwargs)
        self.config_file_path = config_file_path
        self.python_script_file_path = python_script_file_path
        self.python_interpreter_path = python_interpreter_path
        self.command_line_args = command_line_args
        self.process_count = process_count