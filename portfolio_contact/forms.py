from django import forms
from django.core import validators


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control', 'id': 'name'}),
        label='',
        validators=[
            validators.MaxLengthValidator(120, 'Max Length is 120 Characters')
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control', 'id': 'email'}),
        label='',
        validators=[
            validators.MaxLengthValidator(100, 'Max Length is 100 Characters')
        ]
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control', 'id': 'subject'}),
        label='',
        validators=[
            validators.MaxLengthValidator(200, 'Max Length is 200 Characters')
        ]
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control', 'rows': '5'}),
        label=''
    )
