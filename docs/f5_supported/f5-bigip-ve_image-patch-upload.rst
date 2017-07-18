.. _ve-image-patch-upload:

F5 BIG-IP Virtual Edition: Image Patch & Upload
===============================================

Overview
--------

This template prepares a BIG-IP Virtual Edition (VE) image for use in OpenStack and imports the patched image to `Glance`_.
The template does the following:

#. launches an Ubuntu server;
#. downloads the BIG-IP VE image from the specified URL to the onboarding server;
#. patches the image for use in OpenStack;
#. uploads the patched BIG-IP VE image to Glance.

Prerequisites
-------------

- An external network with access to the internet.
- BIG-IP Virtual Edition image file in qcow.zip format.
- BIG-IP license provisioned appropriately for your environment. [#fn1]_
- `F5 Plugins for OpenStack Heat`_ installed on the Neutron controller.
- Ubuntu image imported to Glance. [#fn2]_
- SSH key configured in OpenStack.
- One (1) VLAN configured in Neutron; must have access to the external network.
  The onboarding server uses this network connection to import the BIG-IP VE image.

Caveats
-------

- The Heat engine cannot retrieve image files via 'https'; for this template, image file uploads are not supported.
  The BIG-IP image must be in a location accessible to the Heat engine via 'http'.
- `BIG-IP VE images come in different sizes`_.
  The `Nova compute flavor`_ you should use for your image depends on the image's disk size requirements.
  See the F5 OpenStack `BIG-IP flavor matrix`_ for more information.

.. tip::

   If you see an unspecified error after launching this template in OpenStack Horizon, see `OpenStack bug id 1476770 <https://bugs.launchpad.net/glance/+bug/1476770>`_.

Configuration Parameters
------------------------

=========================================== =============== =========================== ===============
Parameter                                   Type            Description                 Default
=========================================== =============== =========================== ===============
Onboard Ubuntu Image [#fn3]_                string          An Ubuntu image to          N/A
                                                            use for the onboarding
                                                            server
------------------------------------------- --------------- --------------------------- ---------------
F5 Onboard Server Flavor                    string          `Nova compute flavor`_      m1.medium
                                                            for the onboarding server
------------------------------------------- --------------- --------------------------- ---------------
Use Config Drive                            boolean         Use config drive to provide False
                                                            meta and user data to the
                                                            orchestration instance
------------------------------------------- --------------- --------------------------- ---------------
F5 Onboard Server Management Network        string          Network you want to attach  N/A
                                                            the onboarding server to;
                                                            must have access to the
                                                            internet
------------------------------------------- --------------- --------------------------- ---------------
Keystone Auth URL                           string          Keystone Authentication URL N/A
------------------------------------------- --------------- --------------------------- ---------------
Image Import Tenant                         string          OpenStack project you want  admin
                                                            to import the image to
------------------------------------------- --------------- --------------------------- ---------------
Image Import User                           string          User account you want to    admin
                                                            import the image to
------------------------------------------- --------------- --------------------------- ---------------
Image Prep URL                              string          F5Networks GitHub repo      DO NOT CHANGE
                                                            where the image prep tools  THIS SETTING
                                                            reside
------------------------------------------- --------------- --------------------------- ---------------
F5 VE Image URL                             string          URL for the BIG-IP VE image N/A
                                                            (**must use http**)
------------------------------------------- --------------- --------------------------- ---------------
F5 VE Image Name                            string          Name of the BIG-IP VE       N/A
                                                            image in the qcow.zip file

                                                            example:
                                                            BIGIP-11.6.0.6.0.442.qcow2
------------------------------------------- --------------- --------------------------- ---------------
SSH Key                                     string          SSH Key to use for          N/A
                                                            authentication to the
                                                            onboarding server
------------------------------------------- --------------- --------------------------- ---------------
Apt-cache URL [#fn4]_                       string          URL for your local          None
                                                            apt-cache proxy
=========================================== =============== =========================== ===============

Deployment
----------

See the `F5 HOT deployment instructions`_.

Download
--------

Click the link below to download the template.

:download:`Download </../f5_supported/ve/images/patch_upload_ve_image.yaml>`

.. rubric:: Footnotes
.. [#fn1] See `Simplified Licensing <https://f5.com/products/how-to-buy/simplified-licensing>`_.
.. [#fn2] See the `OpenStack Virtual Machine Image Guide <https://docs.openstack.org/image-guide/obtain-images.html>`_ for more information.
.. [#fn3] Import the image to Glance before you launch this template.
.. [#fn4] Used by the F5 OpenStack development team for testing.

.. _Glance: https://docs.openstack.org/developer/glance/

