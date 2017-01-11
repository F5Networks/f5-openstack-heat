Overview
--------

This guide demonstrates how to use the `OpenStack Heat <https://wiki.openstack.org/wiki/Heat>`_ orchestration service to onboard; deploy; and provision services on an F5 BIG-IP Virtual Edition (VE) via the `OpenStack dashboard <https://wiki.openstack.org/wiki/Horizon>`_ (aka, the GUI).

The following :ref:`F5-Supported <f5-supported_home>` Heat templates are used in this guide:

- :file:`patch_upload_ve_image.yaml`: uploads an OpenStack-ready BIG-IP VE image to Glance.

- :file:`f5_ve_standalone_3_nic.yaml`: uses the VE image to deploy a standalone BIG-IP VE.

- :file:`deploy-lb`: deploys a simple load balancer on the VE


