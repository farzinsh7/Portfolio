from django.shortcuts import render
from django.views.generic import DetailView
from . import models


class ResumeView(DetailView):
    template_name = "resume/resume.html"
    model = models.Summary

    def get_object(self, queryset=None):
        return models.Summary.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experience'] = models.Experience.objects.all()
        context['education'] = models.Education.objects.all()

        return context
