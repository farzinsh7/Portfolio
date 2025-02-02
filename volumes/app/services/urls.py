from django.urls import path
from . import views


app_name = "services"
urlpatterns = [
    path("services/", views.ServicesListView.as_view(), name="services-list"),
]
