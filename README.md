# File Server

File Server is a platform to exchange files throgh a local network. it is a web stack that is based on nginx as web server, reverse proxy and Django web framework.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Installation](#Installation)



## General Info

assume we want to share file sample.txt through this platform. first we should run the server on host computer that stores incoming files and serving files to other devices. then all devices should be connected to a single router (eg. home wifi network). now every device in this network can connect to host throgh a local network.

this service has an authorizaion method based on private ip addresses and a host admin should give privilages to users. otherwise they get a 403 error. the autorization is handled in two phases.first the nginx redirect all requests to a endpoint that acts as a registeration function. it captures client ip addresses and store them on a file named `client_addresses.txt`. so every client that visited the host ip address , is registered. then the host admin should pickup ip addresses from this file and write in the `permited_client_ips.txt` file. if client's ip is not in the permited_client_ips file , he/she does not have access to the host resources even she registered. the second and final phase is the ip_middleware that checks clients should be registered and authorized.

by using this service , you dont need to  connect your device to host computer by usb cables. it needs internet connection at its boot time and can do jobs without that anymore.its secure and suits for personal or small businness that needs a file sharing network.

## Technologies
* **Python 3.8**
* **Django 3**
* **Nginx**
* **Bootstrap**



## Installation:

#### ubuntu

get the project from this repository. move to the project root direcotory and run the command:
    ```source config.sh```

it will install the appropriate packages ,  install virual environment with python packages. then a prompt appeares that requires the user's name that every time she logs in to ubuntu with that.if it corrects create nginx server blocks , put environment variables in .env file.
next and final step is to run the run.py that acts as an entrypoint. it populates nginx server blocks with appropriate data  , migrate the database and run the django server.
now every device is accecible throgh the host private ip address as url.to get its value see `host_ip_address.txt` file.

Note: to access other devices , put their ip addresses in permited_client_ips.txt file. like this:
```
    192.168.1.6
    192.168.2.3
    192.168.1.8
    192.168.1.11

```
Note: in ` config.sh` the varible `FILE_SERVER_PATH` points to the location where all files recieves from clients stores here. change it to every location you want. also if you change that location you should this line to the same value. `mkdir /home/vahid/file-server/`
enjoy it :))).

#### other Unix like systems

change file `config.sh` based on your distribution. also in other unix systems the nginx config direcotry may differs from ```/etc/nginx```. so read nginx documentations and change config.sh and run.py accordinglly. other parts works fine with these configurations.

have any comments? email me at zidan.roony@yahoo.com
