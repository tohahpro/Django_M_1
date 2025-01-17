from django import forms
from tasks.models import Task

# Django Form 
class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, label='Task Title')
    description = forms.CharField(widget=forms.Textarea, label='Task Description')
    due_date = forms.DateField(widget=forms.SelectDateWidget, label='Due Date')
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Assigned To')
    

    def __init__(self, *args, **kwargs):
        employees = kwargs.pop("employees",[])

        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices = [(emp.id, emp.name) for emp in employees]


# Django Model Form 
class TaskModelFrom(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','due_date','assigned_to']
        # exclude = ['project', 'is_completed', 'created_at', 'updated_at']
