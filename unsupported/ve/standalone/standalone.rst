BIG-IP® VE Standalone Templates
===============================

Overview
--------
The BIG-IP® VE Standalone templates deploy a single VE instance, with variations on the number of desired data interfaces.


The standalone templates utilize the same configuration settings as those in the :ref:`Common <ve-common>` directory, such as the security groups and the ``OS::Nova::Server`` resources for VE. Refer to those templates if you'd like to get a better idea of how Heat templates should be composed.

.. note::

    * The license key is a required input parameter if you wish to boot up a licensed VE. The license must include the VE modules you wish to provision.

    * The outputs of these templates give you a programmatic way to retrieve details about the VE.



