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

from f5.bigip import ManagementRoot
from f5.multi_device.cluster import ClusterManager

import os
import pytest


@pytest.fixture
def F5PluginTemplateLoc(SupportedDir):
    return os.path.join(
        os.path.join(SupportedDir, 'f5_plugins', 'active_standby.yaml')
    )


def test_active_standby(HeatStack, symbols, F5PluginTemplateLoc):
    hc, stack = HeatStack(
        F5PluginTemplateLoc,
        'func_test_deploy_lb',
        parameters={
            'bigip1_ip': symbols.bigip1_ip,
            'bigip2_ip': symbols.bigip2_ip,
            'bigip1_un': symbols.bigip1_un,
            'bigip2_un': symbols.bigip2_un,
            'bigip1_pw': symbols.bigip1_un,
            'bigip2_pw': symbols.bigip2_un,
            'cluster_name': symbols.cluster_name
        }
    )
    a = ManagementRoot(symbols.bigip1_ip, symbols.bigip1_un, symbols.bigip1_pw)
    b = ManagementRoot(symbols.bigip2_ip, symbols.bigip2_un, symbols.bigip2_pw)

    cm = ClusterManager(
        devices=[a, b],
        device_group_name=symbols.cluster_name,
        device_group_type='sync-failover',
        device_group_partition='Common'
    )
    expected_ips = [symbols.bigip1_ip, symbols.bigip2_ip]
    for device in cm.cluster.devices:
        assert device._meta_data['hostname'] in expected_ips
        expected_ips.remove(device._meta_data['hostname'])
    assert cm.cluster.device_group_name == symbols.cluster_name
    assert cm.cluster.device_group_partition == 'Common'
    assert cm.cluster.device_group_type == 'sync-failover'
    sync_status_entry = 'https://localhost/mgmt/tm/cm/sync-status/0'
    sync_status_a = a.tm.cm.sync_status
    sync_status_b = b.tm.cm.sync_status
    sync_status_a.refresh()
    sync_status_b.refresh()
    current_status_a = (sync_status_a.entries[sync_status_entry]
                        ['nestedStats']['entries']['status']['description'])
    assert current_status_a == 'In Sync'
    current_status_b = (sync_status_b.entries[sync_status_entry]
                        ['nestedStats']['entries']['status']['description'])
    assert current_status_b == 'In Sync'
