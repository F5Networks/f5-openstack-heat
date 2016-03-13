Heat Composition
================

Description
-----------
The templates within offer examples of how to perform Heat template composition. This is not the only way to do Heat template composition. Refer to the `Openstack Template Composition <http://docs.openstack.org/developer/heat/template_guide/composition.html>` for more information on this way to compose Heat templates. These are specifically using composition and the F5 Heat plugins to stand up a load-balancing scenario. The client issues a curl request to the virtual IP address, and that request is proxied to the backend pool member. Both the client and the server are created in the template, but the underlying private networks they connect to are not. The other important note is that the VE itself is not created in these templates, we are merely interacting with an existing VE.
