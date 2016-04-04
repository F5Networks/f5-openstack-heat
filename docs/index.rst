F5 Networks® OpenStack Heat Template Library
============================================

.. raw:: html

    <script async defer src="https://f5-openstack-slack.herokuapp.com/slackin.js"></script>

.. toctree::
    :hidden:
    :maxdepth: 2

    f5-supported/f5-supported-index
    unsupported/unsupported-index

Introduction
------------
The F5® OpenStack Heat template library contains templates that can be used to deploy and/or configure F5® BIG-IP® in an OpenStack cloud.

The library contains two groups of templates:

* :ref:`F5® Supported <f5-supported_home>`
* :ref:`Unsupported <unsupported_home>`

Releases and Versions
---------------------
Release v |release| supports the OpenStack |openstack| release.

For more information regarding releases and versioning, please see the `Release, Versioning, and Support Matrix <http://f5-openstack-docs.readthedocs.org/en/latest/releases_and_versioning.html>`_.

.. include:: ../f5_supported/README.rst

.. include:: ../unsupported/README.rst

Installation & Configuration
----------------------------
Any of F5®'s Heat templates can be downloaded, copied, and/or modified as needed to deploy resources in OpenStack.

Heat templates can be loaded via the OpenStack Horizon GUI, the Heat command line, or API. Please see the `OpenStack Heat documentation <http://docs.openstack.org/developer/heat/#using-heat>`_ for usage instructions.

.. note::

    Many of the templates require the F5® Heat plugins to be installed.
    Please see the `documentation <http://f5-openstack-heat-plugins.readthedocs.org/en/latest/>`_ for instructions.


Copyright
---------
Copyright 2013-2016 F5 Networks Inc.

Support
-------
.. include:: ../SUPPORT.md

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
