from django import forms
from django.utils.translation import gettext_lazy as _
from website.models import MyInformation, Counter, InterestedIn, Skills, Website, SocialMedias
from resume.models import Summary, Experience, Education
from services.models import Services, ServicesSummary
from django.forms import inlineformset_factory, BaseInlineFormSet


# -----------------------------Website--------------------------------------
class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = [
            "site_title",
            "sub_title",
            "about_me",
            "logo_image",
            "background_image",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['site_title'].widget.attrs['class'] = "form-control"
        self.fields['sub_title'].widget.attrs['class'] = "form-control"
        self.fields['about_me'].widget.attrs['class'] = "form-control"
        self.fields['logo_image'].widget.attrs['class'] = "form-control"
        self.fields['background_image'].widget.attrs['class'] = "form-control"


# Create a custom formset class for Social
class BaseSocialFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.fields['title'].widget.attrs['class'] = 'form-control'
            form.fields['icon'].widget.attrs['class'] = 'form-control'
            form.fields['link'].widget.attrs['class'] = 'form-control'


SocialFormSet = inlineformset_factory(Website, SocialMedias, fields=[
    'title', 'icon', 'link'], extra=5, can_delete=True, formset=BaseSocialFormSet)


# -----------------------------Services--------------------------------------
class ServicesSummaryForm(forms.ModelForm):
    class Meta:
        model = ServicesSummary
        fields = [
            "title",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = "form-control"
        self.fields['description'].widget.attrs['class'] = "form-control"


# Create a custom formset class for Social
class BaseServicesFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.fields['title'].widget.attrs['class'] = 'form-control'
            form.fields['icon'].widget.attrs['class'] = 'form-control'
            form.fields['description'].widget.attrs['class'] = 'form-control'
            form.fields['description'].widget.attrs['rows'] = '3'


ServiceFormSet = inlineformset_factory(ServicesSummary, Services, fields=[
    'title', 'icon', 'description'], extra=10, can_delete=True, formset=BaseServicesFormSet)

# -----------------------------Informations--------------------------------------


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


class BaseCounterFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.fields['title'].widget.attrs['class'] = 'form-control'
            form.fields['value'].widget.attrs['class'] = 'form-control'
            form.fields['icon'].widget.attrs['class'] = 'form-control'


class BaseInterestedFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.fields['title'].widget.attrs['class'] = 'form-control'
            form.fields['color'].widget.attrs['class'] = 'form-control'
            form.fields['icon'].widget.attrs['class'] = 'form-control'


CounterFormSet = inlineformset_factory(MyInformation, Counter, fields=[
                                       'title', 'value', 'icon'], extra=10, can_delete=True, formset=BaseCounterFormSet)
InterestedFormSet = inlineformset_factory(MyInformation, InterestedIn, fields=[
                                          'title', 'color', 'icon'], extra=10, can_delete=True, formset=BaseInterestedFormSet)


# ---------------------------Skills----------------------------------------
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = [
            "title",
            "value",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = "form-control"
        self.fields['value'].widget.attrs['class'] = "form-control"


# ---------------------------Resume----------------------------------------
class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = [
            "title",
            "description",
            "short_description",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = "form-control"
        self.fields['description'].widget.attrs['class'] = "form-control"
        self.fields['short_description'].widget.attrs['class'] = "form-control"


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "from_date",
            "till_date",
            "company",
            "company_location",
            "description",
        ]
        widgets = {
            'from_date': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'till_date': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = "form-control"
        self.fields['company'].widget.attrs['class'] = "form-control"
        self.fields['company_location'].widget.attrs['class'] = "form-control"
        self.fields['description'].widget.attrs['class'] = "form-control"


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            "title",
            "from_date",
            "till_date",
            "university",
            "university_location",
            "description",
        ]
        widgets = {
            'from_date': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'till_date': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = "form-control"
        self.fields['university'].widget.attrs['class'] = "form-control"
        self.fields['university_location'].widget.attrs['class'] = "form-control"
        self.fields['description'].widget.attrs['class'] = "form-control"
