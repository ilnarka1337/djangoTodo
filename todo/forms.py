from django import forms
from .models import Task


class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'started_at_date', 'started_at_time', 'due_date_date',
                  'due_date_time']