from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelFrom
from tasks.models import Employee, Task

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

def create_task(request):
    # employees = Employee.objects.all()
    form = TaskModelFrom()


    if request.method == "POST":
        form = TaskModelFrom(request.POST)
        if form.is_valid():
            """For Model From Data"""
            print(form)
            form.save()

            return render(request,'task_form.html',{"form": form, "message": "Task added successfully"})


            """For Django From Data"""

            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')

            # # django shell e jamon kaj ta kortam 
            # task = Task.objects.create(
            #     title=title, description=description, due_date=due_date)
            
            # # Assign employee to tasks
            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employee)


    context = {"form": form}
    return render(request, "task_form.html", context)



def view_task(request):
    # Retrieving Data task model 
    tasks = Task.objects.all()
    # return render(request, 'view_task.html',{"tasks": tasks})

    # Retrieving a specific task
    task_3 = Task.objects.get(id=1)
    
    return render(request, 'view_task.html',{"tasks": tasks, 'task_3': task_3})
    
