.. _deploy-lb:

Deploy Basic Load Balancer
==========================

Overview
--------

This template deploys a basic load balancing scenario on a BIG-IP device (hardware or virtual edition).
The stack includes the following resources:

- one (1) client virtual machine (VM);
- one (1) server VM;
- one (1) virtual server, one (1) pool, and one (1) pool member created on the BIG-IP device for the server VM.

Prerequisites
-------------

- Licensed, operational BIG-IP device (hardware or VE) accessible to the OpenStack cloud.
- `Glance image`_ for the OS of your choice, to use for the VMs.
- `BIG-IP Security Groups`_ configured in OpenStack.
- SSH key(s) configured in OpenStack; to use for authentication to the VM instances launched by this template.
- `F5 OpenStack Heat Plugins`_ installed on the Neutron controller.
- At least two (2) VLANs configured in Neutron -- 'mgmt' and 'data' -- to use for BIG-IP system management and client-server data traffic, respectively.

Caveats
-------

None.


Configuration Parameters
------------------------

=============================== =============== =========================== ===============
Parameter                       Type            Description                 Default
=============================== =============== =========================== ===============
Client/Server Glance Image      string          Image to use for VMs        N/A
------------------------------- --------------- --------------------------- ---------------
Client/Server Nova Flavor       string          `Nova Compute flavor`_ to   N/A
                                                use for VMs
------------------------------- --------------- --------------------------- ---------------
Key name                        string          ssh key to use for
                                                authentication to VMs       N/A
------------------------------- --------------- --------------------------- ---------------
Security Group                  string          security group to assign    N/A
                                                to VMs
------------------------------- --------------- --------------------------- ---------------
Client Network                  string          Client traffic network      N/A
------------------------------- --------------- --------------------------- ---------------
Server Network                  string          Server traffic network      N/A
------------------------------- --------------- --------------------------- ---------------
BIG-IP Login Username           string          BIG-IP device username      N/A
------------------------------- --------------- --------------------------- ---------------
BIG-IP Login Password           string          BIG-IP device password      N/A
------------------------------- --------------- --------------------------- ---------------
Virtual Server Name             string          Name to assign to the       virtual_server1
                                                virtual server
------------------------------- --------------- --------------------------- ---------------
Pool Name                       string          Name to assign to the pool  pool1
------------------------------- --------------- --------------------------- ---------------
BIG-IP Floating IP              string          The BIG-IP device's         N/A
(``bigip_fip``)                                 floating IP address
------------------------------- --------------- --------------------------- ---------------
Virtual Server VIP              string          Virtual IP address to       N/A
                                                assign to the virtual
                                                server
------------------------------- --------------- --------------------------- ---------------
Virtual Server Port             integer         Port the virtual server     443
                                                should listen on
------------------------------- --------------- --------------------------- ---------------
Pool Member Port                integer         Port the pool member can    8080
                                                receive traffic on
=============================== =============== =========================== ===============

Deployment
----------

See the `F5 OpenStack Heat template deployment instructions`_.


Download
--------

Click the link below to download the template.

:download:`Download </../f5_supported/f5_plugins/deploy_lb.yaml>`


.. _Glance image: https://docs.openstack.org/image-guide/obtain-images.html
