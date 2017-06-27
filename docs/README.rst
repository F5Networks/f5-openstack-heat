F5 Orchestration Templates for OpenStack Heat
=============================================

.. sidebar:: **OpenStack version:**

   |openstack|

.. raw:: html

   <script async defer src="https://f5-openstack-slack.herokuapp.com/slackin.js"></script>

version |release|
-----------------

|release-notes|

F5's orchestration template library for OpenStack Heat (``f5-openstack-heat``) is a set of Heat Orchestration Templates (HOT) that let you deploy and/or configure a BIG-IP device/cluster from your OpenStack cloud.

Guides
------

See the `F5 Integration for OpenStack Heat`_ user documentation.


Heat Orchestration Template index
---------------------------------

The :code:`f5-openstack-heat` template library contains two groups of Heat orchestration templates: F5-supported and Unsupported.


.. _f5-supported-heat:

F5-Supported Heat templates
```````````````````````````

The `F5 support policy for GitHub software`_ applies to the F5-supported templates listed below.

.. toctree::
   :maxdepth: 1
   :glob:

   f5_supported/*

.. _unsupported-heat:

Unsupported Heat templates
``````````````````````````

**The Heat orchestration templates below are not supported by F5.** Use at your own risk.

.. toctree::
   :maxdepth: 1
   :glob:

   unsupported

Configuration
-------------

Each of the F5 Heat orchestration templates accepts a specific set of inputs, as described in the documentation for each template. [#fn1]_

.. _BIG-IP security groups:

.. note:: the *unsupported* template library includes the following templates that set up the required BIG-IP security groups:

   * :fonticon:`fa fa-download` :download:`BIG-IP control security group <../unsupported/ve/common/bigip_control_security_group.yaml>`
   * :fonticon:`fa fa-download` :download:`BIG-IP data security group <../unsupported/ve/common/bigip_data_security_group.yaml>`
   * :fonticon:`fa fa-download` :download:`BIG-IP mgmt security group <../unsupported/ve/common/bigip_mgmt_security_group.yaml>`


F5 Plugins for OpenStack Heat
-----------------------------

Many of the F5-supported Heat templates require the `F5 Plugins for OpenStack Heat`_.
See the F5 Heat plugins documentation for installation instructions.



.. rubric:: Footnotes
.. [#fn1] F5-supported Heat orchestration templates only; unsupported templates are not documented.


.. _F5 support policy for GitHub software: https://support.f5.com/csp/article/K80012344
