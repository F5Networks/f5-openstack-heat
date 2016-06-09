:orphan: true

.. _topic_before-you-begin:

Before You Begin
================

You will need the following in order to follow this guide:

- Basic understanding of `BIG-IP® system configuration <https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-initial-configuration-12-0-0/2.html#conceptid>`_.

- BIG-IP® LTM® Virtual Edition image file in qcow.zip format; can be any size (ALL, LTM, or LTM_1SLOT). [#]_

- An operational OpenStack |openstack| deployment with `Neutron <http://www.openstack.org/software/releases/kilo/components/neutron>`_ and `Heat <http://www.openstack.org/software/releases/kilo/components/heat>`_ installed. [#]_

- An external network, which has access to the internet, :ref:`configured in Neutron <docs:os-neutron-network-setup>`.

- :ref:`F5 OpenStack Heat Plugins <heatplugins:home>` installed on the Neutron controller. The plugins provide the F5® objects needed to provision BIG-IP® resources in OpenStack.

- :ref:`SSH key(s) <add-ssh-key-horizon>` configured in OpenStack; to be used for authentication to BIG-IP® and/or any client or server instances created by the Heat templates.

- The Heat templates listed below.

    - :download:`patch_upload_ve_image.yaml <../../f5_supported/ve/images/patch_upload_ve_image.yaml>`

    - :download:`f5_ve_standalone_3_nic.yaml <../../f5_supported/ve/standalone/f5_ve_standalone_3_nic.yaml>`

    - :download:`deploy_lb.yaml <../../f5_supported/f5_plugins/deploy_lb.yaml>`


Caveats
-------

- The BIG-IP® VE image must be hosted in a location accessible to the Heat engine via 'http'. The F5® Heat templates do not currently support retrieval of files via 'https' or file uploads.

- VE images come in 3 different sizes: LTM, ALL, and LTM-1SLOT. Each has its own size requirements, which  determine what Nova flavor you should select. See the F5® OpenStack `BIG-IP® flavor matrix <http://f5-openstack-docs.readthedocs.org/en/latest/guides/openstack_big-ip_flavors.html>`_ for more information.

- There is a `known issue <https://bugs.launchpad.net/glance/+bug/1476770>`_ with ``python-glanceclient`` that returns an unspecified error after you click :guilabel:`Launch` to launch a stack from the OpenStack dashboard. You may need to upgrade the package in order to resolve this issue.


.. rubric:: Footnotes:

.. [#] `How to Buy <https://f5.com/products/how-to-buy>`_
.. [#] Unsure how to get started with OpenStack? See the F5® OpenStack :ref:`deployment <docs:os-deploy-guide>` and :ref:`configuration <docs:os-config-guide>` guides.
