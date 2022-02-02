from django.shortcuts import render, redirect
from portfolio_contact.forms import ContactForm
from portfolio_contact.models import ContactUS
from portfolio_resume.models import ResumeCategory, Resume, Services
from portfolio_settings.models import SiteSetting
from portfolio_skills.models import MySkills


def home_page(request):
    site_setting = SiteSetting.objects.first()
    skills = MySkills.objects.all()
    contact_form = ContactForm(request.POST or None)
    categories = ResumeCategory.objects.all()
    project = Resume.objects.get_queryset().all()
    services = Services.objects.all()
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUS.objects.create(full_name=full_name, email=email, subject=subject, text=text)
        # todo : show user a success message
        # contact_form = ContactUS.objects.create()

    context = {
        'setting': site_setting,
        'contact_form': contact_form,
        'skills': skills,
        'categories': categories,
        'project': project,
        'services': services,
    }
    return render(request, 'home_page.html', context)

