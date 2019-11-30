# Django

Installing django: `pip install django`

Verifying django installation: `python -m django 
--version`

To see the list of available sub-commands in django, simply type `django-admin`

```
F:\Repositories>django-admin

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
```

### Create a new Django project
The below command will create a new django project with basic file structures

`F:\Repositories\Django>django-admin startproject django_project`
```
F:.
│   manage.py
│
└───django_project
        settings.py
        urls.py
        wsgi.py
        __init__.py
```
**outer mysite/ root directory** 
- Just a container for your project.
- Its name doesn’t matter to Django; you can rename it to anything you like.

**manage.py:** 
- A command-line utility that lets you interact with this Django project in various ways.
- We wont be making any changes to this file

**inner mysite/ directory** 
- It is the actual Python package for your project. 
- Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

**mysite/__init__.py:** 
- An empty file that tells Python that this directory should be considered a Python package.

**mysite/settings.py:** 
- Settings/configuration for this Django project. 
- Django settings will tell you all about how settings work.
- We will be making many changes to this file

**mysite/urls.py:** 
- The URL declarations for this Django project; 
- a "table of contents" of your Django-powered site. 

**mysite/wsgi.py:** 
- An entry-point for WSGI-compatible web servers to serve your project. 
- This is how our webserver and web application communicates
- We will not make any changes to the file



`wsgi.py`


## Start the webserver
Navigate to the dir containing manage.py

`python manage.py runserver`

```
F:\Repositories\Django\django_project>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 30, 2019 - 03:37:28
Django version 2.2.7, using settings 'django_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
----
# Creating app

Didn't we just create an app ?
- We created a project/website
- A website can have many apps - store app, blog app
- we can take out an app and add to multiple projects
- `python manage.py startapp blog`
```
F:.
│   db.sqlite3
│   manage.py
│
├───blog
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   views.py
│   │   __init__.py
│   │
│   └───migrations
│           __init__.py
│
└───django_project
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py
    
```