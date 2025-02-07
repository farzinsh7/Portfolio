from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DeleteView, CreateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import InformationForm
from django.utils.translation import gettext_lazy as _
from website.models import MyInformation


class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"


class AdminInformationView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/information.html"
    model = MyInformation
    success_message = "The information was updated successfully."
    form_class = InformationForm

    def get_object(self, queryset=None):
        return MyInformation.objects.first()
