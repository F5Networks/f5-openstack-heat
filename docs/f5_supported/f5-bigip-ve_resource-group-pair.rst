.. _cluster-prep:

F5 BIG-IP VE: Cluster-Ready Resource Group
==========================================

Overview
--------

This template deploys two (2) BIG-IP Virtual Edition (VE) instances in OpenStack using the F5-supported :ref:`cluster-ready 4nic <4nic-cluster-ready>` Heat orchestration template.

Prerequisites
-------------

- `F5 Plugins for OpenStack Heat`_ installed on the Neutron controller.
- :ref:`BIG-IP security groups <big-ip security groups>` configured in OpenStack.
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
VE Management Network                       string          Choose a subnet from the    N/A
                                                            list; used as the BIG-IP
                                                            VE management interface
                                                            network
------------------------------------------- --------------- --------------------------- ---------------
VE HA Network                               string          Choose a subnet from the    N/A
                                                            list; used as the BIG-IP VE
                                                            high availability interface
                                                            network
------------------------------------------- --------------- --------------------------- ---------------
VE Network for the 1.2 Interface            string          Assign a network to the     N/A
                                                            BIG-IP VE 1.2 TMM interface
------------------------------------------- --------------- --------------------------- ---------------
Name for Network 1.2                        string          Enter a name for the 1.2    data1
                                                            network
------------------------------------------- --------------- --------------------------- ---------------
VE Network for the 1.3 Interface            string          Assign a network to the      N/A
                                                            BIG-IP VE 1.3 TMM interface
------------------------------------------- --------------- --------------------------- ---------------
Name for Network 1.3                        string          Enter a name for the 1.3    data2
                                                            network
------------------------------------------- --------------- --------------------------- ---------------
Default Gateway IP                          string          Enter the Gateway IP        none
                                                            address to use for VE
                                                            instances
=========================================== =============== =========================== ===============


Deployment
----------

See the `F5 HOT deployment instructions`_.

Download
--------

Click the link below to download the template.

:download:`Download </../f5_supported/ve/resource_group/f5_two_ve_resource_group.yaml>`
