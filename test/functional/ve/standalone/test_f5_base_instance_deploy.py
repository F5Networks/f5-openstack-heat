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

from f5.sdk_exception import F5SDKError

import os
import pytest


BIGIP_11_5_4_IMG = 'BIGIP-11.5.4.0.0.256'
BIGIP_11_5_4_VERSION = '11.5.4'
BIGIP_11_6_IMG = 'BIGIP-11.6.0.0.0.401'
BIGIP_11_6_VERSION = '11.6.0'
BIGIP_12_0_IMG = 'BIGIP-12.0.0.0.0.606'
BIGIP_12_0_VERSION = '12.0.0'

# At the very minimum, these should be created
EXPECTED_IFC_NAMES = ['1.1', 'mgmt']
EXPECTED_SELFIP_NAMES = [u'selfip.network-1.1']
EXPECTED_VLAN_NAMES = [u'network-1.1']


def get_floating_ip_output(stack):
    for output in stack.outputs:
        if 'floating_ip' == output['output_key']:
            return output['output_value']


def check_net_components(bigip, ifc_num):
    expected_ifc_names = EXPECTED_IFC_NAMES[:]
    expected_selfip_names = EXPECTED_SELFIP_NAMES[:]
    expected_vlan_names = EXPECTED_VLAN_NAMES[:]
    for ifc in range(2, ifc_num):
        expected_ifc_names.append('1.{}'.format(ifc))
        expected_selfip_names.append(u'selfip.network-1.{}'.format(ifc))
        expected_vlan_names.append(u'network-1.{}'.format(ifc))
    params = {}
    try:
        # Since 11.5.0 is not a default supported version in f5-sdk we must
        # handle it with requests_params and setting the version in query
        # args
        bigip.tm.net.interfaces.get_collection()
    except F5SDKError as ex:
        if '11.5.4' in ex.value.message:
            params = {'params': {'ver': ['11.5.0']}}
    ifcs = bigip.tm.net.interfaces.get_collection(requests_params=params)
    ifc_names = [ifc.name for ifc in ifcs]
    assert sorted(expected_ifc_names) == sorted(ifc_names)
    selfips = bigip.tm.net.selfips.get_collection(requests_params=params)
    selfip_names = [selfip.name for selfip in selfips]
    assert sorted(expected_selfip_names) == sorted(selfip_names)
    vlans = bigip.tm.net.vlans.get_collection(requests_params=params)
    vlan_names = [vlan.name for vlan in vlans]
    assert sorted(expected_vlan_names) == sorted(vlan_names)


@pytest.fixture
def CommonTemplateDir(SupportedDir):
    return os.path.join(
        os.path.join(
            SupportedDir, 've', 'standalone'
        )
    )


# These tests require a patched VE instance in your stack

def test_f5_base_instance_deploy_2_nic_11_5_4(
        HeatStack, symbols, CommonTemplateDir, WaitForLicensedBigIP
):
    hc, stack = HeatStack(
        os.path.join(CommonTemplateDir, 'f5_ve_standalone_2_nic.yaml'),
        'func_test_standalone_2_nic',
        parameters={
            've_image': BIGIP_11_5_4_IMG,
            'external_network': symbols.external_network,
            'mgmt_network': symbols.mgmt_net,
            've_flavor': symbols.ve_flavor,
            'network_1': symbols.data1_net,
            'f5_ve_os_ssh_key': symbols.ssh_key,
            'admin_password': symbols.bigip_admin_password,
            'root_password': symbols.bigip_root_password,
            'license': symbols.license
        }
    )
    updated_stack = hc.stacks.get(stack.id)
    floating_ip = get_floating_ip_output(updated_stack)
    bigip = WaitForLicensedBigIP(
        floating_ip, 'admin', symbols.bigip_admin_password,
        BIGIP_11_5_4_VERSION, 2
    )
    check_net_components(bigip, 2)


def test_f5_base_instance_deploy_2_nic_11_6(
        HeatStack, symbols, CommonTemplateDir, WaitForLicensedBigIP
):
    hc, stack = HeatStack(
        os.path.join(CommonTemplateDir, 'f5_ve_standalone_2_nic.yaml'),
        'func_test_standalone_2_nic',
        parameters={
            've_image': BIGIP_11_6_IMG,
            'external_network': symbols.external_network,
            'mgmt_network': symbols.mgmt_net,
            've_flavor': symbols.ve_flavor,
            'network_1': symbols.data1_net,
            'f5_ve_os_ssh_key': symbols.ssh_key,
            'admin_password': symbols.bigip_admin_password,
            'root_password': symbols.bigip_root_password,
            'license': symbols.license
        }
    )
    updated_stack = hc.stacks.get(stack.id)
    floating_ip = get_floating_ip_output(updated_stack)
    bigip = WaitForLicensedBigIP(
        floating_ip, 'admin', symbols.bigip_admin_password,
        BIGIP_11_6_VERSION, 2
    )
    check_net_components(bigip, 2)


