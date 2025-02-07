from django import forms
from django.utils.translation import gettext_lazy as _
from website.models import MyInformation


class InformationForm(forms.ModelForm):
    class Meta:
        model = MyInformation
        fields = [
            "title",
            "description",
            "image",
            "birth_date",
            "website",
            "phone",
            "city",
            "degree",
            "email",
            "freelance",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = "form-control"
        self.fields['description'].widget.attrs['class'] = "form-control"
        self.fields['image'].widget.attrs['class'] = "form-select"
        self.fields['birth_date'].widget.attrs['class'] = "form-control"
        self.fields['website'].widget.attrs['class'] = "form-control"
        self.fields['phone'].widget.attrs['class'] = "form-control"
        self.fields['city'].widget.attrs['class'] = "form-control"
        self.fields['degree'].widget.attrs['class'] = "form-control"
        self.fields['email'].widget.attrs['class'] = "form-select"
        self.fields['freelance'].widget.attrs['class'] = "form-control"
