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

from f5.bigip import BigIP
import os
import time


HEAT_DIR = '/root/heat/unsupported/ve/common'
BIGIP_11_5_4_IMG = 'BIGIP-11.5.4.0.0.256'
BIGIP_11_5_4_VERSION = '11.5.4'
BIGIP_11_6_IMG = 'BIGIP-11.6.0.0.0.401'
BIGIP_11_6_VERSION = '11.6.0'
BIGIP_12_0_IMG = 'BIGIP-12.0.0.0.0.606'
BIGIP_12_0_VERSION = '12.0.0'


def get_floating_ip_output(stack):
    for output in stack.outputs:
        if 'floating_ip' == output['output_key']:
            return output['output_value']


def wait_for_active_licensed_bigip(
        bigip_ip, username, password, bigip_version
):
    # We can hide this later and refine the values
    max_attempts = 50
    interval = 10
    # This thing is going to take at least a minute to get networking up
    time.sleep(60)
    bigip = BigIP(bigip_ip, username, password)
    for attempt in range(max_attempts):
        time.sleep(interval)
        try:
            registration = bigip.shared.licensing.registration.load()
            assert registration.licensedVersion == bigip_version
            return
        except Exception:
            continue


# These tests require a patched VE instance in your stack

def itest_f5_base_instance_deploy_3_nic_11_5_4(HeatStack, BigIPConfig):
    admin_password, root_password, license = BigIPConfig
    hc, stack = HeatStack(
        os.path.join(HEAT_DIR, 'f5_ve_standalone_3_nic.yaml'),
        'func_test_standalone_3_nic',
        parameters={
            've_image': BIGIP_11_5_4_IMG,
            'external_network': 'external_network',
            'mgmt_network': 'mgmt_net',
            'network_1': 'data1_net',
            'network_2': 'data2_net',
            'f5_ve_os_ssh_key': 'testlab',
            'admin_password': admin_password,
            'root_password': root_password,
            'license': license
        }
    )
    updated_stack = hc.stacks.get(stack.id)
    floating_ip = get_floating_ip_output(updated_stack)
    wait_for_active_licensed_bigip(
        floating_ip, 'admin', admin_password, BIGIP_11_5_4_VERSION
    )


def test_f5_base_instance_deploy_3_nic_11_6(HeatStack, BigIPConfig):
    admin_password, root_password, license = BigIPConfig
    hc, stack = HeatStack(
        os.path.join(HEAT_DIR, 'f5_ve_standalone_3_nic.yaml'),
        'func_test_standalone_3_nic',
        parameters={
            've_image': BIGIP_11_6_IMG,
            'external_network': 'external_network',
            'mgmt_network': 'mgmt_net',
            'network_1': 'data1_net',
            'network_2': 'data2_net',
            'f5_ve_os_ssh_key': 'testlab',
            'admin_password': admin_password,
            'root_password': root_password,
            'license': license
        }
    )
    updated_stack = hc.stacks.get(stack.id)
    floating_ip = get_floating_ip_output(updated_stack)
    wait_for_active_licensed_bigip(
        floating_ip, 'admin', admin_password, BIGIP_11_6_VERSION
    )


def test_f5_base_instance_deploy_3_nic_12_0(HeatStack, BigIPConfig):
    admin_password, root_password, license = BigIPConfig
    hc, stack = HeatStack(
        os.path.join(HEAT_DIR, 'f5_ve_standalone_3_nic.yaml'),
        'func_test_standalone_3_nic',
        parameters={
            've_image': BIGIP_12_0_IMG,
            'external_network': 'external_network',
            'mgmt_network': 'mgmt_net',
            'network_1': 'data1_net',
            'network_2': 'data2_net',
            'f5_ve_os_ssh_key': 'testlab',
            'admin_password': admin_password,
            'root_password': root_password,
            'license': license
        }
    )
    updated_stack = hc.stacks.get(stack.id)
    floating_ip = get_floating_ip_output(updated_stack)
    wait_for_active_licensed_bigip(
        floating_ip, 'admin', admin_password, BIGIP_12_0_VERSION
    )
