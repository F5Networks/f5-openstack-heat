# Copyright 2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

import os
import yaml
from yaml.error import YAMLError


def check_yaml(check_dir):
    '''Check yaml files in given dir to ensure they are parsable as yaml.'''

    for base, directory, files in os.walk(check_dir):
        for filename in files:
            if filename.endswith('.yaml'):
                yaml_path = os.path.join(base, filename)
                with open(yaml_path, 'r') as template:
                    template_string = template.read()
                    try:
                        yaml.load(template_string)
                    except YAMLError as ex:
                        msg = 'The HOT file at location: %r failed to parse ' \
                            'as YAML' % yaml_path
                        raise YAMLError('{0}\n{1}'.format(msg, ex))


def test_unsupported_files(UnsupportedDir):
    check_yaml(UnsupportedDir)


def test_f5_supported_files(SupportedDir):
    check_yaml(SupportedDir)
