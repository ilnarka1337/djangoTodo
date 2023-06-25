import django_filters
from .models import Task, CHOICES


class TaskFilter(django_filters.FilterSet):
    # status = django_filters.NumberFilter()
    status = django_filters.ChoiceFilter(choices=CHOICES, empty_label=None, null_value=None)
    start_date = django_filters.DateFilter(field_name='started_at_date', lookup_expr='gt')
    end_date = django_filters.DateFilter(field_name='started_at_date', lookup_expr='lt')
    date_range = django_filters.DateRangeFilter(field_name='started_at_date')

    class Meta:
        model = Task
        fields = ['status']
