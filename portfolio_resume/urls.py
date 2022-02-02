from django.urls import path

from portfolio_resume.views import resume_detail

urlpatterns = [
    path('resume/<id>/<title>', resume_detail),
]
