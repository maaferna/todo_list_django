from django.urls import path
from .views import home, delete_task, edit_task

urlpatterns = [
    path('', home, name='home'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
]
