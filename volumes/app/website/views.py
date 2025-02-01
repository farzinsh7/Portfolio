from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.utils.timezone import now
from datetime import date
from . import models


class IndexView(TemplateView):
    template_name = "website/index.html"


class AboutView(DetailView):
    template_name = "website/about.html"
    model = models.MyInformation

    def get_object(self, queryset=None):
        return models.MyInformation.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = models.Skills.objects.all()

        # Get the object instance
        my_info = self.get_object()
        if my_info and my_info.birth_date:
            today = date.today()
            age = today.year - my_info.birth_date.year - (
                (today.month, today.day) < (
                    my_info.birth_date.month, my_info.birth_date.day)
            )
            context['age'] = age
        else:
            context['age'] = None

        return context


class ContactView(TemplateView):
    template_name = "website/contact.html"
