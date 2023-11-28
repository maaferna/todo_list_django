# todo_app/urls.py

from django.urls import path
from .views import task_list

urlpatterns = [
    path('tasks/', task_list, name='task_list'),
]
