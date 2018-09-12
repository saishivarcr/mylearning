# Installing Docker using Ansible
## Pre-requisites
Ansible version >2.4 installed on linux machine.
## Install docker role for ansible
```bash
$ ansible-galaxy install geerlingguy.docker
$ ansible-galaxy install geerlingguy.pip
```
## Create playbook and run for installing docker
copy and paste below playbook contents to `play.yml`
```
---
- hosts: localhost

  vars:
    pip_install_packages:
      - name: docker

  roles:
    - geerlingguy.pip
    - geerlingguy.docker
```
Run below command to install docker on localmachine
```bash
$ ansible-playbook play.yml
```
## Check docker version
```bash
$ docker --version
Docker version 18.06.0-ce, build 0ffa825
```