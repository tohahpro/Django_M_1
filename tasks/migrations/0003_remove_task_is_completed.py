# Generated by Django 5.1.4 on 2025-02-13 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_taskdetails_assigned_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_completed',
        ),
    ]
