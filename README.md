# Django

Instal django: `pip install django`

Verify django: `python -m django --version`

Create project: `F:\Repositories\Django>django-admin startproject django_project`

```
F:.
│   manage.py
└───django_project
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

Navigate to the dir containing manage.py

start server: `python manage.py runserver`

if we go to http://127.0.0.1:8000/ on browser, we will see a default page




---

django-admin startproject helloworld
cd helloworld

python manage.py startapp howdy

register howdy as a new in settings.py 
helloworld > settings.py > INSTALLED_APPS > add 'howdy' 

python manage.py migrate
python manage.py createsuperuser

create the html page 
howdy > templates > howdy > howdyhome.html

link the page to view
howdy > views.py > def howdyhome 
return render(request, 'howdy/howdyhome.html')

link the view to url in howdy urls.py 
howdy > create urls.py > path('', views.howdyhome)

link howdy urls.py to main helloworld urls.py
path('', include('howdy.urls')),




---
**outer mysite/ root directory** : Just a container for project - can be renames
**manage.py:**: Command-line utility to interact with project

**inner mysite/ directory** 
- It is the actual Python package for your project. 
- Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

**mysite/__init__.py:**  An empty file that tells Python that this directory should be considered a Python package.

**mysite/settings.py:** - Settings/configuration for this Django project. We will be making many changes to this file

**mysite/urls.py:** The URL declarations for this Django project

**mysite/wsgi.py:** An entry-point for WSGI-compatible web servers to serve your project. We will not make any changes to the file
