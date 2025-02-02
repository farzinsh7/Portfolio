from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Count
from . import models


class PortfolioListView(ListView):
    template_name = "portfolio/portfolio-list.html"

    def get_queryset(self):
        return models.Resume.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = models.ResumeCategory.objects.annotate(
            resume_count=Count('resume')).filter(resume_count__gt=0)
        return context


class PortfolioDetailView(DetailView):
    template_name = "portfolio/portfolio-detail.html"
    model = models.Resume
    queryset = models.Resume.objects.all()
