from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"
