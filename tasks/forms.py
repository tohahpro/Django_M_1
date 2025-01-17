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

        widgets = {
            'title':forms.TextInput(attrs={
                'class':"border border-gray-300 w-full rounded-lg shadow-sm focus:border-rose-500 focus:ring-rose-500", 'placeholder':"Enter Task title"
            }),
            'description': forms.Textarea(attrs={
                'class':"border border-gray-300 w-full rounded-lg shadow-sm focus:border-rose-500 focus:ring-rose-500", 'placeholder':"Enter your description"
            }),
            'due_date': forms.SelectDateWidget(attrs={
                'class':"border border-gray-300 shadow-sm focus:border-rose-500 focus:ring-rose-500"
            }),
            'assigned_to': forms.CheckboxSelectMultiple
        }
