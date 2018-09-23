# Breaking the Box
## Discover box/Get the IP address
### Using NMAP
```bash
nmap 192.168.172.0/24
```
### Using netdiscover
```bash
netdiscover -r 192.168.172.0/24
```
## Run deep/aggressive scan for the IP address obtained using NMAP
```bash
nmap -A 192.168.172.6
```
## Enumerate the services running
### use nikto
> Nikto Web Scanner is a Web server scanner that tests Web servers for dangerous files/CGIs, outdated server software and other problems. It performs generic and server type specific checks. It also captures and prints any cookies received. 

```bash
nikto -h http://192.168.172.6
```
### Use dirb
> DIRB is a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching a dictionary based attack against a web server and analyzing the response.

> DIRB comes with a set of preconfigured attack wordlists for easy usage but you can use your custom wordlists. Also DIRB sometimes can be used as a classic CGI scanner, but remember is a content scanner not a vulnerability scanner.

```bash
dirb http://192.168.172.6
```
### Use Gobuster
> Gobuster is a tool used to brute-force:
> * URIs (directories and files) in web sites.
> * DNS subdomains (with wildcard support).

Scan a website (_-u http://192.168.0.155/_) for directories using a wordlist (_-w /usr/share/wordlists/dirb/common.txt_) and print the full URLs of discovered paths (-e):
```bash
gobuster -e -u http://192.168.0.155/ -w /usr/share/wordlists/dirb/common.txt
```
### Use dirbuster
> DirBuster is a multi threaded java application designed to brute force directories and files names on web/application servers.
This is kind of gui equivalent to gobuster
```bash
dirbuster
```
### Use wfuzz
> Wfuzz is a tool designed for bruteforcing Web Applications, it can be used for finding resources not linked (directories, servlets, scripts, etc), bruteforce GET and POST parameters for checking different kind of injections (SQL, XSS, LDAP,etc), bruteforce Forms parameters (User/Password), Fuzzing,etc.

Use colour output (_-c_), a wordlist as a payload (_-z file,/usr/share/wfuzz/wordlist/general/common.txt_), and hide 404 messages (_–hc 404_) to fuzz the given URL (_http://192.168.1.202/FUZZ_):
```bash
wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 http://192.168.1.202/FUZZ
```
### Use WMap
> WMAP is a feature-rich web application vulnerability scanner that was originally created from a tool named SQLMap. This tool is integrated with Metasploit and allows us to conduct web application scanning from within the Metasploit Framework.

[WMAP](https://www.offensive-security.com/metasploit-unleashed/wmap-web-scanner/)

