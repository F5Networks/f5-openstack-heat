F5 Heat Plugin Example Templates
================================

Before You Start
----------------

The f5_plugins templates require the F5 Heat plugins found in `F5Networks/f5-openstack-heat-plugins <https://github.com/F5Networks/f5-openstack-heat-plugins>`_. The repo's readme contains instructions for deploying the plugins in your own OpenStack.

Overview
--------
The f5_plugins templates demonstrate using F5® iApps® and Heat templates in tandem to deploy resources in OpenStack. F5's iApps® contain specific configuration deployments, represented as executable TCL scripts. Each of these scripts is called an iApps® template.

There are two ways to use F5's Heat plugins to deploy iApps® templates. The first is demonstrated in :file:`deploy_composite_iapp.yaml` / :file:`F5::Sys::iAppCompositeTemplate`. This combination of Heat and iApps templates uses an ``F5::Sys::iAppCompositeTemplate`` and ``F5::Sys::iAppService`` Heat resource to create an iApps® service on the BIG-IP®.

The second method is a simple dump of the iApp's full TCL file into the Heat template, as we've done in :file:`F5::Sys::iAppFullTemplate`. Once the template has been created on the BIG-IP®, it can be executed to create the iApp Service (``F5::Sys::iAppService``).

We've provided example templates for each supported F5 plugin. Feel free to browse around the repo (`F5Networks/f5-openstack-heat/unsupported/f5_plugins <https://github.com/F5Networks/f5-openstack-heat/tree/develop/unsupported/f5_plugins>`_); you can fork the project and tweak the parameters and resources to suit your needs.

