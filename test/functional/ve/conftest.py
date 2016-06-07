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

import pytest
import time


@pytest.fixture
def WaitForLicensedBigIP():
    def poll_for_licensed_bigip(
            bigip_ip, username, password, bigip_ver,
            ifc_num, attempts=50, interval=10
    ):
        '''Poll the device until it is licensed and has a config.'''
        for attempt in range(attempts):
            time.sleep(interval)
            try:
                bigip = ManagementRoot(bigip_ip, username, password)
                registration = bigip.tm.shared.licensing.registration.load()
                assert registration.licensedVersion == bigip_ver
                assert len(bigip.tm.net.vlans.get_collection()) == ifc_num - 1
                assert len(bigip.tm.net.interfaces.get_collection()) == ifc_num
                assert len(bigip.tm.net.selfips.get_collection()) == \
                    ifc_num - 1
                return bigip
            except Exception as ex:
                if attempt == (attempts - 1):
                    raise ex
                continue
    return poll_for_licensed_bigip
