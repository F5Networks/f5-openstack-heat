f5_two_ve_resource_group.yaml
#############################

This template deploys the two BIG-IP devices in a OS::Heat::ResourceGroup resource.
This creates two devices that are essentially identical, with the exception of which IP addresses are given to them at bootup time.
If these devices do not need to be identical, feel free to use the same sub template in f5_supported/ve/common, but break the OS::Nova::Instances out here instead of using a ResourceGroup.
