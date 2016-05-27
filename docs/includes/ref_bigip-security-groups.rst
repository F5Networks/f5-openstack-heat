BIG-IP® Security Groups
=======================

The following Heat templates can be used to deploy security groups in OpenStack that have the necessary settings to allow traffic to reach your BIG-IP®. These security groups correspond to the control, data, and management networks commonly used with BIG-IP®.

Control Security Group
----------------------

This security group applies to the 'control' network used for high availability and mirroring. All devices in a device service cluster must be connected to the same 'control', or 'HA', network to use high availability features.

:download:`Download <../../unsupported/ve/common/bigip_control_security_group.yaml>`


Data Security Group
-------------------

This security group contains the necessary configurations for passing traffic to BIG-IP® data interfaces (e.g., '1.1', '1.2', '1.3').

:download:`Download <../../unsupported/ve/common/bigip_data_security_group.yaml>`


Managment Security Group
------------------------

This security group sets up the necessary configurations to allow incoming and outgoing traffic on the BIG-IP® management interface, which is dedicated to performing a specific set of system management functions.

:download:`Download <../../unsupported/ve/common/bigip_mgmt_security_group.yaml>`

.. seealso::

    * `Introduction to BIG-IP® System Interfaces (v12.0.0) <https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/tmos-routing-administration-12-0-0/3.html?sr=54703143>`_


