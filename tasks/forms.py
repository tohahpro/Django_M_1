from django import forms
from tasks.models import Task, TaskDetails

# Django Form 
# class TaskForm(forms.Form):
#     title = forms.CharField(max_length=250, label='Task Title')
#     description = forms.CharField(widget=forms.Textarea, label='Task Description')
#     due_date = forms.DateField(widget=forms.SelectDateWidget, label='Due Date')
#     assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Assigned To')
    

#     def __init__(self, *args, **kwargs):
#         employees = kwargs.pop("employees",[])

#         super().__init__(*args, **kwargs)
#         self.fields['assigned_to'].choices = [(emp.id, emp.name) for emp in employees]


# Use Form Mixins for Clean Code
class StyleForMixin:
    """ Mixing to apply style to form field"""

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_styled_widgets()

    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder':  f"Enter {field.label.lower()}",
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                print("Inside Date")
                field.widget.attrs.update({
                    "class": "border-2 border-gray-300 p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                print("Inside checkbox")
                field.widget.attrs.update({
                    'class': "space-y-2"
                })
            else:
                print("Inside else")
                field.widget.attrs.update({
                    'class': self.default_classes
                })
                


# Django Model Form 
class TaskModelFrom(StyleForMixin,forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','due_date','assigned_to']
        # exclude = ['project', 'is_completed', 'created_at', 'updated_at']
        widgets = {
            'due_date' : forms.SelectDateWidget,
            'assigned_to': forms.CheckboxSelectMultiple
        }


# """Widget using mixins"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()


class TaskDetailsModelForm(StyleForMixin,forms.ModelForm):
    class Meta:
        model = TaskDetails
        fields = ['priority','notes']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
    
     
    

