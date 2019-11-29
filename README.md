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

`manage.py`
-   We wont be making any changes to this file
- This file helps us in running some commands

`__init__.py`
- empty file
- This just tells python that it is a package

`settings.py`
- This is where all the settings and configurations are
- We will be making many changes to this file

`urls.py`
- This contains the routes

`wsgi.py`
- This is how our webserver and web application communicates
- We will not make any changes to the file


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
