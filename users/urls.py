from django.urls import path
from users.views import sign_up, sign_in, sign_out,active_user, admin_dashboard

urlpatterns = [
    path('sign-up/', sign_up, name='sign-up'),    
    path('sign-in/', sign_in, name='sign-in'),    
    path('logout/', sign_out, name='logout'),    
    path('activate/<int:user_id>/<str:token>/',active_user),
    path('admin/dashboard/',admin_dashboard, name='admin-dashboard')
]