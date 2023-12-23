from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('dashboard/', dashboard, name='dashboard'),
    path('get_task_details/<int:task_id>/', get_task_details, name='get_task_details'),
    path('serializer_tasks/', TasksList.as_view()),
    path('create-task/', TaskCreateView.as_view(), name='create-task'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf'),
    path('get-user-data/', current_user, name='current_user'),

]

handler403 = 'todo_app.views.custom_permission_denied'
