from django.views.generic import DetailView, CreateView
from datetime import date
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from . import models
from .forms import ContactFormClass


class IndexView(DetailView):
    template_name = "website/index.html"
    model = models.Website

    def get_object(self, queryset=None):
        return models.Website.objects.first()


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


class ContactView(SuccessMessageMixin, CreateView):
    template_name = "website/contact.html"
    form_class = ContactFormClass
    success_url = reverse_lazy("website:contact")
    template_name = "website/contact.html"
    success_message = "Your message has been sent. Thank you!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_information"] = models.MyInformation.objects.first()

        return context
