# todo_app/admin.py

from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'priority', 'effort')
    list_filter = ('completed', 'priority', 'effort')
    search_fields = ('title',)  # Add 'title' to enable searching
    ordering = ('title',)  # Add 'title' to enable ordering

admin.site.register(Task, TaskAdmin)

