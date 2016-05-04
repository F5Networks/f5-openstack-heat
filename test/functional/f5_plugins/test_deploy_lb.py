# Copyright 2015-2016 F5 Networks Inc.
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
import pytest


@pytest.fixture
def F5PluginTemplateLoc(SupportedDir):
    return os.path.join(
        os.path.join(SupportedDir, 'f5_plugins', 'deploy_lb.yaml')
    )


def test_deploy_lb(
        HeatStack,
        symbols,
        F5PluginTemplateLoc
):
    hc, stack = HeatStack(
        F5PluginTemplateLoc,
        'func_test_deploy_lb',
        parameters={
            'client_server_image': 'ubuntu_14.04_lts',
            'client_server_flavor': 'm1.small',
            'key_name': 'testlab',
            'client_network': 'data1_net',
            'server_network': 'data2_net',
            'bigip_pw': symbols.bigip_admin_password,
            'bigip_fip': symbols.bigip_fip,
            'vs_vip': symbols.vs_vip
        }
    )
