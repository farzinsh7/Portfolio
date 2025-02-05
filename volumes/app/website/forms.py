from django import forms
from .models import ContactUs


class ContactFormClass(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('full_name', 'subject', 'email', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['class'] = "form-control"
        self.fields['full_name'].widget.attrs['placeholder'] = "Your Name"
        self.fields['subject'].widget.attrs['class'] = "form-control"
        self.fields['subject'].widget.attrs['placeholder'] = "Subject"
        self.fields['email'].widget.attrs['class'] = "form-control"
        self.fields['email'].widget.attrs['placeholder'] = "Your Email"
        self.fields['message'].widget.attrs['class'] = "form-control"
        self.fields['message'].widget.attrs['placeholder'] = "Message"
