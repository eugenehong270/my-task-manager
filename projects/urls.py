from django.urls import path

from django.contrib.auth import views as auth_views

from projects.views import (
    ProjectListView,
    ProjectDetailView,
)


urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
]
