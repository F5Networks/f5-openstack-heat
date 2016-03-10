Generating OpenStack Ready VE Images
====================================

Description
-----------
The templates within this directory launch a Heat stack to prepare a VE image for use in OpenStack. The sync_image.yaml template launches an Ubuntu onboarding server that downloads an F5 BigIP VE qcow image, extracts it, if necessary, and patches it. Note, the URL given as the location for that F5 BigIP VE qcow image must be publicly accessible as for now. Once the image is patched, it is uploaded into the OpenStack Glance service you provided as inputs to the Heat template.

Note: the templates currently are pulling an Ubuntu image from ubuntu.com, but you could easily replace that with an Ubuntu that already exists in your stack. After the image is uploaded into Glance, the stack then deletes itself. Please do not modify the 'user_data' script in the 'onboard_instance' resource unless you are certain what you are doing. The script is downloading, extracting, patching, and uploading the F5 image you specified as an input.
