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
import pytest
import time


BIGIP_11_6_VERSION = '11.6.0'

# At the very minimum, these should be created
EXPECTED_IFC_NAMES = ['1.1', '1.2', '1.3', 'mgmt']
EXPECTED_SELFIP_NAMES = [u'selfip.HA', u'selfip.data1', u'selfip.data2']
EXPECTED_VLAN_NAMES = [u'vlan.HA', u'data1', u'data2']


def get_floating_ip_output(hc, stack):
    max_attempts = 10
    interval = 5
    for attempt in range(max_attempts):
        floating_ips = []
        updated_stack = hc.stacks.get(stack.id)
        for output in updated_stack.outputs:
            if 'floating_ip' in output['output_key']:
                floating_ips.append(output['output_value'])
        if len(floating_ips) != 2:
            time.sleep(interval)
            continue
    if len(floating_ips) != 2:
        msg = 'Stack outputs not found within test window.'
        raise Exception(msg)
    return floating_ips


def check_net_components(bigip, ifc_num):
    ifcs = bigip.tm.net.interfaces.get_collection()
    ifc_names = [ifc.name for ifc in ifcs]
    assert sorted(EXPECTED_IFC_NAMES) == sorted(ifc_names)
    selfips = bigip.tm.net.selfips.get_collection()
    selfip_names = [selfip.name for selfip in selfips]
    assert sorted(EXPECTED_SELFIP_NAMES) == sorted(selfip_names)
    vlans = bigip.tm.net.vlans.get_collection()
    vlan_names = [vlan.name for vlan in vlans]
    assert sorted(EXPECTED_VLAN_NAMES) == sorted(vlan_names)


@pytest.fixture
def CommonTemplateDir(SupportedDir):
    return os.path.join(
        os.path.join(
            SupportedDir, 've', 'resource_group'
        )
    )


# These tests require a patched VE instance in your stack

def test_f5_two_ve_resource_group(
        HeatStack, symbols, CommonTemplateDir, WaitForLicensedBigIP
):
    hc, stack = HeatStack(
        os.path.join(CommonTemplateDir, 'f5_two_ve_resource_group.yaml'),
        'func_test_two_ve_resource_group',
        parameters={
            've_image': symbols.cluster_ready_ve_11_6_image,
            'external_network': symbols.external_network,
            'mgmt_network': symbols.mgmt_net,
            'ha_network': symbols.ha_net,
            'network_1': symbols.data1_net,
            'network_2': symbols.data2_net,
            'network_1_name': symbols.data1_name,
            'network_2_name': symbols.data2_name,
            'ssh_key': symbols.ssh_key,
            'admin_password': symbols.bigip_admin_password,
            'root_password': symbols.bigip_root_password,
            'license': symbols.license,
            'data_secgroup': symbols.secgroup,
            'control_secgroup': symbols.secgroup,
            'mgmt_secgroup': symbols.secgroup,
            've_flavor': symbols.ve_flavor
        }
    )
    floating_ips = get_floating_ip_output(hc, stack)
    for bigip_ip in floating_ips:
        bigip = WaitForLicensedBigIP(
            bigip_ip, 'admin', symbols.bigip_admin_password,
            BIGIP_11_6_VERSION, 4
        )
        check_net_components(bigip, 4)
