.. _how-to_onboard-ve:

Onboarding a VE Image in OpenStack
----------------------------------

In order to use a BIG-IP® VE image in OpenStack, it first has to be made 'OpenStack-ready'. The VE image patch template (:file:`patch_upload_ve_image.yaml`) uses a Ubuntu image as a TMOS VE image onboarding server to convert the image for use in OpenStack. You will need to use an SSH key for authentication.

.. seealso::

    :ref:`Add a Ubuntu image to Glance <add-ubuntu-image-glance>`

    :ref:`Add an SSH key to Horizon <add-ssh-key-horizon>`


Import the VE Image
```````````````````

Follow the steps below to launch a Heat stack to import the VE image. Once the VE image appears in :guilabel:`Images`, you can safely delete the stack.

1. In Horizon, go to :guilabel:`Orchestration` --> :guilabel:`Stacks`.

2. Click :guilabel:`Launch Stack`.

3. Choose the :guilabel:`Template File` -- :file:`patch_upload_ve_image.yaml` from its location on your machine, then click :guilabel:`Next`.

    .. note::

        You will not be able to use the template by entering its GitHub URL because GitHub uses https. You must save the file locally and upload it.

4. Next, you will need to provide the necessary information for the Heat engine to build your stack.

    .. list-table:: Configuration Items
        :widths: 30, 30
        :header-rows: 1

        * - Configuration Item
          - Entry/Description
        * - Stack Name
          - big-ip_ve_11.6_LTM
        * - Creation Timeout (minutes)
          - 60
        * - Password for user "admin"
          - <your OpenStack password>
        * - Onboard Ubuntu Image
          - select the image you created
        * - F5 Onboard Server Flavor
          - default: m1.medium
        * - F5 Onboard Server Management Network
          - choose any network from the drop-down
        * - SSH Key
          - select an SSH key pair
        * - Keystone Auth URL
          - enter your Keystone authentication URL; usually, this uses the same IP address at which you log in to Horizon
        * - Image Import Tenant
          - the project into which you want to import the VE image; it will be imported into your current project by default
        * - Image Import User
          - defaults to the user account you are logged in to
        * - Image Import User Password
          - the password for the user into whose account the image will be imported
        * - Image Prep URL
          - automatically populated with the URL of the F5 Networks® image prep GitHub repo
        * - F5 VE Image URL
          - must be a publicly-accessible (i.e., ``http``) URL from which the F5 VE image can be downloaded
        * - F5 VE Image Name
          - the VE file name (e.g., :file:`BIGIP-11.6.0.6.0.442.qcow2`)

5. Click :guilabel:`Launch`.


The Heat engine will create your stack; the status changes to :guilabel:`Create complete` when it is finished.

Caveats
```````

There is a `known issue <https://bugs.launchpad.net/glance/+bug/1476770>`_ with ``python-glanceclient`` that returns in an unspecified error after you click :guilabel:`Launch`. You may need to upgrade in order to resolve this issue.

