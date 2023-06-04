from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from todo.models import *
from .forms import *


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'todo/index.html'
    context_object_name = 'task_list'


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
