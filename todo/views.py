from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
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

