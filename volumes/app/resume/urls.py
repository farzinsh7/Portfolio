from django.urls import path
from . import views


app_name = "resume"
urlpatterns = [
    path("resume/", views.ResumeView.as_view(), name="resume-detail"),
]
