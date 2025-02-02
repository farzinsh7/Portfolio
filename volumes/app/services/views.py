from django.shortcuts import render
from django.views.generic import DetailView
from . import models


class ServicesListView(DetailView):
    template_name = "services/services-list.html"
    model = models.ServicesSummary

    def get_object(self, queryset=None):
        return models.ServicesSummary.objects.first()
