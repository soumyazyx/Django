from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataxfer_home),
    path('faqs/', views.dataxfer_home),

]
