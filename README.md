# Django-simple-blog
Simple blog example using Python3 and Django framework

Created by leejooy96@gmail.com

## Features
- Minimal style & simple layout
- Responsive web
- User authentication with Django basic auth
- Easy-to-publish posts
- Easy customize blog
- Comments and Likes

## Requirements
- Python 3.7
- Django 2.1
- SQLite3
- Browser support ES6 script

## Dependencies
- [BootStrap 4 & JQuery 3.4.1 (Installed)](https://getbootstrap.com/)
- [django-summernote](https://github.com/summernote/django-summernote)
- [django-el-pagination](https://github.com/shtalinberg/django-el-pagination)

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

## Todo
- [ ] Add license
- [ ] Complete profile page
- [ ] Tab based settings page
- [ ] Logo image
- [ ] Add post category

## References
- Django Girls Tutorial : https://tutorial.djangogirls.org/