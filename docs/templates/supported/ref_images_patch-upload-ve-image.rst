.. _ve-image:

F5 BIG-IP VE: Image Patch & Upload
==================================

Overview
--------

This template can be used to prepare a BIG-IP VE image for use in OpenStack. It launches an Ubuntu server that downloads a zipped F5 BIG-IP VE qcow image, extracts it, and patches it. The patched image is then uploaded to Glance so it can be used to launch BIG-IP instances.


Prerequisites
-------------

- An external network with access to the internet.

- Basic understanding of `BIG-IP system configuration <https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-initial-configuration-12-0-0/2.html>`_.

- BIG-IP LTM Virtual Edition image file in qcow.zip format; can be any size (ALL, LTM, or LTM_1SLOT). [#]_

- :ref:`F5 OpenStack Heat Plugins <heatplugins:home>` installed on the Neutron controller.

- :ref:`SSH key(s) <add-ssh-key-horizon>` configured in OpenStack; to be used for authentication to the BIG-IP VE instances launched by this template.

- One (1) VLAN :ref:`configured in Neutron <docs:os-neutron-network-setup>`, to be used by the onboarding server to import the image.


Caveats
-------

- The BIG-IP image must be hosted in a location accessible to the Heat engine via 'http'. This template does not currently support retrieval of files via 'https' or file uploads.

- VE images come in 3 different sizes: LTM, ALL, and LTM-1SLOT. Each has its own size requirements, which  determine what Nova flavor you should select. See the F5 OpenStack `BIG-IP flavor matrix <http://f5-openstack-docs.readthedocs.org/en/latest/guides/openstack_big-ip_flavors.html>`_ for more information.

- There is a `known issue <https://bugs.launchpad.net/glance/+bug/1476770>`_ with ``python-glanceclient`` that returns in an unspecified error after you click :guilabel:`Launch`. You may need to upgrade in order to resolve this issue.


Deployment
----------

.. include:: /includes/topic_for-reuse_how-to-deploy.rst

.. list-table:: Configuration Items
    :widths: 10, 10, 20
    :header-rows: 1

    * - Configuration Item
      - Type
      - Entry/Description
    * - Onboard Ubuntu Image
      - string
      - Select an Ubuntu image to use for the onboarding server
    * - F5 Onboard Server Flavor
      - string
      - Select a Nova flavor for the onboarding server (default: m1.medium)
    * - Use Config Drive
      - boolean
      - Use config drive to provider meta and user data to the orchestration instance (default: false)
    * - F5 Onboard Server Management Network
      - string
      - Select a network to attach the onboarding server to
    * - Keystone Auth URL
      - string
      - Keystone Authentication URL for your OpenStack cloud (example: \http://<ip_address>:5000/v2.0)
    * - Image Import Tenant
      - string
      - Name of tenant to which image should be imported (default: admin)
    * - Image Import User
      - string
      - User account to which image should be imported (default: admin)
    * - Image Prep URL
      - string
      - URL of F5 Networks GitHub repo where image prep tools reside (DO NOT CHANGE)
    * - F5 VE Image URL
      - string
      - URL where VE image can be accessed (**must use http**)
    * - F5 VE Image Name
      - string
      - Name of the VE image in the qcow.zip file (example: :file:`BIGIP-11.6.0.6.0.442.qcow2`)
    * - SSH Key
      - string
      - SSH Key to use for authentication to the onboarding server
    * - Apt-cache URL
      - string
      - URL for local apt-cache proxy (default: None)


Download
--------

Click the download link below to save a copy of the template.

:download:`Download </../f5_supported/ve/images/patch_upload_ve_image.yaml>`


.. [#] `How to Buy <https://f5.com/products/how-to-buy>`_
