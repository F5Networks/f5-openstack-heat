# Contributing guide for  f5-openstack-Heat
If you have found this that means you you want to help us out.  Thanks in
advance for lending a hand! This guide should get you up and running quickly
and make it easy for you to contribute.  If we don't answer your questions here
and you need help or just want to say hi shoot us an email at
<f5_openstack_heat@f5.com>.

## Branches

The f5-openstack-heat repository contains a `develop` and `master` branch. The
`develop` branch is used for ongoing development of heat templates. These
templates may be highly active, undergoing many iterations, as they are
refined. Criteria for promoting a develop template to a master template will be
established by testing guidelines.

The master branch is considered *golden* as it offers some assurance of
adequate and sufficient testing as defined by the creators of this repository.

To contribute to this repository, fork the repository and then clone your fork.
Add the original repository as an upstream remote.

```
git remote add upstream https://github.com/F5Networks/f5-openstack-heat.git
```

Develop locally, pushing to your fork when necessary, and updating from the
upstream repository often. When ready, submit a pull request using the template
below.

## Where Templates Go

### F5 Supported Templates
The `f5_supported` top-level directory contains templates that are tested and
vetted by F5 Networks, thus falling under the support of F5 Networks.

### Unsupported Templates
The `unsupported` top-level directory contains templates that are not
officially supported by F5 Networks. These templates have not undergone
unit/functional/integration testing, and can be considered experimental. With
that, if you are unsure where to put your template, this is a good place to
start.

### Template Types
Within each of the above directories, sub-directories exist to describe the
template type. This describes the overall use of a particular template. If
deploying a BigIP Virtual Edition (VE) is the primary goal of the template,
one could define an `unsupported/ve` directory to contain such templates. If
you are unsure where to put a template, create a template type directory that
fits with your description of the template, and place it in there.

### Template Filename
For your template filename, please prepend the Openstack HOT Template version
to the filename. This should be a direct copy of the value
`heat_template_version` contained within your template. An example is
`2015-04-30`.

## Issues
Creating issues is good, creating good issues is even better.  By filing
meaningful bug reports will lots of information in them helps us figure out
what to fix when and how it impacts our users.  We like bugs because it means
people are using our code, and we like fixing them even more.

* Title: A short but descriptive summary of the issue, whether it be a bug or enhancement.
* Labels: Click on the gear icon and give us some direction on the type of issue you are filing.
* Milestone: Leave this field empty.
* Assignee: If you're not fixing the issue, leave this field empty.
* Details: For bugs, copy and paste the following template into your new issue and fill it out.

```
#### Heat Template
<Fill in the Heat template(s) that you are filing this issue against>

#### Operating System
<Fill in the host OS of the machine running the agent, such as Ubuntu 14.04>

#### OpenStack Release
<Fill in the OpenStack release, such as Kilo>

#### Description
<Describe the bug in detail and the steps taken prior to encountering the issue>

#### Deployment
<Explain in reasonable detail your OpenStack deployment, the F5 OpenStack agent, and BIG-IP(s)>
<Example: Single OpenStack controller with one F5 agent managing a cluster of 4 BIG-IP VEs>
<Example: Three OpenStack controllers in HA, each with one standalone F5 agent managing a single BIG-IP appliance>
```
* Details: For enhancements, copy and paste the following template into your new issue and fill it out.

```
#### Application Stack
<Describe what the heat stack is and what application(s) it contains>

#### Description
<Describe the enhancement request in detail>
```

## Commit Template and PR Template
The commit template for this repository is contained in the root directory,
named .git-commit-template.txt. Use it when committing.

When submitting a pull request please use the following template
```
@<reviewer_id>
#### What issues does this address?
Fixes #<issueid>
WIP #<issueid>
...

#### What's this change do?

#### Where should the reviewer start?

#### Any background context?
```

## License

### Apache V2.0
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 
http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
 
### Contributor License Agreement
Individuals or business entities who contribute to this project must have completed and submitted the [F5 Contributor License Agreement](http://f5-openstack-docs.readthedocs.org/en/latest/cla_landing.html) to Openstack_CLA@f5.com prior to their
code submission being included in this project.
