from django.db import models

# Create your models here.

# many to many 
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Task(models.Model):
    project= models.ForeignKey(
        "Projects",
        on_delete=models.CASCADE, 
        default=1
    )
    assigned_to = models.ManyToManyField(Employee, related_name='tasks')
    # notun_string = models.CharField(max_length=100,default="")
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TaskDetails(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM , 'Medium'),
        (LOW, 'Low'),
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices= PRIORITY_OPTIONS, default=LOW)

class Projects(models.Model):
    name= models.CharField(max_length=100)
    start_date = models.DateField()

