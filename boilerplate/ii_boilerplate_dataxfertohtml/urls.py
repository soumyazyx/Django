from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ii_boilerplate_dataxfertohtml_home)
]