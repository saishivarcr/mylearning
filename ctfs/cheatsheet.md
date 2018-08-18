# Breaking the Box
## Discover box/Get the IP address
### Using NMAP
```bash
# nmap 192.168.172.0/24

Starting Nmap 7.60 ( https://nmap.org ) at 2018-08-18 06:20 EDT
Nmap scan report for 192.168.172.1
Host is up (0.00074s latency).
All 1000 scanned ports on 192.168.172.1 are filtered
MAC Address: 0A:00:27:00:00:13 (Unknown)

Nmap scan report for 192.168.172.2
Host is up (0.00096s latency).
All 1000 scanned ports on 192.168.172.2 are filtered
MAC Address: 08:00:27:99:5C:E8 (Oracle VirtualBox virtual NIC)

Nmap scan report for 192.168.172.6
Host is up (0.00059s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
80/tcp   open  http
8011/tcp open  unknown
MAC Address: 08:00:27:3D:25:33 (Oracle VirtualBox virtual NIC)

Nmap scan report for 192.168.172.4
Host is up (0.000011s latency).
All 1000 scanned ports on 192.168.172.4 are closed

Nmap done: 256 IP addresses (4 hosts up) scanned in 223.41 seconds

```
### Using netdiscover
```bash
# netdiscover -r 192.168.172.0/24

Currently scanning: Finished!   |   Screen View: Unique Hosts                                                                                      
                                                                                                                                                    
 3 Captured ARP Req/Rep packets, from 3 hosts.   Total size: 180                                                                                    
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
 -----------------------------------------------------------------------------
 192.168.172.1   0a:00:27:00:00:13      1      60  Unknown vendor                                                                                   
 192.168.172.2   08:00:27:99:5c:e8      1      60  PCS Systemtechnik GmbH                                                                           
 192.168.172.6   08:00:27:3d:25:33      1      60  PCS Systemtechnik GmbH

 ```
 ## Run deep/aggressive scan for the IP address obtained using NMAP
 ```bash
 # nmap -A 192.168.172.6

 Starting Nmap 7.60 ( https://nmap.org ) at 2018-08-18 06:31 EDT
Nmap scan report for 192.168.172.6
Host is up (0.00062s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 2.3.5
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.172.4
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 2.3.5 - secure, fast, stable
|_End of status
22/tcp   open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 d4:f8:c1:55:92:75:93:f7:7b:65:dd:2b:94:e8:bb:47 (DSA)
|   2048 3d:24:ea:4f:a2:2a:ca:63:b7:f4:27:0f:d9:17:03:22 (RSA)
|_  256 e2:54:a7:c7:ef:aa:8c:15:61:20:bd:aa:72:c0:17:88 (ECDSA)
80/tcp   open  http    Apache httpd 2.2.22 ((Ubuntu))
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: FRANK's Website | Under development
8011/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:3D:25:33 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.19 - 2.6.36
Network Distance: 1 hop
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.62 ms 192.168.172.6

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.75 seconds
```

## Enumerate the services running
### use nikto
> Nikto Web Scanner is a Web server scanner that tests Web servers for dangerous files/CGIs, outdated server software and other problems. It performs generic and server type specific checks. It also captures and prints any cookies received. 

```bash
# nikto -h http://192.168.172.6

- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.172.6
+ Target Hostname:    192.168.172.6
+ Target Port:        80
+ Start Time:         2018-08-18 06:39:17 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.2.22 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, inode: 1051931, size: 13516, mtime: Sat Apr 14 09:39:32 2018
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Uncommon header 'tcn' found, with contents: list
+ Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. See http://www.wisec.it/sectou.php?id=4698ebdc59d15. The following alternatives for 'index' were found: index.html, index.html.bak
+ Apache/2.2.22 appears to be outdated (current is at least Apache/2.4.12). Apache 2.0.65 (final release) and 2.2.29 are also current.
+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS 
+ OSVDB-3268: /img/: Directory indexing found.
+ OSVDB-3092: /img/: This might be interesting...
+ OSVDB-3233: /icons/README: Apache default file found.
+ 8497 requests: 0 error(s) and 11 item(s) reported on remote host
+ End Time:           2018-08-18 06:40:05 (GMT-4) (48 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```
### Use dirb
> DIRB is a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching a dictionary based attack against a web server and analyzing the response.

> DIRB comes with a set of preconfigured attack wordlists for easy usage but you can use your custom wordlists. Also DIRB sometimes can be used as a classic CGI scanner, but remember is a content scanner not a vulnerability scanner.

```bash
# dirb http://192.168.172.6

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sat Aug 18 07:01:53 2018
URL_BASE: http://192.168.172.6/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://192.168.172.6/ ----
+ http://192.168.172.6/cgi-bin/ (CODE:403|SIZE:289)                                                                                                 
==> DIRECTORY: http://192.168.172.6/css/                                                                                                            
+ http://192.168.172.6/development (CODE:401|SIZE:480)                                                                                              
==> DIRECTORY: http://192.168.172.6/img/                                                                                                            
+ http://192.168.172.6/index (CODE:200|SIZE:334)                                                                                                    
+ http://192.168.172.6/index.html (CODE:200|SIZE:13516)                                                                                             
==> DIRECTORY: http://192.168.172.6/js/                                                                                                             
+ http://192.168.172.6/LICENSE (CODE:200|SIZE:1093)                                                                                                 
+ http://192.168.172.6/robots (CODE:200|SIZE:21)                                                                                                    
+ http://192.168.172.6/robots.txt (CODE:200|SIZE:21)                                                                                                
+ http://192.168.172.6/server-status (CODE:403|SIZE:294)                                                                                            
==> DIRECTORY: http://192.168.172.6/vendor/                                                                                                         
                                                                                                                                                    
---- Entering directory: http://192.168.172.6/css/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                    
---- Entering directory: http://192.168.172.6/img/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                    
---- Entering directory: http://192.168.172.6/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                    
---- Entering directory: http://192.168.172.6/vendor/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                               
-----------------
END_TIME: Sat Aug 18 07:01:56 2018
DOWNLOADED: 4612 - FOUND: 8
```



