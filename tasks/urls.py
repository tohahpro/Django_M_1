from django.urls import path
from tasks.views import user_dashboard, manager_dashboard, test

urlpatterns = [
    path('user-dashboard/', user_dashboard),
    path('manager-dashboard/', manager_dashboard),
    path('test/', test)

]