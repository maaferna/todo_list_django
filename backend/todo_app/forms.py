from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'priority', 'effort']
        # You can customize the widgets or add extra validation if needed
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title here'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description here', 'class': 'custom-description-field'}),
            'priority': forms.Select(attrs={'class': 'custom-select'}),
            'effort': forms.Select(attrs={'class': 'custom-select'}),
        }

    def __init__(self, *args, **kwargs):
            super(TaskForm, self).__init__(*args, **kwargs)
            # Make the priority and effort fields optional with default values
            self.fields['priority'].required = True
            self.fields['effort'].required = True

    def clean(self):
        cleaned_data = super(TaskForm, self).clean()
        priority = cleaned_data.get('priority')
        effort = cleaned_data.get('effort')

        # Check if either priority or effort is missing
        if priority is None or effort is None:
            raise forms.ValidationError("Please select values for both priority and effort.")

        return cleaned_data
