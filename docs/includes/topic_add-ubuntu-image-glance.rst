:orphan: true

.. _add-ubuntu-image-glance:

Add a Ubuntu image to Glance
````````````````````````````

If you don't already have a Ubuntu image in your OpenStack environment, you'll need to add one to Glance before you can use the template.

1. Copy the download URL for the Ubuntu Cloud server image of your choice. We used `trusty-server-cloudimg-amd64-disk1.img <http://uec-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-disk1.img>`_.

2. Add the image to Glance:

    - In Horizon, go to :guilabel:`Compute` --> :guilabel:`Images`.
    - Click :guilabel:`Create Image` and paste the image URL in the :guilabel:`Image Location` field.
    - Enter the requested information, including the minimum requirements for your image (we used 7GB disk and 520MB RAM).
    - Click :guilabel:`Create` to add the image to Glance.

