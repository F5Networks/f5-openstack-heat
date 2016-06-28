:orphan: true

F5-Supported Heat Template Prerequisites
========================================

.. This file is for internal use only. It contains a list of prerequisites that can be reused in the f5-supported heat template documentation as needed.


- Basic understanding of `BIG-IP® system configuration <https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-initial-configuration-12-0-0/2.html#conceptid>`_.


- Basic understanding of `BIG-IP® device service clustering <https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-device-service-clustering-admin-12-0-0.html>`_.


- :ref:`BIG-IP® VE image <F5® BIG-IP® VE: Image Patch & Upload>` uploaded to Glance.


- :ref:`F5 OpenStack Heat Plugins <heatplugins:home>` installed on the Neutron controller.


- :ref:`BIG-IP® Security Groups` configured in OpenStack.


- :ref:`SSH key(s) <add-ssh-key-horizon>` configured in OpenStack; to be used for authentication to the BIG-IP® VE instances launched by this template.


- :ref:`SSH key(s) <add-ssh-key-horizon>` configured in OpenStack; to be used for authentication to the vm instances launched by this template.


- Glance image(s) [#]_ of your choice, to be used for the client and server.


- Two (2) VLANs :ref:`configured in Neutron <docs:os-neutron-network-setup>` -- 'mgmt' and 'data' - to be used for system management and data traffic, respectively.


- Three (3) VLANs :ref:`configured in Neutron <docs:os-neutron-network-setup>` -- 'mgmt', 'control', and 'data' -- to be used for system management, high availability (if desired), and data traffic, respectively.



- At least two (2) VLANs :ref:`configured in Neutron <docs:os-neutron-network-setup>` -- 'mgmt' and 'data' - to be used for BIG-IP® system management and client-server data traffic, respectively.


- An external network with access to the internet.


- Two (2) licensed, operational BIG-IP® devices (hardware or Virtual Edition); both must be connected to the 'control' VLAN.

- Login credentials for user(s) with administrative permissions on BIG-IP® device(s).


- Licensed, operational BIG-IP® hardware or VE.


- BIG-IP® `License base key <https://support.f5.com/kb/en-us/solutions/public/7000/700/sol7752.html>`_.


- BIG-IP® LTM® Virtual Edition image file in qcow.zip format; can be any size (ALL, LTM, or LTM_1SLOT). [#]_

:rubric: Footnotes:
.. [#] :ref:`Adding a Ubuntu Image to Glance <add-ubuntu-image-glance>` contains instructions for uploading an image to Glance via the OpenStack dashboard. You may use the OS of your choice; Ubuntu is not a requirement for this template.
.. [#] `How to Buy <https://f5.com/products/how-to-buy>`_
