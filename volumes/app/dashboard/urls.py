from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.DashboardHomeView.as_view(), name="home"),
    path("information/", views.AdminInformationView.as_view(), name="information"),
    path("skills/", views.AdminSkillListview.as_view(), name="skill-list"),
    path("skills/<int:pk>/update/",
         views.AdminSkillUpdateview.as_view(), name="skill-update"),
]
