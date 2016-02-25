iApps® APIC Integration Template
================================

Overview
--------
This Heat template deploys an iApps® template that can automate and orchestrate Layer 4-7 applications service deployments using F5® BIG-IP®/BIG-IQ® products. Additionally, it can serve as a common integration point for third party SDN/NFV/Automation/Orchestration products.

There are two major components to this deployment. The iApps® template deploys first, then the Heat template creates the service.  When the service is deployed, the Heat template passes in a set of default answers to the choices/questions posed in the APL section of the iApps® template. These answers, which can be in the form of variables, tables, and/or lists, can be altered as needed to suit your needs.

For more information about this iApp and its author, please see `appsvcs_integration_iapp <https://github.com/0xHiteshPatel/appsvcs_integration_iapp>`_ on GitHub.
