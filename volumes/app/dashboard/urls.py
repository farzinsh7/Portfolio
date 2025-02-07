from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.DashboardHomeView.as_view(), name="home"),
    path("information/", views.AdminInformationView.as_view(), name="information"),
]
