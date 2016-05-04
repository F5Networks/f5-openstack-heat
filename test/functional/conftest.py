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
    parser.addoption('--no-teardown-glance-images', action='store_true',
                     default=False,
                     help='Include if you do not wish to remove images '
                     'pushed into glance.')
    parser.addoption('--bigip-fip', action='store',
                     help='The Floating IP for the BigIP.')
    parser.addoption('--vs-vip', action='store',
                     help='The Virtual IP for the virtual server.')


@pytest.fixture
def BaseRepoDir():
    base_repo_dir = \
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )
        )
    return base_repo_dir


@pytest.fixture
def UnsupportedDir(BaseRepoDir):
    return os.path.join(BaseRepoDir, 'unsupported')


@pytest.fixture
def SupportedDir(BaseRepoDir):
    return os.path.join(BaseRepoDir, 'f5_supported')
