Unsupported Heat Templates
==========================

.. warning::

   Unsupported templates are experimental and should be used **AT YOUR OWN RISK**.

   These templates may be under development by F5 or may have been contributed by other users (non-F5-employees).

   F5 will not support templates that are in the unsupported state, regardless of a customer's support contract status.

F5 plugins
----------

The ``f5_plugins`` templates use F5 iApps and Heat templates in tandem to deploy BIG-IP resources in OpenStack.

* :download:`iapp_apic_service.yaml </../unsupported/f5_plugins/apic_iapp/iapp_apic_service.yaml>`
* :download:`iapp_client.yaml <../unsupported/f5_plugins/heat_composition/iapp_client.yaml>`
* :download:`iapp_env.yaml <../unsupported/f5_plugins/heat_composition/iapp_env.yaml>`
* :download:`iapp_lb_deploy.yaml <../unsupported/f5_plugins/heat_composition/iapp_lb_deploy.yaml>`
* :download:`deploy_composite_iapp.yaml <../unsupported/f5_plugins/deploy_composite_iapp.yaml>`
* :download:`deploy_composite_iapp_with_get_file_answers.yaml <../unsupported/f5_plugins/deploy_composite_iapp_with_get_file_answers.yaml>`
* :download:`pool.yaml <../unsupported/f5_plugins/pool.yaml>`
* :download:`virtual_server.yaml <../unsupported/f5_plugins/virtual_server.yaml>`

Learning stacks
---------------

If you're just starting out with OpenStack Heat, you can use the Learning Stacks template(s) to get an idea of how a Heat stack manages resources.

* :download:`ubuntu_classic_stack.yaml <../unsupported/learning_stacks/ubuntu_classic_stack.yaml>`

VE
--

The ``ve`` templates prepare BIG-IP Virtual Edition (VE) images for use and launch VE instances in OpenStack.

Common
``````

These templates are primarily used by other Heat templates to compose customized stacks.

* :download:`bigip_control_security_group.yaml <../unsupported/ve/common/bigip_control_security_group.yaml>`
* :download:`bigip_data_security_group.yaml <../unsupported/ve/common/bigip_data_security_group.yaml>`
* :download:`bigip_mgmt_security_group.yaml <../unsupported/ve/common/bigip_mgmt_security_group.yaml>`
* :download:`f5_ve_standalone_4_nic.yaml <../unsupported/ve/common/f5_ve_standalone_4_nic.yaml>`
* :download:`f5_ve_standalone_5_nic.yaml <../unsupported/ve/common/f5_ve_standalone_5_nic.yaml>`
* :download:`f5_ve_standalone_6_nic.yaml <../unsupported/ve/common/f5_ve_standalone_6_nic.yaml>`
* :download:`f5_ve_standalone_7_nic.yaml <../unsupported/ve/common/f5_ve_standalone_7_nic.yaml>`
* :download:`f5_ve_standalone_8_nic.yaml <../unsupported/ve/common/f5_ve_standalone_8_nic.yaml>`
* :download:`f5_ve_standalone_9_nic.yaml <../unsupported/ve/common/f5_ve_standalone_9_nic.yaml>`
* :download:`f5_ve_standalone_10_nic.yaml <../unsupported/ve/common/f5_ve_standalone_10_nic.yaml>`

Standalone
----------

Each of the BIG-IP VE Standalone templates deploys a single VE instance; only the number of data interfaces differs.

* :download:`f5_base_instance_deploy_4_nic.yaml <../unsupported/ve/standalone/f5_base_instance_deploy_4_nic.yaml>`
* :download:`f5_base_instance_deploy_5_nic.yaml <../unsupported/ve/standalone/f5_base_instance_deploy_4_nic.yaml>`
* :download:`f5_base_instance_deploy_6_nic.yaml <../unsupported/ve/standalone/f5_base_instance_deploy_4_nic.yaml>`
* :download:`f5_base_instance_deploy_7_nic.yaml <../unsupported/ve/standalone/f5_base_instance_deploy_4_nic.yaml>`
* :download:`f5_base_instance_deploy_8_nic.yaml <../unsupported/ve/standalone/f5_base_instance_deploy_4_nic.yaml>`
* :download:`f5_base_instance_deploy_9_nic.yaml <../unsupported/ve/standalone/f5_base_instance_deploy_4_nic.yaml>`
* :download:`f5_base_instance_deploy_10_nic.yaml <../unsupported/ve/standalone/f5_base_instance_deploy_4_nic.yaml>`

