from django.urls import path
from . import views


app_name = "portfolio"
urlpatterns = [
    path("portfolio/", views.PortfolioListView.as_view(), name="portfolio-list"),
    path("portfolio/<int:pk>/detail/",
         views.PortfolioDetailView.as_view(), name="portfolio-detail"),
]
