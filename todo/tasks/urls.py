from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.taskshome, name='taskshome'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete_task/<str:pk>/', views.deleteTask, name='delete_task'),
]
