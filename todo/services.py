import django_filters
from django_filters import widgets
from django import forms
from .models import Task, CHOICES

from datetime import timedelta
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

choices = [
    ('today', _('Сегодня')),
    ('tomorrow', _('Завтра')),
    ('week', _('На этой неделе')),
    ('month', _('В этом месяце')),
    ('year', _('В этом году')),
]

filters = {
    'today': lambda qs, name: qs.filter(**{
        '%s__year' % name: now().year,
        '%s__month' % name: now().month,
        '%s__day' % name: now().day
    }),
    'tomorrow': lambda qs, name: qs.filter(**{
        '%s__year' % name: (now() + timedelta(days=1)).year,
        '%s__month' % name: (now() + timedelta(days=1)).month,
        '%s__day' % name: (now() + timedelta(days=1)).day,
    }),
    'week': lambda qs, name: qs.filter(**{
        '%s__gte' % name: _truncate(now() - timedelta(days=7)),
        '%s__lte' % name: _truncate(now() + timedelta(days=1)),
    }),
    'month': lambda qs, name: qs.filter(**{
        '%s__year' % name: now().year,
        '%s__month' % name: now().month
    }),
    'year': lambda qs, name: qs.filter(**{
        '%s__year' % name: now().year,
    }),
}

date_list = {
    "now": now().date().isoformat(),
    "tomorrow": (now() + timedelta(days=1)).date().isoformat(),
    "next_week": (now() + timedelta(days=7)).date().isoformat(),
    "all": (now() + timedelta(days=10000)).date().isoformat(),
}

def _truncate(dt):
    return dt.date()


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=CHOICES, empty_label="Все", null_value=None,
                                         widget=forms.Select(attrs={"class": "form-select"}))
    start_date = django_filters.DateFilter(field_name='started_at_date', lookup_expr='gt')
    end_date = django_filters.DateFilter(field_name='started_at_date', lookup_expr='lt')
    date_range_modify = django_filters.DateRangeFilter(field_name='started_at_date', empty_label="Все", null_value=None,
                                                       choices=choices, filters=filters,
                                                       widget=forms.Select(attrs={"class": "form-select"}))
    date_range = django_filters.DateFromToRangeFilter(field_name='started_at_date',
                                                      widget=forms.Select(attrs={"class": "form-select"}))

    class Meta:
        model = Task
        fields = ['status']
