# Breaking Node
DownloadLink: https://www.vulnhub.com/entry/node-1,252/

```bash
root@kali:~# nmap -A 192.168.172.5

Starting Nmap 7.60 ( https://nmap.org ) at 2018-08-15 04:35 EDT
Nmap scan report for 192.168.172.5
Host is up (0.00080s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE            VERSION
22/tcp   open  ssh                OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 dc:5e:34:a6:25:db:43:ec:eb:40:f4:96:7b:8e:d1:da (RSA)
|   256 6c:8e:5e:5f:4f:d5:41:7d:18:95:d1:dc:2e:3f:e5:9c (ECDSA)
|_  256 d8:78:b8:5d:85:ff:ad:7b:e6:e2:b5:da:1e:52:62:36 (EdDSA)
3000/tcp open  hadoop-tasktracker Apache Hadoop
| hadoop-datanode-info:
|_  Logs: /login
|_hadoop-jobtracker-info:
| hadoop-tasktracker-info:
|_  Logs: /login
|_hbase-master-info:
|_http-title: MyPlace
MAC Address: 08:00:27:A2:8A:95 (Oracle VirtualBox virtual NIC)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.10 - 4.8, Linux 3.16 - 4.6, Linux 3.2 - 4.8, Linux 4.4
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.80 ms 192.168.172.5

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.24 seconds

```