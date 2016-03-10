VE Templates
============

Description
-----------
The templates within this directory launch and/or prepare BigIP Virtual Editions(VE). To launch a VE, one must use an OpenStack-Ready VE image. In the directory 'images' here, there are templates to do just that. This operation is done via a heat stack with an onboarding server. For more details, see the documentation within that directory.

The other directories here contain templates to launch different configurations of one or more VEs. There are templates to launch a six-armed VE (that is, six data interfaces) and other for a two-armed deployment. The input paramaters of each should be enough of to customize to your needs.
