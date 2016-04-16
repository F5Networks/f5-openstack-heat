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


def pytest_addoption(parser):
    parser.addoption('--bigip-admin-password', action='store',
                     help='Default BIGIP admin password')
    parser.addoption('--bigip-root-password', action='store',
                     help='Default BIGIP root password')
    parser.addoption('--license', action='store',
                     help='BIGIP license key')
    parser.addoption('--no-teardown-glance-images', action='store_true',
                     default=False,
                     help='Include if you do not wish to remove images '
                     'pushed into glance.')


@pytest.fixture
def BigIPConfig(request, scope='module'):
    '''Provides BIGIP password and license configuration.'''
    admin_password = request.config.getoption('--bigip-admin-password')
    root_password = request.config.getoption('--bigip-root-password')
    license = request.config.getoption('license')
    return admin_password, root_password, license


@pytest.fixture
def OSPassword(request):
    return request.config.getoption('--os-password')


@pytest.fixture
def AuthAddress(request):
    return request.config.getoption('--auth-netloc')


@pytest.fixture
def UnsupportedDir():
    base_repo_dir = \
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )
        )
    unsupported_dir = os.path.join(base_repo_dir, 'unsupported')
    return unsupported_dir
