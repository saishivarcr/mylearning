# Securing NFS share

## Securing NFS Server
Set permissions in `/etc/exports` file for each of the directories made available over the network

Sample Entry:
```bash
/directory/to/share machine1(option1,option2,...) machine2(...) ...
```

**machine1**: IP/Hostname which is granted permission to access the shared folder.

**/directory/to/share**: Absolute path to shared folder

Example Entry:
```
/usr/share/example 127.0.0.1(rw,sync,no_subtree_check)
```

### Notes

* Directories are made available as read-only by default (or with the ro option). The **rw** option allows read-write access.
* By default, the server only answers an NFS query when the current disk operation is complete (**sync** option); this can be disabled with the **async** option.
* In order to not give root access to the filesystem to any NFS client, all queries appearing to come from a root user are considered by the server as coming from the nobody user. This behavior corresponds to the **root_squash** option, and is enabled by default. The **no_root_squash** option, which disables this behavior, is risky and should only be used in controlled environments.
* [Reference - The Debian Administrator's Handbook](https://debian-handbook.info/browse/wheezy/sect.nfs-file-server.html)

# Exploiting misconfigured NFS share

* [Exploiting NFS Share](https://resources.infosecinstitute.com/exploiting-nfs-share/)

