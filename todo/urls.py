from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('task-create', TaskCreateView.as_view(), name='task_create'),
]
