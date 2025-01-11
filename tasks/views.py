from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # work with database
    # data pass
    # Transform data
    # Http response / Json Response
    return HttpResponse("hello")

def contact(request):
    return HttpResponse("This is contact page.")

def show_task(request):
    return HttpResponse("this is show task.")

def show_specific_task(request, id):
    print("id", id)
    print("id type", type(id))
    return HttpResponse(f"This is specific task.{id}")