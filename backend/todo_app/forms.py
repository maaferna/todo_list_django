from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'priority', 'effort']
        # You can customize the widgets or add extra validation if needed
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title here'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description here'}),
            'priority': forms.Select(attrs={'class': 'custom-select'}),
            'effort': forms.Select(attrs={'class': 'custom-select'}),
        }


