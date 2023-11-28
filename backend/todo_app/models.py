# todo_app/models.py

from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('', 'Select Priority'),
        ('low', 'Bajo'),
        ('medium', 'Medio'),
        ('high', 'Alto'),
        ('important', 'Importante'),
    ]

    EFFORT_CHOICES = [
        ('', 'Select Effort'),
        ('low', 'Bajo'),
        ('medium', 'Medio'),
        ('high', 'Alto'),
    ]

    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='')
    effort = models.CharField(max_length=10, choices=EFFORT_CHOICES, default='')

    def __str__(self):
        return self.title


