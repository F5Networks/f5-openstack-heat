.. _4nic-cluster-ready:

F5 BIG-IP VE: Cluster-Ready, 4-nic
==================================

Overview
--------

This template deploys a "cluster-ready" pair of BIG-IP Virtual Edition (VE) devices. Each device has four (4) network interfaces: management, control, and two (2) data interfaces.
The control interface ("HA") allows connection failover traffic, configuration synchronization, and connection mirroring.
Using a control interface allows for the separation of control traffic from client/user data.


Prerequisites
-------------

- `F5 OpenStack Heat Plugins`_ installed on the Neutron controller.
- `BIG-IP Security Groups`_ configured in OpenStack.
- SSH key(s) configured in OpenStack.
- :ref:`BIG-IP VE image uploaded to Glance <ve-image-patch-upload>`.
- `BIG-IP license base key`_.
- Three (3) VLANs configured in Neutron -- 'mgmt', 'control', and 'data' -- to use for system management, high availability, and data traffic, respectively.
- Basic understanding of `BIG-IP device service clustering`_.

Caveats
-------

- `BIG-IP VE images come in different sizes`_.
  The `Nova compute flavor`_ you should use for your image depends on the image's disk size requirements.
  See the F5 OpenStack `BIG-IP flavor matrix`_ for more information.

Configuration Parameters
------------------------

=========================================== =============== =========================== ===============
Parameter                                   Type            Description                 Default
=========================================== =============== =========================== ===============
Stack Name                                  string          Provide a name for the      N/A
                                                            stack
------------------------------------------- --------------- --------------------------- ---------------
Creation Timeout                            integer         Length of time after which  N/A
                                                            stack creation will time
                                                            out (minutes)
------------------------------------------- --------------- --------------------------- ---------------
Password for user "<username>"              string          The password for your       N/A
                                                            OpenStack user account
------------------------------------------- --------------- --------------------------- ---------------
F5 VE Image                                 string          Choose a BIG-IP VE image    N/A
                                                            from the dropdown list
------------------------------------------- --------------- --------------------------- ---------------
F5 VE Flavor                                string          Choose a flavor for the     N/A
                                                            BIG-IP VE
------------------------------------------- --------------- --------------------------- ---------------
Use Config Drive                            boolean         Use config drive to provide False
                                                            meta and user data
------------------------------------------- --------------- --------------------------- ---------------
F5 Root SSH Key Name                        string          Choose an ssh key-pair;     N/A
                                                            used for authentication to
                                                            the BIG-IP VE instances
------------------------------------------- --------------- --------------------------- ---------------
F5 VE Admin User Password                   string          Create a password for the   N/A
                                                            BIG-IP VE 'admin' user
                                                            account
------------------------------------------- --------------- --------------------------- ---------------
F5 VE Root User Password                    string          create a password for the   N/A
                                                            BIG-IP VE 'root' user
                                                            account
------------------------------------------- --------------- --------------------------- ---------------
Security Group for the data network         string          Enter the name of a         N/A
                                                            security group
------------------------------------------- --------------- --------------------------- ---------------
Security Group for the control network      string          Enter the name of a         N/A
                                                            security group
------------------------------------------- --------------- --------------------------- ---------------
Security Group for the management network   string          Enter the name of a         N/A
                                                            security group
------------------------------------------- --------------- --------------------------- ---------------
Primary VE License Base Key                 string          Enter your F5 license       N/A
                                                            base registration key
------------------------------------------- --------------- --------------------------- ---------------
External Network                            string          Choose the external network N/A
                                                            from the list
------------------------------------------- --------------- --------------------------- ---------------
VE Management Network                       string          Assign a Neutron subnet     N/A
                                                            to the management interface
                                                            on the BIG-IP VE instances
------------------------------------------- --------------- --------------------------- ---------------
VE HA Network                               string          Assign a Neutron subnet     N/A
                                                            to the high availability
                                                            interface on the
                                                            BIG-IP VE instances
------------------------------------------- --------------- --------------------------- ---------------
VE Network for the 1.2 Interface            string          Assign a Neutron network    N/A
                                                            to the 1.2 interface on the
                                                            BIG-IP VE instances
------------------------------------------- --------------- --------------------------- ---------------
Name for Network 1.2                        string          Enter a name for the 1.2    data1
                                                            network on the BIG-IP VE
                                                            instances
------------------------------------------- --------------- --------------------------- ---------------
VE Network for the 1.3 Interface            string          Assign a Neutron network    N/A
                                                            to the 1.2 interface on the
                                                            BIG-IP VE instances
------------------------------------------- --------------- --------------------------- ---------------
Name for Network 1.3                        string          Enter a name for the 1.3    data2
                                                            network on the BIG-IP VE
                                                            instances
------------------------------------------- --------------- --------------------------- ---------------
Default Gateway IP                          string          Enter the Gateway IP        none
                                                            address to use for the
                                                            BIG-IP VE instances
=========================================== =============== =========================== ===============

Deployment
----------

See the `F5 OpenStack Heat template deployment instructions`_.

Download
--------

Click the link below to download the template.

:download:`Download </../f5_supported/ve/common/cluster_ready_ve_4_nic.yaml>`



