from django.contrib import admin
from tasks.models import Task, TaskDetails, Employee, Projects

# Register your models here.

admin.site.register(Task)
admin.site.register(TaskDetails)
admin.site.register(Projects)
