# gi-simplify

## Overview

To respond to the growth and innovation in data networks, CSPs have expanded
existing legacy platforms and added new ones without a holistic view of the
network architecture. In many cases, this has resulted in needlessly complex
networks that cannot readily be scaled, increase deployment and operating costs,
and reduces the ability to add or adapt new services.

Once established in a position to steer traffic to VAS platforms, the BIG-IP
platform enables CSPs to consolidate several incremental network functions to
increase network efficiency and ROI. F5 products provide a number of additional
service functions, including security, translation, processing offloading,
optimisation, and policy enforcement.

The purpose of this solution is to research and demonstrate the use case
scenarios for the F5 PEM, CGNAT modules to simplify the implementation of the
GI infrastructure that is used by ISP nowadays.

## Use cases

  - Traffic steering
  - iCap ad insertion
  - Logging
  - WAP Offload iRule solution
  - X-IMSI insert

## Requirements

This heat template has been deployed on various OpenStack Kilo clouds which use
the reference neutron with OVS networking layer.

Depending on your environment, additional work may be required on your part to
ensure that the template correctly creates the necessary infrastructure.

## Notes

The following should be noted about this template to satisfy any questions on
why various things were done

### Usage of OS::Heat::CloudConfig

These were used to ensure that default users were created on the OpenStack
instances that were booted. Without this, there is no guarantee that known
unprivileged users will be created

### DHCP on all interfaces

This reference solution uses fixed IP addresses. These addresses can only be
served by neutron if DHCP is enabled on the subnet. Note that we deliberately
assign high allocation pools to prevent these static addresses from being
assigned to the DHCP server port.

### Security groups default allow

neutron, by default, will default deny all traffic. If your usage of this
template requires troubleshooting or debugging, we deliberately allow all
traffic to support that effort.

We expect after your troubleshooting efforts are complete that you will change
these security group settings to reasonable defaults.

### Allowed address pairs allowing all

Due to the nature of the BIG-IP product, traffic that is NAT'd sufficiently
may appear to neutron as being spoofed. To disable this feature we specify an
allowed_address_pair of 0.0.0.0/0 on each BIG-IP port. This is also required
if the port-security extension is enabled on your cloud.

If the allowed_address_pairs extension is not enabled, these settings can be
removed.

### OpenStack-ready BIG-IP image

We require that you have an OpenStack-ready BIG-IP image available (version 12.0.0
with the appropriate OpenStack /config/startup script in place)

### Infrastructure only

Our approach to heat templates has been to separate the creation of the
infrastructure from the configuration of that infrastructure. Therefore, in this
template you will only see infrastructure creation.

## License

Copyright 2015 F5 Networks

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
