from django.urls import path
from .views import *

urlpatterns = [
    path('', task_listing, name='home'),
    path('all-tasks', all_tasks_listing, name='all_tasks'),
    path('task-create', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('big-task-create', BigTaskCreateView.as_view(), name='big_task_create'),
    path('task-start/<int:pk>/', task_start, name='task_start'),
    path('task-done/<int:pk>/', task_done, name='task_done'),
    path('task-plan/<int:pk>/', task_plan, name='task_plan'),
    # path('tasks/filter/<int:status>/', get_new_queryset, name='change_queryset'),
    # path('tasks/filter/<int:status>/', get_new_queryset, name='get_new_queryset'),
]
