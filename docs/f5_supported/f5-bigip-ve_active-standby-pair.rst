.. _active-standby-pair:

F5 BIG-IP VE: Active-Standby Pair
=================================

Overview
--------

The active-standby cluster template configures two (2) BIG-IP devices as an "active-standby" `sync-failover device group`_.

Prerequisites
-------------

- `F5 Plugins for OpenStack Heat`_ installed on the Neutron controller.
- Three (3) VLANs configured in Neutron -- 'mgmt', 'control', and 'data' -- to use for system management, high availability, and data traffic, respectively.
- Two (2) licensed, operational BIG-IP devices (hardware or Virtual Edition), connected to the 'control' VLAN.
- Login credentials for user with permission to configure the BIG-IP devices.
- Basic understanding of `BIG-IP device service clustering`_.

Caveats
-------

None.


Configuration Parameters
------------------------

=============================== =============== =========================== ===============
Parameter                       Type            Description                 Default
=============================== =============== =========================== ===============
Stack Name                      string          Name for the stack          N/A
------------------------------- --------------- --------------------------- ---------------
Creation Timeout                integer         Length of time after which  N/A
                                                stack creation will time
                                                out (minutes)
------------------------------- --------------- --------------------------- ---------------
Password for user "<username>"  string          The password for your       N/A
                                                OpenStack user account
------------------------------- --------------- --------------------------- ---------------
Cluster Name                    string          Assign a name to the new    N/A
                                                cluster
------------------------------- --------------- --------------------------- ---------------
FIP for first device            string          Floating IP address of the
                                                first BIG-IP device         N/A
------------------------------- --------------- --------------------------- ---------------
FIP for second device           string          Floating IP address of the  N/A
                                                second BIG-IP device
------------------------------- --------------- --------------------------- ---------------
Username for first device       string          Username for the first      N/A
                                                BIG-IP device
------------------------------- --------------- --------------------------- ---------------
Password for first device       string          Password for the first      N/A
                                                BIG-IP device
------------------------------- --------------- --------------------------- ---------------
Username for second device      string          Username for the second     N/A
                                                BIG-IP device
------------------------------- --------------- --------------------------- ---------------
Password for second device      string          Password for the second     N/A
                                                BIG-IP device
=============================== =============== =========================== ===============


Deployment
----------

See the `F5 HOT deployment instructions`_.


Download
--------

Click the link below to download the template.

:download:`Download </../f5_supported/f5_plugins/active_standby.yaml>`


.. _sync-failover device group: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-device-service-clustering-administration-13-0-0/4.html
