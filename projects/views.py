from django.views.generic import ListView, DetailView, CreateView

from projects.models import Project
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "firstfold/list.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "firstfold/detail.html"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "firstfold/create.html"
    fields = ["name", "description", "members"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.id])
