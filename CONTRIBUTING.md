# Contributing to F5-Openstack-Heat

## Branches

The f5-openstack-heat repository contains a develop and master branch. The develop branch is used for ongoing development of heat templates. These templates may be highly active, undergoing many iterations, as they are refined. Criteria for promoting a develop template to a master template will be established by testing guidelines. The master branch is considered *golden* as it offers some assurance of adequate and sufficient testing as defined by the creators of this repository.

## Where Templates Go

### F5 Supported Templates
The *f5_supported* top-level directory contains templates that are tested and vetted by F5 Networks, thus falling under the support of F5 Networks.

### Unsupported Templates
The *unsupported* top-level directory contains templates that are not officially supported by F5 Networks. These templates have not undergone unit/functional/integration testing, and can be considered experimental. With that, if you are unsure where to put your template, this is a good place to start.

### Template Types
Within each of the above directories, sub-directories exist to describe the template type. This describes the overall use of a particular template. If deploying a BigIP Virtual Edition (ve) is the primary goal of the template, one could define a *ve* directory to contain such templates. If unsure where to put a template, create a template type directory that fits with your description of the template, and place it in there.

### Template Filename
For your template filename, please prepend the Openstack HOT Template version to the filename. This should be a direct copy of the value *heat_template_version* contained within your template. An example is '2015-04-30'.

## Commit Template and PR Template
The commit template for this repository is contained in the root directory, named .git-commit-template.txt. Use it when committing.
DO: Added PR Template
