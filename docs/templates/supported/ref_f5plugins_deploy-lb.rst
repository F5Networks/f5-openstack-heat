Deploy Basic Load Balancer
==========================

Overview
--------

This template deploys a basic load balancing scenario on an F5® BIG-IP® device (hardware or virtual edition). The deployment includes the following resources: one (1) client vm; one (1) server vm; one (1) virtual server, one (1) pool, and one (1) pool member are created on the server vm.

Prerequisites
-------------

- Licensed, operational BIG-IP® hardware or VE.

- Glance image(s) [#]_ for the OS of your choice, to be used for the client and server.

- :ref:`BIG-IP® Security Groups` configured in OpenStack.

- :ref:`SSH key(s) <add-ssh-key-horizon>` configured in OpenStack; to be used for authentication to the vm instances launched by this template.

- :ref:`F5 OpenStack Heat Plugins <heatplugins:home>` installed on the Neutron controller.

- At least two (2) VLANs :ref:`configured in Neutron <docs:os-neutron-network-setup>` -- 'mgmt' and 'data' - to be used for BIG-IP® system management and client-server data traffic, respectively.


Caveats
-------

None.


Deployment
----------

.. include:: ../../includes/topic_for-reuse_how-to-deploy.rst
    :start-line: 3

.. list-table:: Configuration Items
    :widths: 10, 10, 20
    :header-rows: 1

    * - Configuration Item
      - Type
      - Entry/Description
    * - Client/Server Glance Image
      - string
      - Image to use for client and server
    * - Client/Server Nova Flavor
      - string
      - Nova flavor to use for client and server
    * - Key Name
      - string
      - The SSH key to use for authentication to the client and server
    * - Security Group
      - string
      - Security group to use for client and server
    * - Client Network
      - string
      - Network for client traffic
    * - Server Network
      - string
      - Network for server traffic
    * - BIG-IP Login Username
      - string
      - Username for an administrator account on the BIG-IP (default: admin)
    * - BIG-IP Login Password
      - string
      - Password for the administrator account on the BIG-IP
    * - Virtual Server Name
      - string
      - Enter a name for the virtual server that will be created (default: virtual_server1)
    * - Pool Name
      - string
      - Enter a name for the pool that will be created (default: pool1)
    * - BIG-IP Floating IP  bigip_fip:
      - string
      - the Floating IP address of the BIG-IP
    * - Virtual Server VIP
      - string
      - Virtual Server Virtual IP address
    * - Virtual Server Port
      - number
      - Port that the virtual server will listen on (default: 443)
    * - Pool Member Port
      - number
      - Port on which the pool member can receive traffic (default: 8080)


Download
--------

Click the download link below to save a copy of the template.

:download:`Download <../../../f5_supported/f5_plugins/deploy_lb.yaml>`


.. rubric:: Footnotes:

.. [#] :ref:`Adding a Ubuntu Image to Glance <add-ubuntu-image-glance>` contains instructions for uploading an image to Glance via the OpenStack dashboard. You may use the OS of your choice; Ubuntu is not a requirement for this template.


