from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
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

        return context


class ContactView(TemplateView):
    template_name = "website/contact.html"
