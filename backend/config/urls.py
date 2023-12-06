from django.contrib import admin
from django.urls import include, path
from todo_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
    path('login', view_login, name='login-customize'),
    path('logout', view_logout, name="logout-customize"),
    path('register', view_register, name="register"),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
]
