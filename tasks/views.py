from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def manager_dashboard(request):
    return render(request, "dashboard/manager_dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")

def test(request):
    context = {
        "names" : ["toha", "Ahamd","john"]
    }
    return render(request, "Test.html",context)



