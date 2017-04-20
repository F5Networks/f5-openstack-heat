F5 OpenStack Heat Orchestration Templates
=========================================

.. raw:: html

   <script async defer src="https://f5-openstack-slack.herokuapp.com/slackin.js"></script>

version |release|
-----------------

|release-notes|

F5's OpenStack Heat Orchestration Templates (HOT) library (f5-openstack-heat) contains templates that let you deploy and/or configure a BIG-IP device/cluster from your OpenStack cloud.

Guides
------

See the `F5 OpenStack Heat user documentation`_.


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

F5 OpenStack Heat Plugins
-------------------------

Many of the F5-supported Heat templates require the `F5 OpenStack Heat Plugins`_.
See the product documentation for installation instructions.



.. rubric:: Footnotes
.. [#fn1] F5-supported Heat orchestration templates only; unsupported templates are not documented.

.. _F5 OpenStack Heat user documentation: /cloud/openstack/latest/heat
.. _F5 support policy for GitHub software: https://support.f5.com/csp/article/K80012344
