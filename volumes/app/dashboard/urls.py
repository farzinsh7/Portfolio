from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.DashboardHomeView.as_view(), name="home"),
    path("information/", views.AdminInformationView.as_view(), name="information"),
    path("website/", views.AdminWebsiteView.as_view(), name="website"),

    # skills
    path("skills/create/",
         views.AdminSkillCreateView.as_view(), name="skill-create"),
    path("skills/", views.AdminSkillListview.as_view(), name="skill-list"),
    path("skills/<int:pk>/update/",
         views.AdminSkillUpdateview.as_view(), name="skill-update"),
    path("skills/<int:pk>/delete/",
         views.AdminSkillDeleteView.as_view(), name="skill-delete"),

    # summary
    path("summary/", views.AdminSummaryView.as_view(), name="summary"),

]
