from django import forms
from .models import Manuscript


class ManuscriptForm(forms.ModelForm):
    class Meta:
        model = Manuscript
        fields = '__all__'
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }