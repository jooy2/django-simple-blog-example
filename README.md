# Simple blog based Django framework
Simple blog example based Django framework

Created by leejooy96@gmail.com

## Features
- Simple design & simple layout
- User authentication with Django basic auth
- Easy-to-publish posts
- Comments and Likes

## Requirements
- Django 2.1
- django-jquery-js
- django-summernote

## Installation
First, you need to activate python virtual environment (virtualenv) in project root directory with following tutorial: https://docs.python.org/3/tutorial/venv.html

Then install requirements with follow command:
```shell script
(venv)$ pip install -r requirements.txt
```

You need to create migration files. If you did, run server to execute follow command: 
```shell script
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python managy.py runserver
```
OR, just execute following script file:

!!! **WARNING**: This command removes all migration files !!!
```shell script
(venv)$ ./initialize.sh
```

If you want to create superuser, enter the follow command:
```shell script
(venv)$ python manage.py createsuperuser
```