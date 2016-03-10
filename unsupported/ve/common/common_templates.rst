Common Template Resources
=========================

Description
-----------
The templates in this directory are often used by other templates to compose a customized stack. For example, the security group templates (such as bigip_data_security_group.yaml) here are pulled in by the standalone templates in the following manner:

    resources:
      bigip_data_security_group:
        type: https://raw.githubusercontent.com/F5Networks/F5Networks/f5-openstack-heat/develop/unsupported/ve/common/bigip_data_security_group.yaml

And once brought into the parent template in this manner, they can be referred to in the sub-template like so:

    resources:
      network_1_port:
        type: OS::Neutron::Port
        properties:
          network: {get_param: network_1 }
          security_groups:
            - bigip_data_security_group

This means that the sub-templates may have parameter and resource dependecies that are given to them via the calling template. When in doubt about what needs to be imported to make a sub-template work, you can review a simple parent template such as those in ../standalone/. This is called template composition, and if you'd like more information on the process go to `Openstack's documentation <http://docs.openstack.org/developer/heat/template_guide/composition.html>`.

The templates here named 'f5_ve_standalone_X_nic.yaml' are the ones described the OS::Nova::Instance for creating a single VE resource. The variations are only among the number of data interfaces that instance will have. Do not modify these templates unless you know what you are doing.
