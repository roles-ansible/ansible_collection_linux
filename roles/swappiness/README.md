 Ansible role to set swappiness
==============================

This pretty simple ansible role will set the vm.swappiness to ``{{ swappiness__vm_swappiness | default('5') }}``.
