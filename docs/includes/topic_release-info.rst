.. _topic_release-info:

Release
-------

The current release of the F5® Heat templates, |release|, is compatible with OpenStack |openstack|. See the `F5® OpenStack Releases, Versioning, and Support matrix <http://f5-openstack-docs.readthedocs.org/en/latest/releases_and_versioning.html>`_ for more information, including BIG-IP® version compatibility.

Summary
-------

Release |release| adds support for three Heat templates:

* f5_supported/ve/images/patch_upload_ve_image.yaml -- prepares a user-supplied BIG-IP® VE image for booting in Openstack
* f5_supported/ve/standalone/f5_ve_standalone_2_nic.yaml -- boots a prepared VE image attached to a single management network and a single data network
* f5_supported/ve/standalone/f5_ve_standalone_3_nic.yaml -- boots a prepared VE image attached to a single management network and two data networks (i.e., client and server networks)

Please see the :ref:`User Guide <heat-user-guide>` for usage instructions.

Release Highlights
------------------

* Each template contains a 'description' section which indicates its basic usage.
* The 'parameters' section of each template indicates what prerequisite resources are needed to launch that particular template.

Caveats
-------

* The security groups being used by the standalone templates have not yet been promoted to supported.
* There is a `known issue <https://bugs.launchpad.net/glance/+bug/1476770>`_ with ``python-glanceclient`` that returns an unspecified error after you launch a stack. You may need to upgrade in order to resolve this issue.

Open Issues
-----------

See the [project issues page](https://github.com/F5Networks/f5-openstack-heat/issues) for a full list of open issues.
