import django_filters
from django_filters import widgets
from django import forms
# from django.utils.timezone import now
from .models import Task, CHOICES


class TaskFilter(django_filters.FilterSet):
    # status = django_filters.NumberFilter()
    status = django_filters.ChoiceFilter(choices=CHOICES, empty_label="Все", null_value=None,
                                         widget=forms.Select(attrs={"class": "form-select"}))
    start_date = django_filters.DateFilter(field_name='started_at_date', lookup_expr='gt')
    end_date = django_filters.DateFilter(field_name='started_at_date', lookup_expr='lt')
    date_range_modify = django_filters.DateRangeFilter(field_name='started_at_date',
                                                       widget=forms.Select(attrs={"class": "form-select"}))
    date_range = django_filters.DateFromToRangeFilter(field_name='started_at_date',
                                                      widget=forms.Select(attrs={"class": "form-select"}))

    class Meta:
        model = Task
        fields = ['status']


# choices = [
#     ('today', _('Сегодня')),
#     ('tomorrow', _('До завтра')),
#     ('week', _('На этой неделе')),
#     ('month', _('В этом месяце')),
#     ('all', _('Все')),
# ]
#
# filters = {
#     'today': lambda qs, name: qs.filter(**{
#         '%s__year' % name: now().year,
#         '%s__month' % name: now().month,
#         '%s__day' % name: now().day
#     }),
#     'yesterday': lambda qs, name: qs.filter(**{
#         '%s__year' % name: (now() - timedelta(days=1)).year,
#         '%s__month' % name: (now() - timedelta(days=1)).month,
#         '%s__day' % name: (now() - timedelta(days=1)).day,
#     }),
#     'week': lambda qs, name: qs.filter(**{
#         '%s__gte' % name: _truncate(now() - timedelta(days=7)),
#         '%s__lt' % name: _truncate(now() + timedelta(days=1)),
#     }),
#     'month': lambda qs, name: qs.filter(**{
#         '%s__year' % name: now().year,
#         '%s__month' % name: now().month
#     }),
#     'year': lambda qs, name: qs.filter(**{
#         '%s__year' % name: now().year,
#     }),
# }
