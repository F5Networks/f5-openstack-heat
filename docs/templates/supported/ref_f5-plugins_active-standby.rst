F5® BIG-IP® Active-Standby Cluster
==================================

Overview
--------
The active-standby cluster template configures two (2) BIG-IP® devices to function as an 'active-standby pair' in a 'sync-failover device group'. An :dfn:`active-standby pair` is a pair of BIG-IP® devices configured so that one device is actively processing traffic while the other device remains ready to take over if failover occurs. A :dfn:`sync-failover device group` contains devices that synchronize their configuration data and fail over to one another if a device becomes unavailable.

Prerequisites
-------------

- Two (2) licensed, functional BIG-IP® devices (hardware or Virtual Edition) connected to the same 'control' VLAN [#]_

.. seealso::

    * :ref:`F5® VE Cluster-Ready 4-nic` Heat template: deploys a pair of BIG-IP® VE devices that are ready for clustering.

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

.. rubric:: Footnotes

.. [#] The 'control' VLAN is a network used for high availability and mirroring. Both devices must be connected to the same network in order for the high availability features deployed by this template to function.

