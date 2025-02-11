from django import forms
from django.utils.translation import gettext_lazy as _
from website.models import MyInformation, Counter, InterestedIn
from django.forms import inlineformset_factory, BaseInlineFormSet


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
        widgets = {
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = "form-control"
        self.fields['description'].widget.attrs['class'] = "form-control"
        self.fields['image'].widget.attrs['class'] = "form-control"
        self.fields['website'].widget.attrs['class'] = "form-control"
        self.fields['phone'].widget.attrs['class'] = "form-control"
        self.fields['city'].widget.attrs['class'] = "form-control"
        self.fields['degree'].widget.attrs['class'] = "form-control"
        self.fields['email'].widget.attrs['class'] = "form-control"
        self.fields['freelance'].widget.attrs['class'] = "form-check-input"


# Create a custom formset class for Counter
class BaseCounterFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.fields['title'].widget.attrs['class'] = 'form-control'
            form.fields['value'].widget.attrs['class'] = 'form-control'
            form.fields['icon'].widget.attrs['class'] = 'form-control'


# Create a custom formset class for InterestedIn
class BaseInterestedFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.fields['title'].widget.attrs['class'] = 'form-control'
            form.fields['color'].widget.attrs['class'] = 'form-control'
            form.fields['icon'].widget.attrs['class'] = 'form-control'


# Now use these custom formsets in your view
CounterFormSet = inlineformset_factory(MyInformation, Counter, fields=[
                                       'title', 'value', 'icon'], extra=1, can_delete=True, formset=BaseCounterFormSet)
InterestedFormSet = inlineformset_factory(MyInformation, InterestedIn, fields=[
                                          'title', 'color', 'icon'], extra=1, can_delete=True, formset=BaseInterestedFormSet)
