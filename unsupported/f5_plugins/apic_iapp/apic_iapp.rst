APIC Iapp
=========

Description
-----------
This purpose of this Heat template is to deploy an iApp template that can be used to automate and orchestrate Layer 4-7 applications service deployments using F5 Networks BIG-IP/BIG-IQ Products. Additionally, this iApp serves as a common integration point for third party SDN/NFV/Automation/Orchestration products. There are two major components to this deployment. The iApp template is deployed first, then the service is created using template. When the service is deployed, the Heat template passes in 'answers' to the choices/questions posed in the APL section of the template. These answers come in three fields: variables, tables, and lists. The Heat stack here deploys that service using a default set of answers. This may not be suited for your needs, but you can feel free to modify those answers to customize your deployment. For more information about this Aapp and its creator, refer to `appsvcs_integration_iapp <https://github.com/0xHiteshPatel/appsvcs_integration_iapp>`.