def test_f5_base_instance_deploy_2_nic_12_0(
        HeatStack, symbols, CommonTemplateDir, WaitForLicensedBigIP
):
    hc, stack = HeatStack(
        os.path.join(CommonTemplateDir, 'f5_ve_standalone_2_nic.yaml'),
        'func_test_standalone_2_nic',
        parameters={
            've_image': BIGIP_12_0_IMG,
            'external_network': symbols.external_network,
            'mgmt_network': symbols.mgmt_net,
            've_flavor': symbols.ve_flavor,
            'network_1': symbols.data1_net,
            'f5_ve_os_ssh_key': symbols.ssh_key,
            'admin_password': symbols.bigip_admin_password,
            'root_password': symbols.bigip_root_password,
            'license': symbols.license
        }
    )
    updated_stack = hc.stacks.get(stack.id)
    floating_ip = get_floating_ip_output(updated_stack)
    bigip = WaitForLicensedBigIP(
        floating_ip, 'admin', symbols.bigip_admin_password,
        BIGIP_12_0_VERSION, 2
    )
    check_net_components(bigip, 2)


def test_f5_base_instance_deploy_3_nic_11_5_4(
        HeatStack, symbols, CommonTemplateDir, WaitForLicensedBigIP
):
    hc, stack = HeatStack(
        os.path.join(CommonTemplateDir, 'f5_ve_standalone_3_nic.yaml'),
        'func_test_standalone_3_nic',
        parameters={
            've_image': BIGIP_11_5_4_IMG,
            've_flavor': symbols.ve_flavor,
            'external_network': symbols.external_network,
            'mgmt_network': symbols.mgmt_net,
            'network_1': symbols.data1_net,
            'network_2': symbols.data2_net,
            'f5_ve_os_ssh_key': symbols.ssh_key,
            'admin_password': symbols.bigip_admin_password,
            'root_password': symbols.bigip_root_password,
            'license': symbols.license
        }
    )
    updated_stack = hc.stacks.get(stack.id)
    floating_ip = get_floating_ip_output(updated_stack)
    bigip = WaitForLicensedBigIP(
        floating_ip, 'admin', symbols.bigip_admin_password,
        BIGIP_11_5_4_VERSION, 3
    )
    check_net_components(bigip, 3)


def test_f5_base_instance_deploy_3_nic_11_6(
        HeatStack, symbols, CommonTemplateDir, WaitForLicensedBigIP
):
    hc, stack = HeatStack(
        os.path.join(CommonTemplateDir, 'f5_ve_standalone_3_nic.yaml'),
        'func_test_standalone_3_nic',
        parameters={
            've_image': BIGIP_11_6_IMG,
            've_flavor': symbols.ve_flavor,
            'external_network': symbols.external_network,
            'mgmt_network': symbols.mgmt_net,
            'network_1': symbols.data1_net,
            'network_2': symbols.data2_net,
            'f5_ve_os_ssh_key': symbols.ssh_key,
            'admin_password': symbols.bigip_admin_password,
            'root_password': symbols.bigip_root_password,
            'license': symbols.license
        }
    )
    updated_stack = hc.stacks.get(stack.id)
    floating_ip = get_floating_ip_output(updated_stack)
    bigip = WaitForLicensedBigIP(
        floating_ip, 'admin', symbols.bigip_admin_password,
        BIGIP_11_6_VERSION, 3
    )
    check_net_components(bigip, 3)


def test_f5_base_instance_deploy_3_nic_12_0(
        HeatStack, symbols, CommonTemplateDir, WaitForLicensedBigIP
):
    hc, stack = HeatStack(
        os.path.join(CommonTemplateDir, 'f5_ve_standalone_3_nic.yaml'),
        'func_test_standalone_3_nic',
        parameters={
            've_image': BIGIP_12_0_IMG,
            've_flavor': symbols.ve_flavor,
            'external_network': symbols.external_network,
            'mgmt_network': symbols.mgmt_net,
            'network_1': symbols.data1_net,
            'network_2': symbols.data2_net,
            'f5_ve_os_ssh_key': symbols.ssh_key,
            'admin_password': symbols.bigip_admin_password,
            'root_password': symbols.bigip_root_password,
            'license': symbols.license
        }
    )
    updated_stack = hc.stacks.get(stack.id)
    floating_ip = get_floating_ip_output(updated_stack)
    bigip = WaitForLicensedBigIP(
        floating_ip, 'admin', symbols.bigip_admin_password,
        BIGIP_12_0_VERSION, 3
    )
    check_net_components(bigip, 3)
