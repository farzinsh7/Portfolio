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


    # experience
    path("experience/create/",
         views.AdminExperienceCreateView.as_view(), name="experience-create"),
    path("experience/", views.AdminExperienceListview.as_view(),
         name="experience-list"),
    path("experience/<int:pk>/update/",
         views.AdminExperienceUpdateview.as_view(), name="experience-update"),
    path("experience/<int:pk>/delete/",
         views.AdminExperienceDeleteView.as_view(), name="experience-delete"),


    # education
    path("education/create/",
         views.AdminEducationCreateView.as_view(), name="education-create"),
    path("education/", views.AdminEducationListview.as_view(),
         name="education-list"),
    path("education/<int:pk>/update/",
         views.AdminEducationUpdateview.as_view(), name="education-update"),
    path("education/<int:pk>/delete/",
         views.AdminEducationDeleteView.as_view(), name="education-delete"),
]
