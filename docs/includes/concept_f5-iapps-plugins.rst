:orphan: true

.. _f5-heat-plugins:

F5 Heat Plugin Example Templates
=================================

Before You Start
----------------

The ``f5_plugins`` templates require the F5 Heat plugins found in `F5Networks/f5-openstack-heat-plugins <https://github.com/F5Networks/f5-openstack-heat-plugins>`_. See the :ref:`project documentation <heatplugins:home>` for installation instructions.

Overview
--------
The ``f5_plugins`` templates use F5 iApps and Heat templates in tandem to deploy BIG-IP resources in OpenStack. F5's iApps contain specific configuration deployments, represented as executable TCL scripts. Each of these scripts is called an iApps template.

There are two ways to use F5's Heat plugins to deploy iApps templates. The first, demonstrated in :file:`deploy_composite_iapp.yaml` and :file:`F5::Sys::iAppCompositeTemplate`, combines Heat and iApps templates to create an iApps service on a BIG-IP.

The second method is a simple dump of the iApp's full TCL file into the Heat template, as we've done in :file:`F5::Sys::iAppFullTemplate`. Once the template has been created on the BIG-IP, it can be executed to create the iApp Service (``F5::Sys::iAppService``).

We've provided example templates for each supported F5 plugin. Feel free to browse around the repo (`F5Networks/f5-openstack-heat/unsupported/f5_plugins <https://github.com/F5Networks/f5-openstack-heat/tree/kilo/unsupported/f5_plugins>`_); you can fork the project and tweak the parameters and resources to suit your needs.


iApps APIC Integration Template
--------------------------------

This Heat template deploys an iApps template that can automate and orchestrate Layer 4-7 applications service deployments using F5 BIG-IP/BIG-IQ products. Additionally, it can serve as a common integration point for third party SDN/NFV/Automation/Orchestration products.

There are two major components to this deployment. The iApps template deploys first, then the Heat template creates the service.  When the service is deployed, the Heat template passes in a set of default answers to the choices/questions posed in the APL section of the iApps template. These answers, which can be in the form of variables, tables, and/or lists, can be altered as needed to suit your needs.

For more information about this iApp and its author, please see `appsvcs_integration_iapp <https://github.com/0xHiteshPatel/appsvcs_integration_iapp>`_ on GitHub.

Heat Composition
----------------

These templates are examples of how to perform Heat template composition. This is not the only way to do Heat template composition. Refer to the `Openstack Template Composition <http://docs.openstack.org/developer/heat/template_guide/composition.html>` for more information on this way to compose Heat templates. These are specifically using composition and the F5 Heat plugins to stand up a load-balancing scenario. The client issues a curl request to the virtual IP address, and that request is proxied to the backend pool member. Both the client and the server are created in the template, but the underlying private networks they connect to are not. The other important note is that the VE itself is not created in these templates, we are merely interacting with an existing VE.

