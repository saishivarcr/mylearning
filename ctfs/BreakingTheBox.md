# Breaking the Box
## Discover box/Get the IP address
### Using NMAP
```bash
# nmap 192.168.172.0/24
```
### Using netdiscover
```bash
# netdiscover -r 192.168.172.0/24
```
## Run deep/aggressive scan for the IP address obtained using NMAP
```bash
# nmap -A 192.168.172.6
```
## Enumerate the services running
### use nikto
> Nikto Web Scanner is a Web server scanner that tests Web servers for dangerous files/CGIs, outdated server software and other problems. It performs generic and server type specific checks. It also captures and prints any cookies received. 

```bash
# nikto -h http://192.168.172.6
```
### Use dirb
> DIRB is a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching a dictionary based attack against a web server and analyzing the response.

> DIRB comes with a set of preconfigured attack wordlists for easy usage but you can use your custom wordlists. Also DIRB sometimes can be used as a classic CGI scanner, but remember is a content scanner not a vulnerability scanner.

```bash
# dirb http://192.168.172.6
```