# Generated by Django 5.1.4 on 2025-02-13 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_task_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskdetails',
            name='asset',
            field=models.ImageField(blank=True, null=True, upload_to='tasks_asset'),
        ),
    ]
