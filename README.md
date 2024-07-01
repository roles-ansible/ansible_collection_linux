[![collection l3d.linux](https://ansible.l3d.space/svg/l3d.linux_ansible-collection_collection.svg)](https://galaxy.ansible.com/ui/repo/published/l3d.linux/)
[![Maintainance](https://ansible.l3d.space/svg/l3d.linux_maintainance_collection.svg)](https://ansible.l3d.space/#l3d.linux)
[![License](https://ansible.l3d.space/svg/l3d.linux_license_collection.svg)](LICENSE)

 Ansible Collection - l3d.linux
============================

This is the Ansible Collection ``l3d.linux``. A collection to to common linux tasks like installing linux packages.

## Ansible Roles in l3d.linux
- [![l3d.linux.packages](https://ansible.l3d.space/svg/l3d.linux.packages_ansible-role.svg)](https://github.com/roles-ansible/ansible_role_packages.git) -  Ansible role to install some base packages on your linux systems

## Using this Collection
You can install the collection using ansible-galaxy by running:
```bash
ansible-galaxy collection install l3d.linux:1.1.1
```

Remember you can to Upgrade to the latest version of the l3d.linux collection using the ``--upgrade`` parameter:
```bash
ansible-galaxy collection install l3d.linux --upgrade
```


Or you could clone this collection in your local ansible project for example to ``collections/ansible_collections/l3d.linux/``. Make sure you checkout [git submodules](https://git-scm.com/docs/git-submodule) too. Example:
```
# Clone git Repo with submodules to specified path
git clone --recursive https://github.com/roles-ansible/ansible_collection_linux.git collections/ansible_collections/l3d/linux/

# change directory
cd collections/ansible_collections/l3d.linux/

# optionally init git submodules
git submodule update --init --recursive

# optionally install all requirements
ansible-galaxy collection install -r requirements.yml --upgrade
```

You can also list a collection in ``requirements.yml``:
```yaml
---
collections:
  - name: l3d.linux
    version: ">=1.1.1"
```

## Include roles in your playbook
Example Playbook using the l3d.linux.packages role:
```yaml
---
- name: "Install NTP Server from collection l3d.linux"
  hosts: ntp.example.com
  roles:
    - {role: l3d.linux.packages, tags: ntp}
  vars:
```

## Requirements
The roles in this collection using the ``community.general`` ansible Collections.

### Example Requirements Installation:
```bash
# galaxy requirements
ansible-galaxy install -r requirements.yml --upgrade
```
