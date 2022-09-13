from django.urls import path

from django.contrib.auth import views as auth_views

from tasks.views import TaskCreateView, TaskListView


urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="create_task"),
    path("mine/", TaskListView.as_view(), name="show_my_tasks"),
]
