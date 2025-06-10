from django import forms
from .models import Manuscript

class ManuscriptForm(forms.ModelForm):
    class Meta:
        model = Manuscript
        fields = ['project', 'title', 'file', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }