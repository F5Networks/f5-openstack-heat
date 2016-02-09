F5 Networks OpenStack Heat Template Library
===========================================

Introduction
------------
OpenStack Heat templates for applications stacks that include F5 BigIP
configurations and templates for deploying F5 VE in an OpenStack cloud.

The two top level directories that exist in this repo which contain Heat
templates are :code:`f5_supported` and :code:`unsupported`.

F5 Supported Templates
~~~~~~~~~~~~~~~~~~~~~~
The :code:`f5_supported` directory contains templates that are officially supported
by F5 Networks for customers with a support contract.  Users who require
support should contact F5 Support through usual means.

.. toctree::
   :maxdepth: 1

   templates/f5_supported/templates

Unsupported Templates
~~~~~~~~~~~~~~~~~~~~~
The :code:`unsupported` directory contains templates that are experimental and should
be used **AT YOUR OWN RISK**.  These templates may have been contributed by
other users or are under development by F5.  Regardless of a customer's status
of a valid support contract, F5 will not support templates that are in this
directory.

.. toctree::
   :maxdepth: 1

   templates/unsupported/templates

Releases and Versions
---------------------
|release| supports the OpenStack |openstack_release| release.

For more information about F5 Networks's OpenStack versioning and support
matrix please see `F5 Networks OpenStack Support Matrix <https://F5Networks.github.io/f5-openstack-docs>`__.

Installation & Configuration
----------------------------
Heat templates can be loaded via the OpenStack Horizon GUI or using the Heat
command line or API.

Some templates may require
`F5Networks/f5-openstack-heat-plugins <https://github.com/F5Networks/f5-openstack-heat-plugins>`__
to be installed.

Contact
-------
Have questions or like to see new templates?  We'd love to hear from you.  You
can email the team at f5_openstack_heat@f5.com, or visit us at
`F5Networks/f5-openstack-heat <https://github.com/F5Networks/f5-openstack-heat>`__.

Copyright
---------
Copyright 2013-2016 F5 Networks Inc.

Support
-------
Maintenance and support of the unmodified F5 code is provided only to customers
who have an existing support contract, purchased separately subject to F5’s
support policies available at http://www.f5.com/about/guidelines-policies/ and
http://askf5.com.  F5 will not provide maintenance and support services of
modified F5 code or code that does not have an existing support contract.

License
-------
Apache V2.0
~~~~~~~~~~~

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See
the License for the specific language governing permissions and limitations
under the License.

Contributor License Agreement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Individuals or business entities who contribute to this project must
have completed and submitted the `F5 Contributor License
Agreement <http://f5networks.github.io/f5-openstack-docs/cla_landing/index.html>`__
to Openstack_CLA@f5.com prior to their code submission being included in this
project.
