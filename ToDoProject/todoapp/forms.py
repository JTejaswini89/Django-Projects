# forms.py

from django import forms
from .models import Task  # Assuming your model is named Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        #These lines are to add the input box effects we do this here
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'task-input',
                'placeholder': 'Enter your task...'
            }),
        }
