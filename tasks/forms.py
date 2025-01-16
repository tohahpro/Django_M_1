from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=250)
    description = forms.CharField()