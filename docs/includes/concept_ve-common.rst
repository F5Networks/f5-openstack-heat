:orphan: true

.. _ve-common:

BIG-IP VE Common Template Resources
====================================

Overview
--------
The templates in this directory are often used by other templates to compose a customized stack. For example, the security group templates (such as bigip_data_security_group.yaml) here are pulled in by the standalone templates in the following manner:

.. code-block:: text

    resources:
      bigip_data_security_group:
        type: https://raw.githubusercontent.com/F5Networks/F5Networks/f5-openstack-heat/master/unsupported/ve/common/bigip_data_security_group.yaml


And once brought into the parent template in this manner, they can be referred to in the sub-template like so:

.. code-block:: text

    resources:
      network_1_port:
        type: OS::Neutron::Port
        properties:
          network: {get_param: network_1 }
          security_groups:
            - bigip_data_security_group


This means that the sub-templates may have parameter and resource dependencies that are assigned by the calling template. When in doubt about what needs to be imported to make a sub-template work, you can review a simple parent template such as those in :ref:`Standalone <ve-standalone>`. This is called template composition. If you'd like more information on the composition process, see `Openstack's documentation <http://docs.openstack.org/developer/heat/template_guide/composition.html>`.

The templates here named :file:`f5_ve_standalone_*_nic.yaml` contain the ``OS::Nova::Instance`` configuration for creating a single VE resource. The numeric variation indicates the number of data interfaces that instance will have.


.. warning::

    Do not modify these templates unless you've had experience both with Heat and complex network configurations.


