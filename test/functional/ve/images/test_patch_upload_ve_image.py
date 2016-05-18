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


BIGIP_12_0_IMG = 'BIGIP-12.0.0.0.0.606'
BIGIP_11_6_IMG = 'BIGIP-11.6.0.0.0.401'
BIGIP_11_5_4_IMG = 'BIGIP-11.5.4.0.0.256'


@pytest.fixture
def GlanceImageCleanup(request, glanceclientmanager):
    def manage_glance(ve_image_name):
        def teardown_glance_image():
            images = [image for image in glanceclientmanager.images.list()]
            for image in images:
                if ve_image_name == image.name:
                    glanceclientmanager.images.delete(image.id)
        # You can run these tests and not teardown the glance images.
        # They can then be used for booting a VE
        if not request.config.getoption('--no-teardown-glance-images'):
            request.addfinalizer(teardown_glance_image)
    return manage_glance


@pytest.fixture
def PatchTemplateLoc(SupportedDir):
    return os.path.join(
        os.path.join(
            SupportedDir, 've', 'images', 'patch_upload_ve_image.yaml'
        )
    )


def test_patched_image_upload_12_0(
        HeatStack,
        GlanceImageCleanup,
        symbols,
        glanceclientmanager,
        PatchTemplateLoc
):
    hc, stack = HeatStack(
        PatchTemplateLoc,
        'func_test_patch_ve_image',
        parameters={
            'onboard_image': 'ubuntu_14.04_lts',
            'image_prep_key': 'testlab',
            'private_network': 'mgmt_net',
            'f5_image_import_password': symbols.os_password,
            'f5_ve_image_url': symbols.ve_12_0_image_path,
            'f5_ve_image_name': BIGIP_12_0_IMG + '.qcow2',
            'apt_cache_proxy_url': 'http://apt-cache.pdbld.f5net.com:3142',
            'f5_image_import_auth_url':
            'http://{}:5000/v2.0'.format(symbols.auth_netloc)
        }
    )
    assert BIGIP_12_0_IMG in \
        [image.name for image in glanceclientmanager.images.list()]
    GlanceImageCleanup(BIGIP_12_0_IMG)


def test_patched_image_upload_11_6(
        HeatStack,
        GlanceImageCleanup,
        symbols,
        glanceclientmanager,
        PatchTemplateLoc
):
    hc, stack = HeatStack(
        PatchTemplateLoc,
        'func_test_patch_ve_image',
        parameters={
            'onboard_image': 'ubuntu_14.04_lts',
            'image_prep_key': 'testlab',
            'private_network': 'mgmt_net',
            'f5_image_import_password': symbols.os_password,
            'f5_ve_image_url': symbols.ve_11_6_image_path,
            'apt_cache_proxy_url': 'http://apt-cache.pdbld.f5net.com:3142',
            'f5_ve_image_name': BIGIP_11_6_IMG + '.qcow2',
            'f5_image_import_auth_url':
            'http://{}:5000/v2.0'.format(symbols.auth_netloc)
        }
    )
    assert BIGIP_11_6_IMG in \
        [image.name for image in glanceclientmanager.images.list()]
    GlanceImageCleanup(BIGIP_11_6_IMG)


def test_patched_image_upload_11_5(
        HeatStack,
        GlanceImageCleanup,
        symbols,
        glanceclientmanager,
        PatchTemplateLoc
):
    hc, stack = HeatStack(
        PatchTemplateLoc,
        'func_test_patch_ve_image',
        parameters={
            'onboard_image': 'ubuntu_14.04_lts',
            'image_prep_key': 'testlab',
            'private_network': 'mgmt_net',
            'f5_image_import_password': symbols.os_password,
            'f5_ve_image_url': symbols.ve_11_5_4_image_path,
            'f5_ve_image_name': BIGIP_11_5_4_IMG + '.qcow2',
            'apt_cache_proxy_url': 'http://apt-cache.pdbld.f5net.com:3142',
            'f5_image_import_auth_url':
            'http://{}:5000/v2.0'.format(symbols.auth_netloc)

        }
    )
    assert BIGIP_11_5_4_IMG in \
        [image.name for image in glanceclientmanager.images.list()]
    GlanceImageCleanup(BIGIP_11_5_4_IMG)
