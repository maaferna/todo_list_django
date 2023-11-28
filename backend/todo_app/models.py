from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    description = models.TextField(blank=True, null=True)  # Added description field
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='')
    effort = models.CharField(max_length=10, choices=EFFORT_CHOICES, default='')
    created_at = models.DateTimeField(auto_now_add=True)  # Records creation timestamp
    modified_at = models.DateTimeField(auto_now=True)  # Records modification timestamp

    def __str__(self):
        return self.title


