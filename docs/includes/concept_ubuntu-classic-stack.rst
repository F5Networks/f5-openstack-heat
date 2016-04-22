.. toctree::
    :maxdepth: 2


Ubuntu Classic Stack
====================

Overview
--------
This template deploys a client, device-under-test (DUT), and a server and creates nearly all network plumbing necessary (with the exception of the external network).

First, the template creates three Ubuntu 14.04 instances. Each instance connects to a data network, which is associated with the floating IP for that instance.

Next, the client connects to the DUT via the ``client_test_network``. The server connects to the DUT via the ``server_test_network``.


Multi-homing
------------
All instances in this stack are multi-homed. This is important to know because default Ubuntu cloud images for 14.04 do not support multiple nics out of the box. You can solve these problems by referring to this `cloudify blog <http://getcloudify.org/2015/05/18/openstack-neutron-nova-cloud-vm-networking-network-automation-orchestration.html>`_ regarding a multi-homed instance in OpenStack.

We have solved this problem by using `ifplugd <http://linux.die.net/man/8/ifplugd>`_, a service baked into the image that waits for any and all interfaces to be hotplugged. Cloud-init creates the port on the OpenStack side for this instance to connect to the additional networks and configures the ethernet devices to be available on the instance. It does not, however, bring up the additional interfaces. That's the job of ``ifplugd``, or of your startup script and whatever you choose to use.
