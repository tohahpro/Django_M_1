from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def manager_dashboard(request):
    return render(request, "dashboard.html")

def user_dashboard(request):
    return render(request, "user_dashboard.html")



