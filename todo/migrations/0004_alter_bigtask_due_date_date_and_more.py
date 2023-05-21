# Generated by Django 4.1.7 on 2023-04-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_bigtask_due_date_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigtask',
            name='due_date_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='bigtask',
            name='due_date_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Время окончания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Время окончания'),
        ),
    ]
