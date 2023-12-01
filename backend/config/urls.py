from django.contrib import admin
from django.urls import include, path
from todo_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
    path('login', view_login, name='login'),
    path('logout', view_logout, name="logout"),
    path('register', view_register, name="register"),
]
