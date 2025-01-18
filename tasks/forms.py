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


# Use Form Mixins for Clean Code
class StyleForMixin:
    """ Mixin to apply style to form field """

    default_classes = "border border-gray-300 w-full rounded shadow-sm focus:border-rose-500 focus:ring-rose-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class' : self.default_classes,
                    'placeholder' : f'Enter {field.label.lower()}'
                })
            
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class' : f'{self.default_classes}',
                    'placeholder' : f'Enter {field.label.lower()}'
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class' : "border border-gray-300 space-y-2 py-1 rounded shadow-sm focus:border-rose-500 focus:ring-rose-500"                    
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class' : "space-y-2"
                })
            else:
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


# '''Manual widget'''
        # widgets = {
        #     'title':forms.TextInput(attrs={
        #         'class':"border border-gray-300 w-full rounded shadow-sm focus:border-rose-500 focus:ring-rose-500", 'placeholder':"Enter Task title"
        #     }),
        #     'description': forms.Textarea(attrs={
        #         'class':"border border-gray-300 w-full rounded shadow-sm focus:border-rose-500 focus:ring-rose-500", 'placeholder':"Enter your description"
        #     }),
        #     'due_date': forms.SelectDateWidget(attrs={
        #         'class':"border border-gray-300 shadow-sm focus:border-rose-500 focus:ring-rose-500"
        #     }),
        #     'assigned_to': forms.CheckboxSelectMultiple
        # }

# """Widget using mixins"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()



    
     
    

