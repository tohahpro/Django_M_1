from django.urls import path
from tasks.views import user_dashboard, manager_dashboard, test, create_task, view_task

urlpatterns = [
    path('user-dashboard/', user_dashboard),
    path('manager-dashboard/', manager_dashboard, name='manager-dashboard'),
    path('test/', test),
    path('create-task/', create_task, name='create-task'),
    path('view-task/', view_task)

]