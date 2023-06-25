from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'status')
    list_editable = ('status',)
    list_filter = ('started_at_date',)


# Register your models here.
admin.site.register(Category)
admin.site.register(Task, TaskAdmin)
admin.site.register(BigTask)
