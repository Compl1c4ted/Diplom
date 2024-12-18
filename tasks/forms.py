from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'descriptions', 'status', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
