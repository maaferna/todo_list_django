from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('dashboard/', dashboard, name='dashboard'),
    path('get_task_details/<int:task_id>/', get_task_details, name='get_task_details'),
]

handler403 = 'todo_app.views.custom_permission_denied'
