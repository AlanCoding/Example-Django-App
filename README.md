# Example-Django-App
Starting place to demo both Django basics and the basic twists to put on your project

## Creation Process

Pre-reqs:
 - create a virtual environment
 - pip install django, others in `requirements.txt`

Along the way, you'll need to use these commands. In-between you need to
actually write code.

```bash
# Find out what you can do
django-admin --help
# Create your django project
django-admin startproject demo
# Create your app
django-admin startapp hiworld
```

Alternatively, after you have started the project, you can run these
things with `python manage.py ....`.

```bash
# Create your app
python manage.py startapp hiworld
# Run the server
python manage.py runserver
```

Database setup in postgres:

```bash
# Get shell in the database
psql
# Create your database
CREATE DATABASE myproject;
# Create your user
CREATE USER myprojectuser WITH PASSWORD 'password';
```

# TYI 2015 projects

Class projects:

 - (demo) https://github.com/tiyd-python-2015-05/mowdie
 - (demo) https://github.com/tiyd-python-2015-05/contact321
 - https://github.com/tiyd-python-2015-05/single-page-app-template
 - https://github.com/tiyd-python-2015-05/urly-bird-api
 - https://github.com/tiyd-python-2015-05/django-movies
 - https://github.com/tiyd-python-2015-05/todomvc-django

Alan's version of it:

 - Github: http://www.ac4.xyz/
 - hosted: 
