Gi Network Simplification Solution
==================================

Overview
--------

To respond to the growth and innovation in data networks, Cloud Service Providers (CSPs) have
expanded existing legacy platforms and added new ones without a holistic view of the network architecture. In many cases, this results in needlessly complex networks that are not readily scalable; increase deployment and operating costs; and reduce the ability to add or adapt new services.

Once established in a position to steer traffic to value-added service (VAS) platforms, BIG-IP® enables CSPs to consolidate several incremental network functions to increase network efficiency and ROI. F5® products provide a number of additional service functions, including security, translation, processing offloading, optimisation, and policy enforcement.

The purpose of this solution is to research and demonstrate the use case scenarios for the F5® BIG-IP® `PEM™ <https://f5.com/products/service-provider-products/policy-enforcement-manager>`_ and `CGNAT <https://f5.com/products/service-provider-products/carrier-grade-nat>`_ modules to simplify the implementation of the Gi infrastructure used by ISPs. For more information, please see F5®'s `S/Gi Network Simplification <https://f5.com/solutions/service-provider/reference-architectures/s-gi-network-simplification>`_ reference architecture.

Use cases
---------

-  Traffic steering
-  iCap ad insertion
-  Logging
-  WAP Offload iRule solution
-  X-IMSI insert

Requirements
------------

This heat template can be deployed on OpenStack Kilo clouds, using Neutron configured with the OVS networking layer. Depending on your environment, additional work may be required on your part to ensure that the template correctly creates the necessary infrastructure.

OpenStack-ready BIG-IP® image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use of this template requires an OpenStack-ready BIG-IP® image (version 12.0.0) with the appropriate OpenStack /config/startup script in place. For more information or to acquire an OpenStack-ready image, **please contact your F5® Support representative**.

Notes
-----

Usage of ``OS::Heat::CloudConfig``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This ensures that default users without admin priviliges are created on the booted
OpenStack instances. Otherwise, there is no guarantee that known unprivileged users will be created.

DHCP on all interfaces
~~~~~~~~~~~~~~~~~~~~~~
This reference solution uses fixed IP addresses. These addresses can only be served by Neutron if DHCP is enabled on the subnet. We deliberately assign high allocation pools to prevent these static addresses from being assigned to the DHCP server port.

Security groups default allow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Neutron, by default, denies all traffic. In this template, we deliberately allow all traffic to support troubleshooting and/or debugging efforts. When troubleshooting efforts are complete, be sure to **change the security group settings** to reasonable defaults.

Allowed address pairs allowing all
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Due to the nature of the BIG-IP®, traffic that is NAT'd sufficiently may appear to Neutron as being spoofed. To disable this feature, we specify an ``allowed_address_pair`` of 0.0.0.0/0 on each BIG-IP® port. This is also required if the port-security extension is enabled on your cloud. If the ``allowed_address_pair`` extension is not enabled, these settings can be removed.

Infrastructure only
~~~~~~~~~~~~~~~~~~~
Our approach to heat templates has been to separate the creation of the infrastructure from the configuration of that infrastructure. Therefore, in this template you will **only** see infrastructure creation.

License
-------

Apache V2.0
~~~~~~~~~~~
Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Copyright
---------
Copyright 2015-2016, F5 Networks