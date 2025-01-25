from django.urls import path
from portfolio_resume.views import resume_detail

app_name = "resume"

urlpatterns = [
    path('resume/<id>/<title>', resume_detail, name="detail"),
]
