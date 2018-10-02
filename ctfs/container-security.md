
## Attacking and auditing Containers

https://github.com/docker/docker-bench-security

https://www.youtube.com/watch?v=ru7GicI5iyI

https://gist.github.com/FrankSpierings/5c79523ba693aaa38bc963083f48456c


## Docker
### Install Docker on Kali
#### Add Docker PGP key:

```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
```

#### Configure Docker APT repository:

```bash
echo 'deb https://download.docker.com/linux/debian stretch stable' > /etc/apt/sources.list.d/docker.list
```

#### Update APT:

```bash
apt-get update
```

#### Install Docker

If you had older versions of Docker installed, uninstall them:

```bash
apt-get remove docker docker-engine docker.io
```
Install Docker:

```bash
apt-get install docker-ce
```
#### Post Install settings
```bash
systemctl start docker
systemctl enable docker
```
#### Testing
```bash
docker run hello-world
```
### Setup DVWA
```bash
docker run -d -p 80:80 citizenstig/dvwa
```
## Privilege Escalation Techniques