from django.urls import path
from cors.views import home

urlpatterns = [
    path('home/',home, name='home'),    
]