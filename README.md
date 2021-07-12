# Django-simple-blog
Simple blog example using Python3 and Django framework.

## Features
- Flat design & Simple layout
- Responsive web (mobile support)
- User authentication with Django basic auth
- Easy to publish posts
- Easy to customize blog
- Comment and Like system

## Requirements
- Python 3.7.4 or higher
- Django 3.0 or higher
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

## License
MIT License

Copyright (c) 2020 jooy2

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## References
- Django Girls Tutorial : https://tutorial.djangogirls.org
