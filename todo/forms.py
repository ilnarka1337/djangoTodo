from django import forms
from .models import Task, BigTask
from django_filters import widgets
from django.contrib.admin.widgets import AdminDateWidget


class TaskAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["status"].widget.attrs.update({"class": "form-select", "width": "100%"})

    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'status', 'started_at_date', 'started_at_time', 'due_date_date',
                  'due_date_time']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "started_at_date": forms.SelectDateWidget(attrs={"class": "form-control snps-inline-select"}),
        }


class BigTaskAddForm(forms.ModelForm):
    class Meta:
        model = BigTask
        fields = ['title', 'description', 'category', 'body', 'started_at_date', 'started_at_time', 'due_date_date',
                  'due_date_time']
