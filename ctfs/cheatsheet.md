### Python simple HTTP server
```Python
python -m SimpleHTTPServer 
```
### Kali Linux assign two network interfaces
Edit `/etc/network/interfaces` and add these lines
```
auto eth0 
iface eth0 inet dhcp 
 
 
auto eth1 
iface eth1 inet dhcp 

```
And then restart the network with following commands.
```bash
systemctl stop networking 
systemctl start networking 
```
### Get interactive bash shell using python
```Python
python -c "import pty;pty.spawn('/bin/bash')"
```

