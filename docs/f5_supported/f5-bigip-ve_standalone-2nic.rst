.. _ve2nic:

F5 BIG-IP VE: Standalone, 2-nic
===============================

Overview
--------

This template deploys a standalone, 2-nic F5 BIG-IP VE instance in OpenStack.

Prerequisites
-------------

- An external network with access to the internet.
- `F5 Plugins for OpenStack Heat`_ installed on the Neutron controller.
- SSH key(s) configured in OpenStack.
- :ref:`BIG-IP VE image <ve-image-patch-upload>` uploaded to Glance.
- Two (2) VLANs configured in Neutron -- 'mgmt' and 'data' -- to use for system management and data traffic, respectively.

Caveats
-------
- This template requires internet access to fetch dependent Heat templates from GitHub.
  (These add the necessary :ref:`BIG-IP security groups <big-ip security groups>` to OpenStack).
- This template deploys an **unlicensed** BIG-IP VE.
  Add your `BIG-IP license base key`_ when you log in for the first time.
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
                                                            BIG-IP VE instance
------------------------------------------- --------------- --------------------------- ---------------
Use Config Drive                            boolean         Use config drive to provide False
                                                            meta and user data
------------------------------------------- --------------- --------------------------- ---------------
F5 Root SSH Key Name                        string          Choose an ssh key-pair;     N/A
                                                            used for authentication to
                                                            the BIG-IP VE instance
------------------------------------------- --------------- --------------------------- ---------------
External Network                            string          Choose the external network N/A
                                                            from the list
------------------------------------------- --------------- --------------------------- ---------------
VE Management Network                       string          Assign a Neutron subnet     N/A
                                                            to the management interface
                                                            on the BIG-IP VE instances
------------------------------------------- --------------- --------------------------- ---------------
VE Network for the 1.1 Interface            string          Assign a Neutron network    N/A
                                                            to the 1.1 interface on the
                                                            BIG-IP VE instance
------------------------------------------- --------------- --------------------------- ---------------
Name for Network 1.1                        string          Enter a name for the 1.1    network-1.1
                                                            network on the BIG-IP
                                                            VE instance
------------------------------------------- --------------- --------------------------- ---------------
Default Gateway IP                          string          Enter the Gateway IP        none
                                                            address to use for the
                                                            BIG-IP VE instance
=========================================== =============== =========================== ===============


Deployment
----------

See the `F5 HOT deployment instructions`_.

Download
--------

Click the link below to download the template.

:download:`Download </../f5_supported/ve/standalone/f5_ve_standalone_2_nic.yaml>`

