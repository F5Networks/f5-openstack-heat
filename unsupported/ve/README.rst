.. _ve_home:

VE Templates
============

Overview
--------

The templates within the VE directory can be used to prepare BIG-IP® Virtual Edition (VE) images for use and to launch VE in OpenStack clouds.

Before you can launch a VE in OpenStack, the image must be converted to make it 'OpenStack-Ready'. We've created templates in the 'images' directory which do just that. The operation is done via a heat stack with an onboarding server. For further details, see :ref:`Images <images_home>`.

The ``/common`` and ``/standalone`` directories contain templates via which you can launch different configurations of one or more VEs. There are templates to launch a six-armed VE (that is, six data interfaces) and other for a two-armed deployment. The input paramaters included for each should be enough to get started and customize the deployment to meet your needs.

