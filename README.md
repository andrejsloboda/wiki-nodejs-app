WikiJS App Prototype
=========
[WikiJS](https://github.com/requarks/wiki) is a modern, lightweight and powerful wiki app built on NodeJS. This repository contains tools to deploy a simple dockerized prototype of this application with PostgreSQL database container and Nginx container as a reverse proxy. All containers are created from official images.

Getting started
---------------
Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://developer.hashicorp.com/vagrant/downloads).

Add a password into ```./secrets/db_pass.txt``` and run in this directory:
```
vagrant up
```
Follow the provisioning steps. Vagrant will pull an image of Ubuntu 22.04.2 LTS (Jammy Jellyfish) and set up the virtual machine. Then it will install Ansible and run ```./ansible/playbook.yml``` inside that will install docker and run docker-compose to deploy the application.

The app will be running at [http://localhost:80](http://localhost:80)

Architecture
-----
![Architecture diagram](wiki_app_diagram.png)

* A WikiJS container
* A PostgreSQL container
* An Nginx container

Database Dump
-----
The repository contains python script ```./db_utils/db_dump.py```. It can be used to dump PostgreSQL. To do so you need to run following command from /vagrant folder as root on host machine where docker is running:
```
python3 db_dump.py <container> <user_name> <database> <destination>
```
An example:
```
python3 ./db_utils/db_dump.py vagrant-db-1 wiki_user wiki ./db_dump
```
This will create a zipped dump file in destination folder.


