from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.utils.timezone import now
from datetime import timedelta
from todo.models import *
from .forms import *
from .services import *


# Create your views here.
# class TaskListView(ListView):
#     model = Task
#     template_name =
#     context_object_name = 'task_list'
#
#     def get_queryset(self):
#         return Task.objects.filter(status__lte=1)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(TaskListView, self).get_context_data()
#         context['status_list'] = CHOICES
#         context['task_done_list'] = self.model.objects.filter(status=2)
#         context['task_all_list'] = self.model.objects.all()
#         return context
#
#     #
#     def update_queryset(self):
#         self.queryset = Task.objects.filter(status=2)
#         return 1


def task_listing(request):
    # task_filtered = TaskFilter(request.GET, queryset=Task.objects.filter(status__lte=1))
    task_filtered = TaskFilter(request.GET, queryset=Task.objects.all())
    date_list = {
        "now": now().date().isoformat(),
        "tomorrow": (now() + timedelta(days=1)).date().isoformat(),
        "next_week": (now() + timedelta(days=7)).date().isoformat(),
        "all": (now() + timedelta(days=10000)).date().isoformat(),
    }
    context = {
        "task_list": task_filtered,
        "status_list": CHOICES,
        "date_list": date_list,
        "task_done_list": Task.objects.filter(status=2),
        "task_all_list": Task.objects.all(),
    }
    return render(request, "todo/index.html", context)


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskAddForm
    template_name = 'todo/addTask.html'
    success_url = reverse_lazy('home')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/viewTask.html'

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        # obj = get_object_or_404(Task, self.object.pk)
        form = TaskAddForm(instance=self.object)
        context['tasktupdateform'] = form
        return context

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskAddForm(request.POST)

        if form.is_valid():
            Task.objects.filter(pk=task.pk).update(**form.cleaned_data)
            # return redirect('task_detail', task.id)  # add your url
            return redirect('home')  # add your url


class BigTaskCreateView(CreateView):
    model = BigTask
    form_class = BigTaskAddForm
    template_name = 'todo/addBigTask.html'


def task_start(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    obj.status = 1
    obj.save()
    return redirect('home')


def task_done(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    obj.status = 2
    obj.save()
    return redirect('home')
