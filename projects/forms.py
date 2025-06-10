from django import forms
from projects.models import Project
from authors.models import Author

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'status', 'budget', 'manager']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=Project.STATUS_CHOICES),
            'budget': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }