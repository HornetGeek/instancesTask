# Create Docker instance using Django and celery

A user can launch multiple Linux instances.
Multiple users can launch an instance at the same time.

## How to run it ?

### setup the machine

First you need to install django in your machine
```sh
$ sudo pip3 install Django
```

then install celery and redis
```sh
$ sudo pip3 install celery 
```
```sh
$ sudo apt-get install redis-server
```
### run the project

start the redis server by 
```sh
$ redis-server
```
create a new tap in the terminal and run the server of the django by
```sh
$ sudo python3 manage.py runserver
```
another tap for celry worker 
```sh
$ sudo celery worker -A cyberdefenders --loglevel=info
```
then open the website in your local machine http://localhost:8000/

## feature roadmap
use socketIO to handel realtime update in the UI
