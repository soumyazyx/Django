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
MODELS
**Models = tables**

1. Create project
django-admin startproject helloworld
cd helloworld

[one time activity]
Migrate and create superuser 
python manage.py migrate
python manage.py createsuperuser - optional

2. Create app
python manage.py startapp howdy

3. Register the app in project settings
helloworld > settings.py > INSTALLED_APPS > add 'howdy' 

5. Create new html page
howdy > templates > howdy > home.html

6. Link the page to view
howdy > views.py > def howdy_home 
return render(request, 'howdy/home.html')

7. link the view to url in howdy urls.py 
howdy_home > create urls.py > path('', views.howdy_home)

8. link howdy urls.py to main helloworld urls.py
path('', include('howdy_home.urls')),

9. Create model. one MODEL class = one TABLE in db
howdy > models.py > 
```python
from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=1000)
    addr = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```
10. Run migration to create the table
python manage.py makemigrations - picks up the class
python manage.py migrate - creates the table

11. Link the model with admin.py so that it appears in the admin page
```python
from .models import Employee

admin.site.register(Employee)
```

12. Add an employee
    1. Goto admin console and add  or
    2. programatically
        ```python
        e1 = Employee(name='Soumya', addr='wherever')
        e1.save()
        ```

---

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
