[![collection l3d.linux](https://ansible.l3d.space/svg/l3d.linux_ansible-collection_collection.svg)](https://galaxy.ansible.com/ui/repo/published/l3d/linux/)
[![Maintainance](https://ansible.l3d.space/svg/l3d.linux_maintainance_collection.svg)](https://ansible.l3d.space/#l3d.linux)
[![License](https://ansible.l3d.space/svg/l3d.linux_license_collection.svg)](LICENSE)

 MODULE l3d.linux.extrepo
==========================

Wrapper for extrepo - [manpages.ubuntu.com](https://manpages.ubuntu.com/manpages/focal/man1/extrepo.1p.html)

## OPTIONS for l3d.linux.extrepo

+ **action**: This parameter is used to define what extrepo is doing.
  - type: `str`
  - required: `true`
  - choices: `search`, `enable`, `disable`, `update`
+ **key**: Used for searching repos
  - type `str`
  - `required` false
+ **repository**: select a repository for an action

## Examples for l3d.linux.extrepo

```yml
---
- name: Enable librewolf via extrepo
  become: true
  l3d.linux.extrepo:
    action: 'enable'
    repository: "librewolf"
  register: _librewolf_repo

- name: Update librewolf via extrepo
  become: true
  l3d.linux.extrepo:
    action: 'update'
    repository: "librewolf"
  changed_when: _librewolf_repo.changed
```
