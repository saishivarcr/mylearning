# Ansible Installation
## Pre-requites
Ubuntu 16.04(Xenial)/Any Supported Linux OS is Installed

### Install/Enable ssh (Optional)
```bash
$ sudo apt-get update
$ sudo apt-get install openssh-server
```
## Install PIP
```bash
$ sudo apt-get install python-pip
```
## Install Ansible
```bash
$ sudo pip install ansible
```
## Verify
```bash
$ ansible --version
ansible 2.5.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/sai/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python2.7/dist-packages/ansible
  executable location = /usr/local/bin/ansible
  python version = 2.7.12 (default, Dec  4 2017, 14:50:18) [GCC 5.4.0 20160609]
```
