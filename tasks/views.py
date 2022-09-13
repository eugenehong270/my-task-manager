from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from tasks.models import Task
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "folder2/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.assignee = self.request.user
        item.save()
        return redirect("show_project", pk=item.id)

    def get_success_url(self) -> str:
        return reverse_lazy("show_project", args=[self.object.id])


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "folder2/list.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)
