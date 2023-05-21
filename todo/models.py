import datetime

import django.utils.timezone
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

CHOICES = (
    (0, 'Запланировано'),
    (1, 'В процессе'),
    (2, 'Выполнено'),
)


# Create your models here.
class Category(MPTTModel):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, verbose_name='Описание', blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.CharField(max_length=1000, verbose_name='Описание задачи', blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    started_at_date = models.DateField(default=django.utils.timezone.localtime, verbose_name='Дата начала')
    started_at_time = models.TimeField(default=django.utils.timezone.localtime, verbose_name='Время начала')
    due_date_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
    due_date_time = models.TimeField(verbose_name='Время окончания', blank=True, null=True)
    order_in_big_task = models.IntegerField(blank=True, null=True, default=0, verbose_name='Приоритетность')
    status = models.IntegerField(default=0, choices=CHOICES)

    def __str__(self):
        return self.title


class BigTask(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название крупной задачи')
    description = models.CharField(max_length=1000, verbose_name='Описание задачи', blank=True)
    body = models.ManyToManyField(Task, verbose_name='Подзадачи', related_name='tasks')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    started_at_date = models.DateField(default=django.utils.timezone.localtime, verbose_name='Дата начала')
    started_at_time = models.TimeField(default=django.utils.timezone.localtime, verbose_name='Время начала')
    due_date_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
    due_date_time = models.TimeField(verbose_name='Время окончания', blank=True, null=True)
    status = models.IntegerField(default=0, choices=CHOICES)

    def __str__(self):
        return self.title
