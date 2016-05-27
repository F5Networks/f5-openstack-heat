F5® VE Cluster-Ready 4-nic
==========================

Overview
--------

This template deploys a 'cluster-ready' pair of BIG-IP® VEs. Each device has four (4) network interfaces: management, control, and two (2) data interfaces. The control interface, which is named 'HA', is configured to allow connection failover traffic, configuration synchronization, and connection mirroring. Using a control interface allows for the separation of control traffic from client/user data.


Prerequisites
-------------

- Basic understanding of BIG-IP® `device service clustering <https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-device-service-clustering-admin-12-0-0.html>`_.

- `License base key <https://support.f5.com/kb/en-us/solutions/public/7000/700/sol7752.html>`_ for BIG-IP® VE.

- :ref:`BIG-IP® Security Groups` configured in OpenStack.

- :ref:`BIG-IP® VE image <F5 VE Image Patch Upload>` uploaded to Glance.

- Three (3) VLANs :ref:`configured in Neutron <docs:os-neutron-network-setup>`: control, data, and management.

- :ref:`SSH key(s) <add-ssh-key-horizon>` configured in OpenStack; to be used for authentication to the BIG-IP® VE instances launched by this template.


Caveats
-------

None.


Deployment
----------

.. include:: ../../includes/topic_for-reuse_how-to-deploy.rst
    :start-line: 5

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
      - Select a VE image from the dropdown list [#]_
    * - F5 VE Flavor
      - string
      - Select a flavor to be used for the VE
    * - Use Config Drive
      - boolean
      - Use config drive to provider meta and user data (default: false)
    * - F5 Root SSH Key Name
      - string
      - Name of existing ssh key-pair to use for authentication to the VE instances
    * - F5 VE Admin User Password
      - string
      - Create a password for the VE 'admin' user account
    * - F5 VE Root User Password
      - string
      - create a password for the VE 'root' user account
    * - Security Group for the data network
      - string
      - Enter the name of an existing security group [#]_
    * - Security Group for the control network
      - string
      - Enter the name of an existing security group
    * - Security Group for the management network
      - string
      - Enter the name of an existing security group
    * - Primary VE License Base Key
      - string
      - Enter your `F5 TMOS License Basekey <https://support.f5.com/kb/en-us/solutions/public/7000/700/sol7752.html>`_
    * - External Network
      - string
      - Select the external network from the list
    * - VE Management Network
      - string
      - Select a subnet from the list to be used as the VE management interface network
    * - VE HA Network
      - string
      - Select a subnet from the list to be used as the VE HA interface network
    * - VE Network for the 1.2 Interface
      - string
      - Select a network to be used for the VE 1.2 TMM interface
    * - Name for Network 1.2
      - string
      - Enter a name for the  Network 1.2 (default: data1)
    * - VE Network for the 1.3 Interface
      - string
      - Select a network to be used for the VE 1.3 TMM interface
    * - Name for Network 1.3
      - string
      - Enter a name for the  Network 1.2 (default: data2)
    * - Default Gateway IP
      - string
      - Enter the upstream Gateway IP address to use for VE instances (default: none)



Download
--------

Click the download link below to save a copy of the template.

:download:`Download <../../../f5_supported/ve/common/cluster_ready_ve_4_nic.yaml>`


.. rubric:: Footnotes

.. [#] You must already have at least one VE image :ref:`onboarded <how-to_onboard-ve>` to Glance.
.. [#] See :ref:`BIG-IP® Security Groups` for more information.
