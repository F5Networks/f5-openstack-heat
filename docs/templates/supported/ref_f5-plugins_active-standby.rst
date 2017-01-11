.. _active-standby-cluster:

F5 BIG-IP: Active-Standby Cluster
=================================

Overview
--------

The active-standby cluster template configures two (2) BIG-IP devices to function as an 'active-standby pair' in a 'sync-failover device group'. An :dfn:`active-standby pair` is a pair of BIG-IP devices configured so that one device is actively processing traffic while the other device remains ready to take over if failover occurs. A :dfn:`sync-failover device group` contains devices that synchronize their configuration data and fail over to one another if a device becomes unavailable.

Prerequisites
-------------

- Basic understanding of `BIG-IP device service clustering <https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-device-service-clustering-admin-12-0-0.html>`_.

- :ref:`F5 OpenStack Heat Plugins <heatplugins:home>` installed on the Neutron controller.

- Three (3) VLANs :ref:`configured in Neutron <docs:os-neutron-network-setup>` -- 'mgmt', 'control', and 'data' -- to be used for system management, high availability, and data traffic, respectively.

- Two (2) licensed, operational BIG-IP devices (hardware or Virtual Edition); both must be connected to the 'control' VLAN.

- Login credentials for user(s) with administrative permissions on BIG-IP device(s).


.. seealso::

    * :ref:`F5 BIG-IP VE: Cluster-Ready, 4-nic` Heat template: deploys a pair of BIG-IP VE devices that are ready for clustering.


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
    * - Cluster Name
      - string
      - the name you'd like to assign to the new cluster
    * - FIP for first device
      - string
      - Floating IP address of the first BIG-IP
    * - FIP for second device
      - string
      - Floating IP address of the second BIG-IP
    * - Username for first device
      - string
      - the username of an admin user for the first BIG-IP
    * - Password for first device
      - string
      - the admin user's password for the first BIG-IP
    * - Username for second device
      - string
      - the username of an admin user for the second BIG-IP
    * - Password for second device
      - string
      - the admin user's password for the second BIG-IP



Download
--------

Click the download link below to save a copy of the template.

:download:`Download <../../../f5_supported/f5_plugins/active-standby.yaml>`



