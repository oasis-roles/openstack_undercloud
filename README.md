[![Build Status](https://travis-ci.com/oasis-roles/openstack_undercloud.svg?branch=master)](https://travis-ci.com/oasis-roles/openstack_undercloud)

openstack_undercloud
===========

Basic description for openstack_undercloud

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `openstack_undercloud_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `openstack_undercloud_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: openstack_undercloud-servers
  roles:
    - role: oasis_roles.openstack_undercloud
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>
