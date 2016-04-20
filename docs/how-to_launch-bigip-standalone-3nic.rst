.. _how-to_launch-standalone-bigip-3nic:

Launch a Standalone, 3-NIC BIG-IP® VE Using Heat
------------------------------------------------

The standalone, 3-nic deployment template uses an existing BIG-IP® VE image to launch and configure a standalone VE. This template requires an external (physical) network and two internal networks (ours are called 'client' and 'server'). The BIG-IP® receives a floating IP address from the external network; traffic from the client and server networks passes through the BIG-IP®, allowing `LTM® <https://www.f5.com/pdf/products/big-ip-local-traffic-manager-ds.pdf>`_ services to be applied. The client and server networks do not need to be able to communicate with each other; they just need to be able to communicate with the BIG-IP®.

Deploy BIG-IP® VE using the standalone, 3-nic template
``````````````````````````````````````````````````````

1. In Horizon, go to :guilabel:`Orchestration` --> :guilabel:`Stacks`.

2. Click :guilabel:`Launch Stack`.

3. Choose the :guilabel:`Template File` -- :file:`f5_ve_standalone_3_nics.yaml` -- from its location on your machine, then click :guilabel:`Next`.

    .. note::

        You will not be able to use the template by entering its GitHub URL because GitHub uses https. You must save the file locally and upload it.

4. Next, you will need to provide the necessary information for the Heat engine to build your stack. You can use the table below as a worksheet to gather all of the necessary information ahead of time.


    .. list-table:: Configuration Items
        :widths: 30, 30
        :header-rows: 1

        * - Configuration Item
          - Entry/Description
        * - Stack Name
          - big-ip_ve_standalone_3_nic
        * - Creation Timeout (minutes)
          - 60
        * - Password for user "admin"
          - <your OpenStack password>
        * - F5 VE Image
          - select the VE image
        * - F5 VE Flavor
          - select the appropriate flavor (default is m1.medium)
        * - F5 FW Root SSH Key Name
          - select the appropriate SSH key
        * - F5 VE Admin User Password
          - <VE password for admin user>
        * - F5 VE Root User Password
          - <VE password for root user>
        * - Primary VE License Base Key
          - the license Base Key sent to you by F5 support
        * - External Network Name
          - select the external network
        * - VE Management Network
          - select the name of the management network to be used by the VE
        * - VE Network for the 1.1 Interface
          - select an internal network (e.g., client)
        * - VE Network Name for the 1.1 Interface
          - enter a name for the network (e.g., 'network-1.1')
        * - VE Network for the 1.2 Interface
          - select an internal network (e.g., server)
        * - VE Network Name for the 1.2 Interface
          - enter a name for the network (e.g., 'network-1.2')
        * - Default Gateway IP
          - enter the IP address of your physical network's default gateway (if applicable)

5. Click :guilabel:`Launch`. The Heat engine then creates your stack; the status changes to :guilabel:`Create complete` when it is finished.

Caveats
```````

VE images come in 3 different sizes: LTM, ALL, and 1SLOT. Each has its own size requirements; see the F5® OpenStack `BIG-IP® flavor matrix <http://f5-openstack-docs.readthedocs.org/en/latest/guides/openstack_big-ip_flavors.html>`_ for more information. To create a new image in Horizon, go to :guilabel:`System` --> :guilabel:`Flavors` and click :guilabel:`Create Flavor`.




.. the following items are being removed from the template:
    * - HTTP proxy Host to use to acquire resources
      - ???
    * - HTTP proxy Port to use to acquire resources
      - default is 8080
    * - HTTP Proxy Script URL for F5 License Client
      - ???
    * - License Activation Host
      - ???
    * - License Activation Port
      - default is 443
