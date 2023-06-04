from django import forms
from .models import Task, BigTask


class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'started_at_date', 'started_at_time', 'due_date_date',
                  'due_date_time']


class BigTaskAddForm(forms.ModelForm):
    class Meta:
        model = BigTask
        fields = ['title', 'description', 'category', 'body', 'started_at_date', 'started_at_time', 'due_date_date',
                  'due_date_time']
