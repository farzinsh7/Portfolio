from django.http import Http404
from django.shortcuts import render

from portfolio_resume.models import Resume, ResumeGallery


def resume_detail(request, *args, **kwargs):
    selected_resume_id = kwargs['id']
    resume = Resume.objects.get_by_id(selected_resume_id)
    galleries = ResumeGallery.objects.filter(project_id=selected_resume_id)
    if resume is None:
        raise Http404('There is no project')
    context = {
        'resume': resume,
        'galleries': galleries
    }
    return render(request, 'resume_detail.html', context)