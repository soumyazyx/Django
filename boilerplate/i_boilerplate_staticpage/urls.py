from django.urls import path
from . import views

urlpatterns = [
    path('', views.i_boilerplate_staticpage_home)
]
