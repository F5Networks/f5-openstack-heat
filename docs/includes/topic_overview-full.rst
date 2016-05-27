Overview
--------

This guide demonstrates how to use the `OpenStack Heat <https://wiki.openstack.org/wiki/Heat>`_ orchestration service to onboard and deploy F5® BIG-IP® Virtual Edition (VE) via the `OpenStack dashboard <https://wiki.openstack.org/wiki/Horizon>`_ (aka, the GUI). You will need to log in as a user with admin permissions.

The templates covered in this guide are:

- :file:`patch_upload_ve_image.yaml`: makes a VE image OpenStack-ready.

- :file:`f5_ve_standalone_3_nic.yaml`: deploys a standard, standalone BIG-IP® VE that processes application traffic and sends it to a server pool on the BIG-IP®'s internal network.


