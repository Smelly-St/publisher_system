from django import forms
from authors.models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'contact_info']
        widgets = {
            'contact_info': forms.Textarea(attrs={'rows': 3}),
        }