.. _home:

F5 Networks OpenStack Heat Template Library
===========================================

.. raw:: html

    <script async defer src="https://f5-openstack-slack.herokuapp.com/slackin.js"></script>

Overview
--------

The F5 OpenStack Heat template library contains templates that can be used to deploy and/or configure BIG-IP from within an OpenStack cloud.

The library contains two groups of templates:

* :ref:`F5-supported <f5-supported_home>`
* :ref:`Unsupported <unsupported_home>`

Releases and Versions
---------------------

Release |release| supports the OpenStack |openstack| release.

For more information regarding releases and versioning, please see the `Release, Versioning, and Support Matrix <http://f5-openstack-docs.readthedocs.org/en/latest/releases_and_versioning.html>`_.

Use
---

Any of F5's Heat templates can be downloaded, copied, and/or modified as needed to deploy resources in OpenStack.

Heat templates can be loaded via the OpenStack GUI, command line, or API. Please see the `OpenStack Heat documentation <http://docs.openstack.org/developer/heat/#using-heat>`_ for instructions.

.. note::

    Many of the templates require the F5 Heat plugins to be installed.
    Please see the :ref:`project documentation <heatplugins:home>` for instructions.


Support
-------

.. include:: ../SUPPORT.md


Contents
--------

.. toctree::
    :maxdepth: 2
    :glob:

    User Guide <map_heat-user-guide>
    Release Notes <release-notes>
    templates/templates_index
