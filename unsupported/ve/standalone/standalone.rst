VE Standalone Templates
=======================

Description
-----------
The templates in this directory are those that deploy a single VE instance with variations only upon the number of data interfaces desired. These templates are composed of templates in the ../common/ directory such as the security groups and the OS::Nova::Server resources for the VE itself. Refer to those templates if you'd like to get a better idea of how template composition is done in Heat. Note that the license key is required as an input parameter to boot up a licensed VE. The license itself must be applicable for the modules you wish to have provisioned on the VE. The outputs of these templates give you a programmatic way to retrieve details about the VE launched by this stack.
