.. _topic_release-info:

Release Notes
=============

Summary
-------

The current release of the F5 Heat templates, |release|, is compatible with OpenStack |openstack|. See the `F5 OpenStack Releases, Versioning, and Support matrix <http://f5-openstack-docs.readthedocs.org/en/latest/releases_and_versioning.html>`_ for more information, including BIG-IP version compatibility.


Release Highlights
------------------

* The new F5 OpenStack Heat plugin ``F5::Cm::Sync`` is used by the `f5_supported/f5_plugins/active_standby.yaml <https://github.com/F5Networks/f5-openstack-heat/blob/kilo/f5_supported/f5_plugins/active_standby.yaml>`_ template to demonstrate configuration synchronization from one device in the cluster to the entire group.
* The new F5 OpenStack Heat plugin ``F5::Sys::Save`` is used in the same template as above to save the running configuration to the device's disk.

Caveats
-------

None.

Open Issues
-----------

See the [project issues page](https://github.com/F5Networks/f5-openstack-heat/issues) for a full list of open issues.
