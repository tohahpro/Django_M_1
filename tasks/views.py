from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.forms import TaskModelFrom, TaskDetailsModelForm
from tasks.models import Employee, Task, TaskDetails, Projects
from django.db.models import Q, Count, Max, Min, Avg
from datetime import date
from django.contrib import messages

# Create your views here.

def manager_dashboard(request):   

    type = request.GET.get('type','all')
   
    # Optimizing Database Query.
    counts = Task.objects.aggregate(
        total=Count('id'),
        completed = Count('id', filter=Q(status = 'COMPLETED')),
        in_progress = Count('id', filter=Q(status = 'IN_PROGRESS')),
        pending = Count('id', filter=Q(status = 'PENDING')),
    )

    # Retrieving task data
    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')    

    if type == 'completed':
        tasks = base_query.filter(status = 'COMPLETED')
    elif type == 'in_progress':
        tasks = base_query.filter(status = 'IN_PROGRESS')
    elif type == 'pending':
        tasks = base_query.filter(status = 'PENDING')
    elif type == 'all':
        tasks = base_query.all()


    context = {
        "tasks" : tasks,
        "counts" : counts    
    }
    return render(request, "dashboard/manager_dashboard.html",context)

def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")


def create_task(request):
    # employees = Employee.objects.all()
    task_form = TaskModelFrom() # For GET
    task_detail_form = TaskDetailsModelForm()

    if request.method == "POST":        
        task_form = TaskModelFrom(request.POST)
        task_detail_form = TaskDetailsModelForm(request.POST)
        if task_form.is_valid() and task_detail_form.is_valid():

            """For Model From Data"""            
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request,"Task Created Successfully!")
            return redirect('create-task')

    context = {"task_form": task_form, "task_detail_form":task_detail_form}
    return render(request, "task_form.html", context)

def update_task(request,id):
    task = Task.objects.get(id=id)    
    task_form = TaskModelFrom(instance=task) # For GET
    task_detail_form = TaskDetailsModelForm()

    if task.details:
        task_detail_form = TaskDetailsModelForm(instance=task.details)

    if request.method == "POST":        
        task_form = TaskModelFrom(request.POST, instance=task)
        task_detail_form = TaskDetailsModelForm(request.POST,instance=task.details)
        if task_form.is_valid() and task_detail_form.is_valid():

            """For Model From Data"""            
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request,"Task Updated Successfully!")
            return redirect('manager-dashboard')

    context = {"task_form": task_form, "task_detail_form":task_detail_form}
    return render(request, "task_form.html", context)


def delete_task(request,id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, 'Task Deleted Successfully')
        return redirect('manager-dashboard')
    else:
        messages.error(request, 'Something went wrong')
    return redirect('manager-dashboard')




# for testing purpose
def test(request):
    context = {
        "names" : ["toha", "Ahamd","john"]
    }
    return render(request, "Test.html",context)

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
    
   

    
