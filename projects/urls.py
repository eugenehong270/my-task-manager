from django.urls import path

from django.contrib.auth import views as auth_views

from projects.views import (
    ProjectListView,
)


urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
]
