from django import forms
from tasks.models import Task
from projects.models import Project
from authors.models import Author

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'assignee', 'due_date', 'status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=Task.STATUS_CHOICES),
        }