f5-openstack-heat
=================

Introduction
------------
OpenStack Heat templates for applications using F5 BigIP and F5 VE deployments.

Supported and Unsupported Templates
-----------------------------------
The two top level directories that exist in this repo which contain Heat
templates are :code:`f5_supported` and :code:`unsupported`.

f5_supported
~~~~~~~~~~~~
The :code:`f5_supported` directory contains templates that are officially supported
by F5 Networks for customers with a support contract.  Users who require
support should contact F5 Support through usual means.

unsupported
~~~~~~~~~~~
The :code:`unsupported` directory contains templates that are experimental and should
be used **AT YOUR OWN RISK**.  These templates may have been contributed by
other users or are under development by F5.  Regardless of a customer's status
of a valid support contract, F5 will not support templates that are in this
directory.

Releases and Versions
---------------------
This branch supports the OpenStack Kilo release.

For more information about F5 Networks's OpenStack versioning and support
matrix please see `F5 Networks OpenStack Support Matrix <https://F5Networks.github.io/f5-openstack-docs>`__.

Installation & Configuration
----------------------------
Heat templates can be loaded via the OpenStack Horizon GUI or using the Heat
command line or API.

Some templates may require
`F5Networks/f5-openstack-heat-plugins <https://github.com/F5Networks/f5-openstack-heat-plugins>`__
to be installed.

Documentation
-------------
Project documentation can be found on `Read The Docs <https://f5-openstack-heat.readthedocs.org>`__

Filing Issues
-------------
If you find an issue we would love to hear about it. Please let us
know by filing an issue in this repository and tell us as much as you can
about what you found and how you found it.

For more information see the Issues section of
`Contributing <CONTRIBUTING.md>`__.

Contributing
------------
See `Contributing <CONTRIBUTING.md>`__

Contact
-------
f5_openstack_heat@f5.com

Copyright
---------
Copyright 2013-2016 F5 Networks Inc.

Support
-------
See `Support <SUPPORT.md>`__

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
Agreement <http://f5-openstack-docs.readthedocs.org/en/latest/cla_landing.html>`__
to Openstack_CLA@f5.com prior to their code submission being included in this
project.
