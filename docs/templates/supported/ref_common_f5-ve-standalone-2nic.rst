.. _ve2nic:

F5 BIG-IP VE: Standalone, 2-nic
===============================

Overview
--------

This template can be used to deploy a standard, standalone F5 BIG-IP VE in OpenStack. :dfn:`Standalone` refers to a single device that can either function on its own, or be added to a device service group.

Prerequisites
-------------

- An external network with access to the internet.

- Basic understanding of `BIG-IP system configuration <https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-initial-configuration-12-0-0/2.html>`_.

- :ref:`F5 OpenStack Heat Plugins <heatplugins:home>` installed on the Neutron controller.

- :ref:`SSH key(s) <add-ssh-key-horizon>` configured in OpenStack; to be used for authentication to the BIG-IP VE instances launched by this template.

- :ref:`BIG-IP VE image <F5 BIG-IP VE: Image Patch & Upload>` uploaded to Glance.

- Two (2) VLANs :ref:`configured in Neutron <docs:os-neutron-network-setup>` -- 'mgmt' and 'data' - to be used for system management and data traffic, respectively.


Caveats
-------

- This template requires internet access; it needs to be able to access GitHub to fetch dependent Heat templates that configure the necessary :ref:`security groups <BIG-IP Security Groups>`.

- This template deploys an unlicensed BIG-IP VE. You will need to add your `F5 TMOS License Basekey <https://support.f5.com/kb/en-us/solutions/public/7000/700/sol7752.html>`_ manually.

- VE images come in 3 different sizes: LTM, ALL, and LTM-1SLOT. Each has its own size requirements, which  determine what Nova flavor you should select. See the F5 OpenStack `BIG-IP flavor matrix <http://f5-openstack-docs.readthedocs.org/en/latest/guides/openstack_big-ip_flavors.html>`_ for more information.

Deployment
----------

.. include:: /includes/topic_for-reuse_how-to-deploy.rst


.. list-table:: Configuration Items
    :widths: 10, 10, 20
    :header-rows: 1

    * - Configuration Item
      - Type
      - Entry/Description
    * - Stack Name
      - string
      - Provide a name for the stack to be created
    * - Creation Timeout
      - integer
      - Length of time after which stack creation will time out (minutes)
    * - Password for user "<username>"
      - string
      - Enter the password for your user account
    * - F5 VE Image
      - string
      - Select a VE image from the dropdown list
    * - F5 VE Flavor
      - string
      - Select a flavor to be used for the VE (default: m1.medium)
    * - Use Config Drive
      - boolean
      - Use config drive to provider meta and user data (default: false)
    * - F5 Root SSH Key Name
      - string
      - Name of existing ssh key-pair to use for authentication to the VE instances
    * - External Network
      - string
      - Select the external network from the list
    * - VE Management Network
      - string
      - Select a subnet from the list to be used as the VE management interface network
    * - VE Network for the 1.1 Interface
      - string
      - Select a network to be used for the VE 1.1 TMM interface
    * - Name for Network 1.1
      - string
      - Enter a name for the  Network 1.1 (default: network-1.1)
    * - Default Gateway IP
      - string
      - Enter the upstream Gateway IP address to use for VE instance (default: none)


Download
--------

Click the download link below to save a copy of the template.

:download:`Download </../f5_supported/ve/standalone/f5_ve_standalone_2_nic.yaml>`

