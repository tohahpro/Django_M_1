from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelFrom
from tasks.models import Employee, Task, TaskDetails, Projects
from django.db.models import Q, Count, Max, Min, Avg
from datetime import date

# Create your views here.


def manager_dashboard(request):
    tasks = Task.objects.all()

    # getting task count
    total_task = tasks.count()
    completed_task = Task.objects.filter(status='COMPLETED').count()
    in_progress_task = Task.objects.filter(status='IN_PROGRESS').count()
    pending_task = Task.objects.filter(status='PENDING').count()

    context = {
        "tasks" : tasks,
        "total_task" : total_task,
        "completed_task" : completed_task,
        "in_progress_task" : in_progress_task,
        "pending_task" : pending_task
    }
    return render(request, "dashboard/manager_dashboard.html",context)

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
    # tasks = Task.objects.all()
    # return render(request, 'view_task.html',{"tasks": tasks})

    # Retrieving a specific task
    # task_3 = Task.objects.get(id=1)    
    # return render(request, 'view_task.html',{"tasks": tasks, 'task_3': task_3})

    # taskFilter = Task.objects.filter(status="PENDING")
    # due_date_Filter = Task.objects.filter(due_date=date.today())

    # """Show the task whos priority is not low"""
    # priority_task = TaskDetails.objects.exclude(priority="L")

    # return render(request, 'view_task.html',{"taskFilter": taskFilter, "due_date_Filter":due_date_Filter,"Task_priority":priority_task })

    look_up = Task.objects.filter(title__icontains='b')

    task_1 = Task.objects.filter(Q(status='PENDING') | Q(status='IN_PROGRESS'))

    tasks = Task.objects.select_related('details').all()

    """Prefetch Related (Reverse Foreignkey, manyToMany)"""
    task_4 = Projects.objects.prefetch_related('task_set').all()

    """Prefetch Related (manyToMany)"""
    task_5 = Task.objects.prefetch_related("assigned_to").all()
    
    # return render(request, 'view_task.html', {"tasks": tasks,"tasks1": task_1, "task4":task_4,"task5":task_5,"look_up": look_up})

    # Aggregations [Advanced]
    # task_count = Task.objects.aggregate(num_task=Count('id'))
    projects = Projects.objects.annotate(num_task=Count('task')).order_by('num_task')

    return render(request, 'view_task.html', {"projects":projects})
    
   

    
