f5-openstack-heat
=================

|Docs build| |slack badge|

Introduction
------------
This repo contains OpenStack `Heat <https://wiki.openstack.org/wiki/Heat>`_ templates that can be used to deploy and/or configure F5® BIG-IP® in an
OpenStack cloud.

Supported and Unsupported Templates
-----------------------------------
The two top-level directories in this repo which contain Heat templates are :code:`f5_supported` and :code:`unsupported`.

f5_supported
~~~~~~~~~~~~
The :code:`f5_supported` directory contains templates that are officially supported by F5 Networks® for customers with a support contract. Users who require support should contact F5® Support via their usual means.

unsupported
~~~~~~~~~~~
The :code:`unsupported` directory contains templates that are experimental and should be used **AT YOUR OWN RISK**. These templates may have been contributed by other users or are under development by F5®. Regardless of a customer's status of a valid support contract, F5® will not support templates that are in this directory.

Documentation
-------------
Documentation for this project is on `Read The Docs <https://f5-openstack-heat.rtfd.org/en>`_.

Releases and Versions
---------------------
This branch supports the OpenStack Kilo release.

For more information regarding releases and versioning, please see the `Release, Versioning, and Support Matrix <http://f5-openstack-docs.readthedocs.org/en/latest/releases_and_versioning.html>`_.

Installation & Configuration
----------------------------
Any of the templates in this repo can be downloaded, copied, and/or modified as needed to deploy resources in OpenStack. Please see the `documentation <https://f5-openstack-heat.rtfd.org/en>`_ for installation, configuration, and usage instructions.

Filing Issues
-------------
If you find an issue, we would love to hear about it. Please let us
know by filing an issue in this repository and tell us as much as you can
about what you found and how you found it.

For more information see the Issues section of
`Contributing <CONTRIBUTING.md>`_.

Contributing
------------
See `Contributing <CONTRIBUTING.md>`_.


Copyright
---------
Copyright 2013-2016 F5 Networks Inc.

Support
-------
See `Support <SUPPORT.md>`_.

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
Individuals or business entities who contribute to this project must have completed and submitted the `F5® Contributor License Agreement <http://f5-openstack-docs.readthedocs.org/en/latest/cla_landing.html>`_ to Openstack_CLA@f5.com prior to their code submission being included in this project.

.. |Docs build| image:: http://readthedocs.org/projects/f5-openstack-heat/badge/?version=latest
    :target: http://f5-openstack-heat.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

.. |slack badge| image:: https://f5-openstack-slack.herokuapp.com/badge.svg
    :target: https://f5-openstack-slack.herokuapp.com/
    :alt: Slack
