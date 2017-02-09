:orphan: true

OpenStack-Ready BIG-IP VE Images
=================================

Overview
--------
The BIG-IP VE 'OpenStack-Ready' image template(s) can be used to prepare, "patch", a BIG-IP VE image for use in OpenStack. Patching requires kernel modules manipulate the large image, therefore the :file:`patch_upload_ve_image.yaml` template launches an Ubuntu server that downloads a zipped F5 BIG-IP VE qcow image, extracts it, and patches it. The patched image is then uploaded to Glance so it can be used to launch BIG-IP instances.

.. note::

    You must provide a publicly-accessible file location as the URL for the BIG-IP VE qcow image. Internally, for testing, we uploaded the zipped image into OpenStack's Swift service and made it publicly accessible.

.. note::

    Once the image is patched, it is uploaded into the OpenStack Glance service (you'll need to provide as an input in the Heat template). After the image is uploaded into Glance, the stack deletes itself.

.. note::

    The templates currently pull a Ubuntu image from ubuntu.com. You can easily replace this with a Ubuntu that already exists in your stack.


.. warning::

    **Please do not modify the 'user_data' script in the 'onboard_instance' resource**. This script is responsible for making the BIG-IP VE image OpenStack-ready and any changes made can break the process.

