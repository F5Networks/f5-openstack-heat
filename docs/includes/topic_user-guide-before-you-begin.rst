.. _topic_before-you-begin:

Before You Begin
----------------

You will need the following in order to use this guide:

* A functional OpenStack |openstack| deployment with at least one controller node; a physical external network; a client network; and a server network.

    Unsure how to get started with OpenStack? See the F5® OpenStack `Deployment Guide <http://f5-openstack-docs.readthedocs.org/en/latest/guides/os-deploy-guide.html>`_ and `Configuration Guide <http://f5-openstack-docs.readthedocs.org/en/latest/guides/os-config-guide.html>`_.

* A BIG-IP® VE image, v11.5.2 or later. This guide uses BIG-IP® VE 11.6.0 LTM (image filename: :file:`BIGIP-11.6.0.6.0.442.LTM.qcow2.zip`).

    `Buy from f5.com <https://f5.com/products/how-to-buy>`_

* The F5® Heat plugins. These create the BIG-IP® objects used by both Heat and iApp® templates to provision BIG-IP® LTM® resources in OpenStack.

    See the `F5® Heat Plugins <http://f5-openstack-heat-plugins.readthedocs.org/en/>`_ documentation for  installation instructions.

* F5® Heat templates:

    We strongly recommend that you `fork this repo <https://github.com/F5Networks/f5-openstack-heat>`_ and clone it locally. This will give you access to all of the latest F5® Heat templates, as well as make it easy for you to customize them to suit your needs. An alternative is to download the latest `release package <https://github.com/F5Networks/f5-openstack-heat/releases>`_.

    .. code-block:: shell

        $ curl -O -L https://github.com/F5Networks/f5-openstack-heat@v7.0.1

    At minimum, you can download the templates used in this guide:

    :download:`patch_upload_ve_image.yaml <../../f5_supported/ve/images/patch_upload_ve_image.yaml>`

    :download:`f5_ve_standalone_3_nic.yaml <../../f5_supported/ve/standalone/f5_ve_standalone_3_nic.yaml>`





