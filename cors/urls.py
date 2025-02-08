from django.urls import path
from cors.views import home, no_permission

urlpatterns = [
    path('home/',home, name='home'),    
    path('no-permission/',no_permission, name='no-permission'),    
]